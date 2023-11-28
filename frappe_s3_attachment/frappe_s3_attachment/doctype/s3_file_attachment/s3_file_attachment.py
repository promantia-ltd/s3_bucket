# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import gzip_decompress
from frappe.desk.form.load import get_attachments
from frappe_s3_attachment.controller import get_file
import requests


class S3FileAttachment(Document):
	pass

def validate_file_url(self):
	if self.is_remote_file or not self.file_url:
		return

	if not self.file_url.startswith(("/files/", "/private/files/","/api/method/")):
		# Probably an invalid URL since it doesn't start with http either
		frappe.throw(
			_("URL must start with http:// or https://","/api/method/"),
			title=_("Invalid URL"),
		)

def  get_prepared_data(self, with_file_name=False):
	if attachments := get_attachments(self.doctype, self.name):
		attachment = attachments[0]
		attached_file = frappe.get_doc("File", attachment.name)

		s3_url=get_file(attached_file.content_hash,attached_file.name)
		response=requests.get(s3_url)
		attached_file.file_url=s3_url
		if response.status_code==200:
			gzip= gzip_decompress(response.content)
			return gzip
		else :
			return
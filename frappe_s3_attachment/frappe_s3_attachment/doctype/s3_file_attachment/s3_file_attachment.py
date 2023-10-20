# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class S3FileAttachment(Document):
	pass

def validate_file_url(self):
	if self.is_remote_file or not self.file_url:
		return

	if not self.file_url.startswith(("/files/", "/private/files/","/api/method/")):
		# Probably an invalid URL since it doesn't start with http either
		frappe.throw(
			_("URL must start with http:// or https://"),
			title=_("Invalid URL"),
		)
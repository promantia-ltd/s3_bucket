# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

import frappe
import frappe.core.doctype.file.file
import frappe_s3_attachment.frappe_s3_attachment.doctype.s3_file_attachment.s3_file_attachment as _custom

frappe.core.doctype.file.file.File.validate_file_url = _custom.validate_file_url


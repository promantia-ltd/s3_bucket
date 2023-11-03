# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

import frappe
import frappe.core.doctype.file.file
import frappe_s3_attachment.frappe_s3_attachment.doctype.s3_file_attachment.s3_file_attachment as _custom
import frappe.core.doctype.prepared_report.prepared_report



frappe.core.doctype.file.file.File.validate_file_url = _custom.validate_file_url
frappe.core.doctype.prepared_report.prepared_report. PreparedReport.get_prepared_data = _custom.get_prepared_data


# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from werkzeug.useragents import UserAgent


def get_context(context):
	context.user_agent = UserAgent(frappe.request.headers.get("User-Agent"))


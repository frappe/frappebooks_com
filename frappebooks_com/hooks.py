# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappebooks_com"
app_title = "Frappe Books Website"
app_publisher = "Frappe Technologies"
app_description = "Website for Frappe Books"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "developers@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappebooks_com/css/frappebooks_com.css"
# app_include_js = "/assets/frappebooks_com/js/frappebooks_com.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappebooks_com/css/frappebooks_com.css"
# web_include_js = "/assets/frappebooks_com/js/frappebooks_com.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappebooks_com.utils.get_home_page"

update_website_context = ["frappebooks_com.website_context.get_context"]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappebooks_com.install.before_install"
# after_install = "frappebooks_com.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappebooks_com.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappebooks_com.tasks.all"
# 	],
# 	"daily": [
# 		"frappebooks_com.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappebooks_com.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappebooks_com.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappebooks_com.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappebooks_com.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappebooks_com.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappebooks_com.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


app_name = "qcs_uae_simple_ot"
app_title = "Qcs Uae Simple Ot"
app_publisher = "QCS"
app_description = "A simple OT tool for UAE"
app_email = "info@quarkcs.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qcs_uae_simple_ot/css/qcs_uae_simple_ot.css"
# app_include_js = "/assets/qcs_uae_simple_ot/js/qcs_uae_simple_ot.js"

# include js, css files in header of web template
# web_include_css = "/assets/qcs_uae_simple_ot/css/qcs_uae_simple_ot.css"
# web_include_js = "/assets/qcs_uae_simple_ot/js/qcs_uae_simple_ot.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qcs_uae_simple_ot/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "qcs_uae_simple_ot/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "qcs_uae_simple_ot.utils.jinja_methods",
# 	"filters": "qcs_uae_simple_ot.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "qcs_uae_simple_ot.install.before_install"
# after_install = "qcs_uae_simple_ot.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qcs_uae_simple_ot.uninstall.before_uninstall"
# after_uninstall = "qcs_uae_simple_ot.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "qcs_uae_simple_ot.utils.before_app_install"
# after_app_install = "qcs_uae_simple_ot.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "qcs_uae_simple_ot.utils.before_app_uninstall"
# after_app_uninstall = "qcs_uae_simple_ot.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qcs_uae_simple_ot.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Quotation": {
# 		"validate": "qcs_uae_simple_ot.controller.quotation.check_dis",
# 	}
# }



fixtures = [
	{
		"dt": "Custom Field", "filters": [
			[
				"name", "in", [
					'Company-custom_sales_manager_max_discount',
					'Company-custom_sales_man_max_discount',
					'Additional Salary-custom_ot_hours',
					'Additional Salary-custom_basic_salary',
					'Additional Salary-custom_simple_it'
				]
			]
		],

	},
	
]
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qcs_uae_simple_ot.tasks.all"
# 	],
# 	"daily": [
# 		"qcs_uae_simple_ot.tasks.daily"
# 	],
# 	"hourly": [
# 		"qcs_uae_simple_ot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qcs_uae_simple_ot.tasks.weekly"
# 	],
# 	"monthly": [
# 		"qcs_uae_simple_ot.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "qcs_uae_simple_ot.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qcs_uae_simple_ot.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qcs_uae_simple_ot.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["qcs_uae_simple_ot.utils.before_request"]
# after_request = ["qcs_uae_simple_ot.utils.after_request"]

# Job Events
# ----------
# before_job = ["qcs_uae_simple_ot.utils.before_job"]
# after_job = ["qcs_uae_simple_ot.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"qcs_uae_simple_ot.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


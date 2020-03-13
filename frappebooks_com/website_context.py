# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe, requests
from werkzeug.useragents import UserAgent


def get_context(context):
	user_agent = UserAgent(frappe.request.headers.get("User-Agent"))
	platform = user_agent.platform

	context.download_links = get_download_links()
	context.default_download_link = "https://github.com/frappe/books/releases/latest"

	if platform == "macos":
		context.platform = "macOS"
	elif platform == "windows":
		context.platform = "Windows"
	elif platform == "linux":
		context.platform = "Linux"

	context.developer_mode = frappe.conf.developer_mode


def get_download_links():
	def get_from_github():
		# find the download links from the latest release
		try:
			response = requests.get(
				"https://api.github.com/repos/frappe/books/releases/latest"
			)
		except Exception:
			return {}

		if response.ok:
			data = response.json()
			assets = data["assets"]

			platform_download_links = {}
			for asset in assets:
				browser_download_url = asset["browser_download_url"]
				extension = browser_download_url.rsplit(".", 1)[1]
				if extension == "dmg":
					platform_download_links["macOS"] = browser_download_url
				elif extension == "exe":
					platform_download_links["Windows"] = browser_download_url
				elif extension == "AppImage":
					platform_download_links["Linux"] = browser_download_url

			frappe.cache().hset("books_download_links", data["name"], platform_download_links)
			return platform_download_links

		return {}

	links = frappe.cache().hgetall("books_download_links")

	if not links:
		return get_from_github()

	versions = list(links.keys()).sort()

	if not versions:
		return get_from_github()

	latest_version = versions[-1]
	return links.get(latest_version, {})

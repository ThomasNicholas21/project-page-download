import pymupdf
from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright, urls: list[str]):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    for url in urls:
        page.goto(url)
    browser.close()


class UrlService:
    def __init__(self):
        pass

    def get_url(self):
        with sync_playwright() as playwright:
            run(playwright)


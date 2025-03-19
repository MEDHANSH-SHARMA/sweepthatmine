import time
from playwright.sync_api import sync_playwright
from engine import *

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sweepthatmine.vercel.app/")
    run(page, 5, 5)
    # ---------------------
    context.close()
    browser.close()
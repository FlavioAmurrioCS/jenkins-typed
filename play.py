# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "playwright>=1.59.0",
# ]
# ///


import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://localhost:55440")
        await page.get_by_label("Administrator password").fill("Hello")
        await browser.close()


asyncio.run(main())

from playwright.sync_api import sync_playwright


class ChartinkFetcher:

    def fetch(self, url):

        with sync_playwright() as p:

            browser = p.chromium.launch()

            page = browser.new_page()

            page.goto(url)

            rows = page.locator("table tbody tr").all()

            symbols = []

            for row in rows:

                symbol = row.locator("td").nth(2).inner_text()

                symbols.append(symbol)

            browser.close()

            return symbols
import time

from rich.live import Live
from rich.table import Table

from data import Product


URLS = [
    "https://www.amazon.com/dp/0544445783",
    "https://www.amazon.com/dp/0593499581",
]

products: list[Product] = []


def create_product_table() -> Table:

    table = Table(show_lines=True)
    table.add_column("Status")
    table.add_column("Title")
    table.add_column("Current Price")
    table.add_column("Dream Price")

    for product in products:
        color: str = "red"
        if product.is_affordable():
            color = "green"

        table.add_row(
            "[yellow]Scrapping..." if product.is_scraping else "Idle",
            product.title,
            f"[{color}]{product.current_price}",
            f"{product.dream_price}",
        )

    return table


if __name__ == "__main__":

    for url in URLS:
        products.append(Product(url, 1.00))

    with Live(create_product_table(), refresh_per_second=1) as live:
        while True:
            for product in products:
                product.is_scraping = True
                live.update(create_product_table())

                product.scrape()
                live.update(create_product_table())

                if product.is_affordable():
                    # send email
                    pass

            time.sleep(60)

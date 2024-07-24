import time
from argparse import ArgumentParser, Namespace

from rich.live import Live
from rich.table import Table

import config
from data import Product


AMAZON_PRODUCT_LINK = "https://www.amazon.com/dp"
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

    for [product_id, dream_price] in config.args.item:
        products.append(
            Product(f"{AMAZON_PRODUCT_LINK}/{product_id}", float(dream_price))
        )

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

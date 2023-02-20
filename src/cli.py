import argparse

# from webtoon_scraper.webtoon import Webtoon
# from webtoon_scraper.storage import Storage
from scraper.scraper import Scraper
from enum import Enum


def parse_args():
    # TODO: change choices to enums
    parser = argparse.ArgumentParser(description="Manhwa scraper cli")
    parser.add_argument(
        "website",
        type=str,
        choices=["webtoon", "asura"],
        help="The website to scrape the manhwa from",
    )

    subparsers = parser.add_subparsers(help="commands", dest="mode")

    list_parser = subparsers.add_parser("list", help="Lists all manhwas")
    list_parser.add_argument(
        "--sort",
        type=str,
        choices=["alph", "pop"],
        default="pop",
        help="Sorting criteria to list the manhwas",
    )
    list_parser.add_argument(
        "--limit", type=int, default=None,
        help="Limits the amount of manhwa displayed"
    )

    search_parser = subparsers.add_parser(
            "search", help="Search a specific manhwa")

    search_parser.add_argument(
        "--title", type=str, help="The title of the webtoon to scrape"
    )
    search_parser.add_argument(
        "--url", type=str, help="The url of the webtoon to scrape"
    )

    download_parser = subparsers.add_parser(
        "download", help="Download a specified manhwa"
    )
    download_parser.add_argument(
        "--title", type=str, help="The title of the webtoon to scrape"
    )
    download_parser.add_argument(
        "--url", type=str, help="The url of the webtoon to scrape"
    )
    download_parser.add_argument(
        "--storage",
        type=str,
        choices=["local", "database"],
        default="local",
        help="The storage mechanism of the manhwa",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # scraper = Scraper(args.website)
    # webtoon = scraper.scrape(args.webtoon_id)
    # st = Storage(args.storage)
    # st.store(webtoon)
    # print(f'Webtoon {webtoon.title} has been scraped successfully')
    # scraper = Scraper(website=args.website)
    # webtoon = scraper.scrape(manhwa_title=args.title)


if __name__ == "__main__":
    main()

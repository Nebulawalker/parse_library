import requests
import argparse
import time
import sys

from download import download_txt, download_image
from parsers import get_book_description
from custom_check import check_for_redirect
from urllib.parse import urljoin
from tululu_urls import TULULU_URL, TULULU_BOOK_DOWNLOAD_TXT_LINK


def main():
    argparser = argparse.ArgumentParser(
        description="Скрипт для скачивания книг с сайта tululu.org."
    )
    argparser.add_argument(
        '--start_id',
        help='id Книги, с которой нужно начать скачивание (по умолчанию 1).',
        default=1,
        type=int)
    argparser.add_argument(
        '--end_id',
        help='id Книги, где нужно завершить скачивание (по умолчанию 10).',
        default=10,
        type=int
    )

    args = argparser.parse_args()

    for book_id in range(args.start_id, args.end_id + 1):
        try:
            book_url = f'{urljoin(TULULU_URL, f"b{book_id}")}/'
            response = requests.get(book_url)
            response.raise_for_status()
            check_for_redirect(response)
            book_description = get_book_description(response)
            book_title = book_description['book_title']
            download_txt(
                TULULU_BOOK_DOWNLOAD_TXT_LINK,
                {'id': book_id},
                f'{book_id}.{book_title}'
            )
            download_image(book_description["book_cover_url"])
        except requests.exceptions.HTTPError as error:
            print(error, file=sys.stderr)
            continue

        except requests.exceptions.ConnectionError as error:
            print(error, file=sys.stderr)
            time.sleep(5)
            continue


if __name__ == '__main__':
    main()

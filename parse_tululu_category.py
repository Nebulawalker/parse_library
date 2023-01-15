import requests
import sys
import time
import json
import argparse

from urllib.parse import urlsplit
from parsers import get_book_description, get_book_urls
from download import download_image, download_txt
from custom_check import check_for_redirect
from tululu_urls import TULULU_SCI_FI_URL, TULULU_BOOK_DOWNLOAD_TXT_LINK


def main():
    argparser = argparse.ArgumentParser(
        description="Скрипт для скачивания книг \
            из категории Sci-fi с сайта tululu.org."
    )
    argparser.add_argument(
        '--start_page',
        help='Номер страницы, \
            с которой нужно начать скачивание (по умолчанию 1).',
        default=1,
        type=int)
    argparser.add_argument(
        '--end_page',
        help='Номер страницы, \
            где нужно завершить скачивание (по умолчанию 2).',
        default=1,
        type=int
    )
    argparser.add_argument(
        '--dest_folder',
        help='Каталог для сохранения книг(по умолчанию books).',
        default='books',
        type=str
    )
    argparser.add_argument(
        '--skip_imgs',
        action='store_true',
        help='Не скачивать изображения (по умолчанию скачивать).'
    )
    argparser.add_argument(
        '--skip_txt',
        action='store_true',
        help='Не скачивать книги (по умолчанию скачивать).'
    )
    argparser.add_argument(
        '--json_path',
        help='Путь к файлу JSON с описанием книг (default: books.json).',
        type=str,
        default='books.json'
    )
    args = argparser.parse_args()

    book_urls = get_book_urls(
        TULULU_SCI_FI_URL,
        args.start_page,
        args.end_page
    )
    book_descriptions = []
    for book_url in book_urls:
        book_id = urlsplit(book_url).path.strip('/').strip('b')
        try:
            response = requests.get(book_url)
            response.raise_for_status()
            check_for_redirect(response)
            book_description = get_book_description(response)
            book_title = book_description['book_title']
            if not args.skip_txt:
                book_description[
                    'book_path'
                ] = download_txt(
                        TULULU_BOOK_DOWNLOAD_TXT_LINK,
                        {'id': book_id},
                        f'{book_id}.{book_title}',
                        args.dest_folder
                    )
            if not args.skip_imgs:
                book_description[
                    'img_src'
                ] = download_image(
                    book_description["book_cover_url"]
                    )

            book_descriptions.append(book_description)
        except requests.exceptions.HTTPError as err:
            print(err, file=sys.stderr)
            continue
        except requests.exceptions.ConnectionError as err:
            print(err, file=sys.stderr)
            time.sleep(5)
            continue

    with open(args.json_path, "w", encoding="utf8") as file:
        json.dump(book_descriptions, file, ensure_ascii=False)


if __name__ == '__main__':
    main()

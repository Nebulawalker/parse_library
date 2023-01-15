import requests
import sys
import time
import json

from urllib.parse import urlsplit
from parsers import get_book_description, get_book_urls
from download import download_image, download_txt
from custom_check import check_for_redirect
from tululu_urls import TULULU_SCI_FI_URL, TULULU_BOOK_DOWNLOAD_TXT_LINK


def main():
    book_urls = get_book_urls(TULULU_SCI_FI_URL, 1, 2)
    book_descriptions = []
    for book_url in book_urls:
        book_id = urlsplit(book_url).path.strip('/').strip('b')
        try:
            response = requests.get(book_url)
            response.raise_for_status()
            check_for_redirect(response)
            book_description = get_book_description(response)
            book_title = book_description['book_title']
            book_description['book_path'] = download_txt(
                                                TULULU_BOOK_DOWNLOAD_TXT_LINK,
                                                {'id': book_id},
                                                f'{book_id}.{book_title}'
                                            )
            book_description['img_src'] = download_image(
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

    with open('books.json', "w", encoding="utf8") as file:
        json.dump(book_descriptions, file, ensure_ascii=False)


if __name__ == '__main__':
    main()

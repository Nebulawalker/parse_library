import requests
import argparse
import time
import sys
from download import download_txt, download_image
from parsers import get_book_description

TULULU_BOOK_DOWNLOAD_TXT_LINK = 'https://tululu.org/txt.php'
TULULU_URL = 'https://tululu.org/'


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

    for index in range(args.start_id, args.end_id + 1):
        payload = {'id': index}
        try:
            book_description = get_book_description(TULULU_URL, index)
            book_title = book_description['book_title']
            download_txt(
                TULULU_BOOK_DOWNLOAD_TXT_LINK,
                payload,
                f'{index}. {book_title}'
            )
            download_image(book_description["book_cover_url"])
        except requests.exceptions.HTTPError as error:
            print(error, file=sys.stderr)
            continue

        except requests.exceptions.ConnectionError as error:
            print(error, file=sys.stderr)
            time.sleep(5)
            continue

        print(f'Заголовок: {book_description["book_title"]}')
        print(f'Жанр: {book_description["book_genre"]}')
        print(f'Ссылка на обложку: {book_description["book_cover_url"]}')
        print(f'Комментарии: \n{book_description["book_comments"]}\n')


if __name__ == '__main__':
    main()

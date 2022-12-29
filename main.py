import requests
import argparse
from download import download_txt, download_image
from parsers import BookParser

TULULU_BOOK_DOWNLOAD_TXT_LINK = 'https://tululu.org/txt.php'
TULULU_URL = 'https://tululu.org/'


def check_for_redirect(response):
    if response.history:
        raise requests.exceptions.HTTPError


def main():
    argparser = argparse.ArgumentParser(
        description="Скрипт для скачивания книг с сайта tululu.org"
    )
    argparser.add_argument(
        '--start_id',
        help = 'id Книги, с которой нужно начать скачивание (по умолчанию 1)',
        default=1,
        type=int)
    argparser.add_argument(
        '--end_id',
        help='id Книги, на которой нужно завершить скачивание (по умолчанию 10)',
        default=10,
        type=int
    )

    start_id = argparser.parse_args().start_id
    end_id = argparser.parse_args().end_id

    for index in range(start_id, end_id+1):
        payload = {'id': index}
        response = requests.get(TULULU_BOOK_DOWNLOAD_TXT_LINK, params=payload)
        response.raise_for_status()
        try:
            check_for_redirect(response)
        except requests.exceptions.HTTPError:
            continue
        correct_url = response.url
        book_description = BookParser(TULULU_URL, index)
        download_txt(
            correct_url,
            f'{index}. {book_description.get_book_title()}'
        )
        download_image(book_description.get_book_cover_url())

        print(f'Заголовок: {book_description.get_book_title()}')
        print(f'Жанр: {book_description.get_book_genre()}')
        print(f'Ссылка на обложку: {book_description.get_book_cover_url()}')
        print(f'Комментарии: \n{book_description.get_book_comments()}\n')
        

if __name__ == '__main__':
    main()
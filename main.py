import requests
from download import download_txt
from parsers import parse_book_name_author

TULULU_BOOK_DOWNLOAD_TXT_LINK = 'https://tululu.org/txt.php'
TULULU_BOOK_DESCRIPTION_LINK = 'https://tululu.org/b'


def check_for_redirect(response):
    if response.history:
        raise requests.exceptions.HTTPError


def main():
    for index in range(1, 11):
        payload = {'id': index}
        response = requests.get(TULULU_BOOK_DOWNLOAD_TXT_LINK, params=payload)
        response.raise_for_status()
        try:
            check_for_redirect(response)
        except requests.exceptions.HTTPError:
            continue
        correct_url = response.url
        download_txt(
            correct_url,
            f'{index}. {parse_book_name_author(TULULU_BOOK_DESCRIPTION_LINK, index)[0]}'
        )      
        

if __name__ == '__main__':
    main()
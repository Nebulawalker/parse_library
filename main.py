import requests
from download import download_txt, download_image
from parsers import BookParser

TULULU_BOOK_DOWNLOAD_TXT_LINK = 'https://tululu.org/txt.php'
TULULU_URL = 'https://tululu.org/'


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
        book_description = BookParser(TULULU_URL, index)
        download_txt(
            correct_url,
            f'{index}. {book_description.book_title}'
        )
        download_image(book_description.book_image_url)

        print(f'Заголовок: {book_description.book_title}')
        print(book_description.book_image_url)      
        

if __name__ == '__main__':
    main()
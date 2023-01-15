import requests
import sys
import time

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from custom_check import check_for_redirect
from main import TULULU_URL


def get_book_title(soup):
    book_title = soup.find('h1').text.split('::')[0].strip()
    return book_title


def get_book_author(soup):
    book_author = soup.find('h1').text.split('::')[1].strip()
    return book_author


def get_book_cover_url(response, soup):
    book_cover_url = urljoin(
        response.url,
        soup.find('div', class_='bookimage').find('img')['src']
    )
    return book_cover_url


def get_book_comments(soup):
    raw_comments = soup.find_all('div', class_='texts')
    book_comments = [
        book_comment.find('span').text for book_comment in raw_comments
    ]
    return book_comments


def get_book_genre(soup):
    raw_genres = soup.find('span', class_='d_book').find_all('a')
    genres = [genre.text for genre in raw_genres]
    return genres


def get_book_description(response):
    soup = BeautifulSoup(response.text, 'lxml')
    return {
        'book_title': get_book_title(soup),
        'book_author': get_book_author(soup),
        'book_cover_url': get_book_cover_url(response, soup),
        'book_comments': get_book_comments(soup),
        'book_genre': get_book_genre(soup)
    }


def get_book_urls(url, start_page, end_page):
    book_urls = []
    for page in range(start_page, end_page):
        try:
            response = requests.get(urljoin(url, str(page)))
            response.raise_for_status()
            check_for_redirect(response)
            soup = BeautifulSoup(response.text, 'lxml')
            book_sections = soup.find_all('table', class_='d_book')
            for book_section in book_sections:
                book_link = book_section.find('a')['href']
                book_url = urljoin(TULULU_URL, book_link)
                book_urls.append(book_url)
        except requests.exceptions.HTTPError as err:
            print(err, file=sys.stderr)
            continue
        except requests.exceptions.ConnectionError as err:
            print(err, file=sys.stderr)
            time.sleep(5)
            continue
    return book_urls

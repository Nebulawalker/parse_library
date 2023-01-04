from bs4 import BeautifulSoup
from urllib.parse import urljoin


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
    return '\n'.join(book_comments)


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

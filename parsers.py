import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

class BookParser:
    def __init__(self, url, book_id) -> None:
        self.book_html_page = requests.get(f'{urljoin(url, f"b{book_id}")}')
        self.book_html_page.raise_for_status
        self.soup = BeautifulSoup(self.book_html_page.text, 'lxml')

    def get_book_title(self):
        book_title = self.soup.find('h1').text.split('::')[0].strip()
        return book_title

    def get_book_cover_url(self):
        book_cover_url = urljoin(
            self.book_html_page.url,
            self.soup.find('div', class_='bookimage').find('img')['src']
        )
        return book_cover_url

    def get_book_comments(self):
        raw_comments = self.soup.find_all('div', class_='texts')
        book_comments = []
        for raw_comment in raw_comments:
            book_comments.append(raw_comment.find('span').text)
        return '\n'.join(book_comments)
    
    def get_book_genre(self):
        raw_genres = self.soup.find('span', class_='d_book').find_all('a')
        genres = []
        for genre in raw_genres:
            genres.append(genre.text)
        return genres




import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

class BookParser:
    def __init__(self, url, book_id) -> None:
        self.book_html_page = requests.get(f'{urljoin(url, f"b{book_id}")}')
        self.book_html_page.raise_for_status
        self.soup = BeautifulSoup(self.book_html_page.text, 'lxml')
        self.book_title = self.soup.find('h1').text.split('::')[0].strip()
        self.book_image_url = urljoin(
            self.book_html_page.url,
            self.soup.find('div', class_='bookimage').find('img')['src']
        )
    
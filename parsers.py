import requests
from bs4 import BeautifulSoup


def parse_book_name_author(url, book_id):
    book_description_url = f'{url}{book_id}'
    response = requests.get(book_description_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    book_name, book_author = soup.find('h1').text.split('::')
    return book_name.strip(), book_author.strip()


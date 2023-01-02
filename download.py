import requests
import os

from pathvalidate import sanitize_filename
from urllib.parse import urlsplit


def check_for_redirect(response):
    print(response.history)
    print(response.status_code)
    if response.history:
        print('Page not found, redirecting')
        raise requests.exceptions.HTTPError


def download_txt(url, payload, filename, folder='books/'):
    """Функция для скачивания текстовых файлов.
    Args:
        url (str): Cсылка на текст, который хочется скачать.
        filename (str): Имя файла, с которым сохранять.
        folder (str): Папка, куда сохранять.
    Returns:
        str: Путь до файла, куда сохранён текст.
    """
    response = requests.get(url, params=payload)
    response.raise_for_status()
    check_for_redirect(response)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f'{sanitize_filename(filename)}.txt')
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath


def download_image(url, folder='images/'):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(folder, exist_ok=True)
    filename = os.path.split(urlsplit(url).path)[1]
    filepath = os.path.join(
        folder, filename)

    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath

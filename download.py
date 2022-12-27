import requests
import os

from pathvalidate import sanitize_filename


def download_txt(url, filename, folder='books/'):
    """Функция для скачивания текстовых файлов.
    Args:
        url (str): Cсылка на текст, который хочется скачать.
        filename (str): Имя файла, с которым сохранять.
        folder (str): Папка, куда сохранять.
    Returns:
        str: Путь до файла, куда сохранён текст.
    """
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f'{sanitize_filename(filename)}.txt')
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath
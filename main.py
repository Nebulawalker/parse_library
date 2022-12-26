import requests
import os

book_link = 'https://tululu.org/txt.php'


def main():
    os.makedirs('books', exist_ok=True)

    for index in range(0, 10):
        payload = {'id': index}
        response = requests.get(book_link, params=payload)
        response.raise_for_status()
        path = os.path.join('books', f'id {index}.txt')
        with open(path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    main()
import requests


book_link = 'https://tululu.org/txt.php?id=32168'

def main():
    response = requests.get(book_link)
    response.raise_for_status()
    filename = '1.txt'
    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    main()
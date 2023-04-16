import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from livereload import Server
from more_itertools import chunked


def render_page():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    with open('books.json', 'r', encoding='utf-8') as file:
        books = json.load(file)

    template = env.get_template('template.html')

    chunked_books = list(chunked(books, 4))

    for page, books_on_page in enumerate(chunked_books):
        rendered_page = template.render(
            books=list(chunked(books_on_page, 2)),
            current_page=page + 1,
            total_pages=len(chunked_books)
        )

        with open(
            os.path.join('pages', f'index{page+1}.html'),
            'w', encoding="utf-8"
        ) as file:
            file.write(rendered_page)


if __name__ == '__main__':
    os.makedirs('pages', exist_ok=True)
    render_page()
    server = Server()
    server.watch('template.html', render_page)
    server.serve(root='.', default_filename='pages/index1.html')

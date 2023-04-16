import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from livereload import Server
from more_itertools import chunked
from pprint import pprint


def render_page():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    with open('books.json', 'r', encoding='utf-8') as file:
        books = json.load(file)

    template = env.get_template('template.html')

    for page, books_on_page in enumerate(list(chunked(books, 5))):
        # pprint(page)
        # pprint(books_on_page)
        rendered_page = template.render(
            books=list(chunked(books_on_page, 2))
        )

        with open(os.path.join('pages', f'index{page+1}.html'), 'w', encoding="utf-8") as file:
            file.write(rendered_page)
# render_page()

if __name__ == '__main__':
    os.makedirs('pages', exist_ok=True)
    render_page()
    server = Server()
    server.watch('template.html', render_page)
    server.serve(root='.')

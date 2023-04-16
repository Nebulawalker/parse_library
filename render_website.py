import json

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

    rendered_page = template.render(
        books=list(chunked(books, 2))
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    render_page()
    server = Server()
    server.watch('template.html', render_page)
    server.serve(root='.')

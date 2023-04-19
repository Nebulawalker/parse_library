import json
import os
import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def get_json_path():
    argparser = argparse.ArgumentParser(
            description='Скрипт для запуска сайта с домашней библиотекой'
    )
    argparser.add_argument(
            '--json_path',
            help='Путь к файлу JSON с описанием книг (default: books.json).',
            type=str,
            default='books.json'
        )
    return argparser.parse_args()


def render_page():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    json_path = get_json_path().json_path
    with open(json_path, 'r', encoding='utf-8') as file:
        book_descriptions = json.load(file)
    book_descriptions_by_pages = list(chunked(book_descriptions, 4))

    for page, book_descriptions_on_page in enumerate(
        book_descriptions_by_pages,
        start=1
    ):
        rendered_page = template.render(
            book_descriptions_on_page_sorted=list(
                chunked(book_descriptions_on_page, 2)
            ),
            current_page=page,
            total_pages=len(book_descriptions_by_pages)
        )
        with open(
            os.path.join('pages', f'index{page}.html'),
            'w', encoding="utf-8"
        ) as file:
            file.write(rendered_page)


if __name__ == '__main__':
    os.makedirs('pages', exist_ok=True)
    render_page()
    server = Server()
    server.watch('template.html', render_page)
    server.serve(root='.', default_filename='pages/index1.html')

# Домашняя оффлайн-библиотека

[![imageup.ru](https://imageup.ru/img210/4296800/snimok-ekrana-ot-2023-04-17-12-02-51.jpg)](https://imageup.ru/img210/4296800/snimok-ekrana-ot-2023-04-17-12-02-51.jpg.html)

Программа для скачивания книг и их описания с https://tululu.org/. А также сайт для удобного просмотра скачанных книг без необходимости подключения к интернету.

## Как установить

Для написания скрипта использовался __Python 3.10.0__.
Инструмент для управления зависимостями __Poetry__.
.
1. Склонировать репозиторий.
   
2. Создать виртуальное окружение.
3. Установить зависимости:
```
poetry install
```
## Самый простой способ запустить библиотеку
После скачивания библиотеки, нужно зайти в папку 'pages' и открыть в браузере файл 'index1.html'.

## Описание скриптов
### Запуск __parse_tululu_book__:
```bash
python parse_tululu_book.py 
```
По умолчанию, будут проверены и скачаны книги с id от 1 до 10. Можно изменить эти параметры.
Например:
```bash
python parse_tululu_book.py --start_id 100 --end_id 200
```
Будут проверены и скачаны книги с id от 100 до 200.

### Запуск __parse_tululu_category__ 
```bash
python parse_tululu_category.py 
``` 
Можно запускать с параметрами, описание ниже:
```text
Скрипт для скачивания книг из категории Sci-fi с сайта tululu.org.

options:
  -h, --help            show this help message and exit
  --start_page START_PAGE
                        Номер страницы, с которой нужно начать скачивание (по умолчанию 1).
  --end_page END_PAGE   Номер страницы, где нужно завершить скачивание (по умолчанию 2).
  --dest_folder DEST_FOLDER
                        Каталог для сохранения книг(по умолчанию books).
  --skip_imgs           Не скачивать изображения (по умолчанию скачивать).
  --skip_txt            Не скачивать книги (по умолчанию скачивать).
  --json_path JSON_PATH
                        Путь к файлу JSON с описанием книг (default: books.json).
```
Для использования сайта не меняйте значения по умолчанию у следующих параметров:
* --dest_folder
* --json_path

### Запуск __render_website.py__
1. Скачайте книги при помощи скрипта parse_tululu_category.py 
2. Запустите скрипт render_website.py:
   ```bash 
   python render_website.py
   ```
3.
```text
usage: render_website.py [-h] [--json_path JSON_PATH]

Скрипт для запуска сайта с домашней библиотекой

options:
  -h, --help            show this help message and exit
  --json_path JSON_PATH
                        Путь к файлу JSON с описанием книг (default: books.json).
```
4. Сайт будет доступен [тут. ](http://127.0.0.1:5500) Даже без интернета.
5. Пример сайта также доступен на [GitHub Pages.](https://nebulawalker.github.io/parse_library/pages/index1.html)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
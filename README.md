# Парсим онлайн-библиотеку

Программа для скачивания книг и их описания с сайта https://tululu.org/

## Как установить

Для написания скрипта использовался __Python 3.10.0__
Инструмент для управления зависимостями __Poetry__

1. Склонировать репозиторий.
2. Создать виртуальное окружение.
3. Установить зависимости:
```
poetry install
```

4. Запуск приложения:
```bash
python main.py
```
По умолчанию, будут проверены и скачаны книги с id от 1 до 10. Можно изменить эти параметры.
Например:
```bash
python main.py --start_id 100 --end_id 200
```
Будут проверены и скачаны книги с id от 100 до 200.



### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
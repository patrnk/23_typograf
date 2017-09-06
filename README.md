# Типограф

Расширяемый типограф, сделанный с помощью Flask и регулярных выражений.

![Пример использования](https://i.imgur.com/SNKagIi.png)

# Запуск
Требует Python 3.
```bash
$ pip install -r requirements.txt
$ python server.py
```

# Расширение
1. Написать в `utils.py` свою функцию, которая на вход принимает такие параметры: `text, additional_filter=''` и возвращает `text`.
2. Добавить эту функцию в список `filters` в том же файле.
3. Написать к ней юнит-тесты в `small_tests.py` и проверить, не ломает ли она HTML в `big_tests.py`.

# Запуск тестов
В зависимости от того, какие тесты надо запустить:
```bash
$ python small_tests.py
```
или
```bash
$ python big_tests.py
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
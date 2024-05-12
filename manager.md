Шаблоны не новые - давно использую их для работы. Правда, должен признать, что это было "неосознанное знание" - как-то сразу после знакомства с контекстным менеджером показалось что все операции, где есть обязательный завершающий шаг, удобнее делать именно через него

## Открытие файла для чтения/записи

Начальный вариант:

```python
fd = open("file.txt", "r")
try:
    lines = fd.read()
    print(lines)
finally:
    fd.close()
```

Вариант с контекстным менеджером:

```python
with open("file.txt", "r") as fd:
    lines = fd.read()
    print(lines)
```

## Работа с БД

Начальный вариант:

```python
import psycopg2

conn = psycopg2.connect(database="db", user="nix", password="qwerty", host="localhost", port=5432)
try:
    cur = conn.cursor()
    cur.execute("INSERT INTO emloyees (id, name) VALUES (1, 'Ivanov')")
finally:
    conn.close()
```

Вариант с контекстным менеджером:

```python
import psycopg2

with psycopg2.connect(database="db", user="nix", password="qwerty", host="localhost", port=5432) as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO emloyees (id, name) VALUES (1, 'Ivanov')")
```
## Запись в эксель-файл
Начальный вариант:

```python
import pandas as pd

excel_writer = pd.ExcelWriter(file_name, engine="xlsxwriter", mode='w')
try:
    df1.to_excel(excel_writer, sheet_name='Раздел 1', index=False)
finally:
    excel_writer.save()
```

Вариант с контекстным менеджером:

```python
import pandas as pd

with pd.ExcelWriter(file_name, engine="xlsxwriter", mode='w') as excel_writer:
    df1.to_excel(excel_writer, sheet_name='Раздел 1', index=False)
```

Использование таких конструкций имеет ряд преимуществ - код более выразителен, исключается возможность случайно забыть закрыть ресурс

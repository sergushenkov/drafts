## Одинаковая реализация - разная спецификация
Предположим, есть три разные задачи для разных таблиц:
1. Выполнить первичную загрузку таблицы
2. Обеспечить ежедневную репликацию таблицы
3. Загрузить таблицу с источника, чтобы найти строки, которые различаются с нашим экземпляром таблицы

Если таблица маленькая и в ширину и в длину - проще всего все три задачи решить одним способом - через полную выгрузку. Но если таблица растёт, то из-за разных спецификаций будут требоваться разные подходы в сопровождении.

Для первичной загрузки полное копирование так и останется единственным способом. Для ежедневной репликации - кажется более подходящим инкрементальное обновление. Для поиска расхождений - возможно стоит копировать не всю таблицу, а только хэш строк

## Полиморфизм или боксинг
Моя задача на полиморфизм - https://github.com/sergushenkov/drafts/blob/main/polymorphism.md

ИМХО, тут точно не боксинг - это именно расширение функционала одной и той же задачи, а не просто де-дублирование кода разных задач

## Необходимость пояснений
Необходимость заглядывать в код других файлов, чтобы разобраться со смыслом импортируемых структур данных и функций зависит от того, насколько качественно написан код.

Ключевый моменты, которые сильно снижают необходимость заглядывать в definition:
* Функция должна делать только одну задачу
* Код внутри функции должен относиться к одному уровню абстракции (условно - не смешивать бизнес-логику и нюансы записи в HDFS)
* Хороший нейминг - отражающий ту самую задачу функции
# Зависимость краша

Детали уже не помню, но в общих чертах - падал сервис на каких-то нодах, выяснилось что служба логирования на этих же нодах сжирала всё общее дисковое пространство. Решили через лимиты. В целом универсальное решение сложно сформулировать, наверное как и в предыдущем пункте

## Семантика
* Зависимость сборки - нет, собираются совершенно независимо друг от друга
* Зависимость времени выполнения - есть, так как используют общий ограниченный ресурс (дисковое пространство)
* Функциональные требования - нет, и службу логирования и целевой сервис могут быть заменены другими, при этом не нарушая работоспособности системы
## Характеристики
Стабильность работы сервиса зависит от "прожорливости" службы логирования, от того, есть ли у неё лимиты на потребление дискового пространства
## Допустимые изменения
Допустимы любые изменения в службе логирования, при условии что она не претендует на дисковое пространство, закреплённое за сервисом

# Зависимость фреймворка - 1

Возникла потребность в подключении из python к Greenplum, это традиционно делается с помощью pcycopg2, но в тот раз с этим возникла реальная проблема. Всё это требовалось сделать на корпоративном компе с заданными политиками безопасности, а psycopg2 при установке требует библиотеки, которые никак установить не получалось. Долго мучались, нашли какой-то вариант модуля с уже встроенными всеми библиотеками, тогда получилось.

## Семантика
* Зависимость сборки - да, проект не собрать без установленных библиотек
* Зависимость времени выполнения - да, проект использует функционал библиотеки
* Функциональные требования - да, проект нельзя перевести на использование другой библиотеки без значительной переделки кода
## Характеристики
Возможность запуска проекта зависит от наличия нужных библиотек в системе
## Допустимые изменения
Допустимы любые изменения в библиотеке, не затрагивающие возможности её использования, кроме добавления новых зависимостей уже самой библиотеки 

# Зависимость расшаренного формата

Работаем совместно с подрядчиком. Отлаживаю код на тестовом сервере. Всё ок. При попытке выполнить код на проде выясняется, что подрядчик использует новую версию таблиц, на которые перешёл не поставив меня в известность.
## Семантика
* Зависимость сборки - нет, работы на тесте и проде велись независимо друг от друга
* Зависимость времени выполнения - да, код падает при попытке использовать таблицы с незнакомой структурой
* Функциональные требования - да, требуется значительная переделка кода, хотя теоретически можно было бы встроить какой то промежуточный адаптер
## Характеристики
Работоспособность кода зависит от наименования колонок в используемых таблицах
## Допустимые изменения
Допустимы изменения в таблицах (сжатие, колоночная/строковая), при условии что наименования колонок, их тип и наложенные ограничения не меняются

# Зависимость фреймворка - 2

В рамках работы с подрядчиком, требуется обеспечить наполнение таблиц данными. После запуска проекта - данные будут заливаться через айрфлоу. Сейчас такой возможности нет, данные вставляются вручную из csv-файлов или даже прямыми insert запросами.

## Семантика
* Зависимость сборки - нет
* Зависимость времени выполнения - да. В рабочем проекте процессы будут завязаны друг на друга, после успешного заверешения одного будет автоматически стартовать другой. Сейчас это приходится делать вручную
* Функциональные требования - нет. Если при ручной заливке данных заполняются все необходимые таблицы, то основной код отработает успешно
## Характеристики 
Работоспоспобность кода зависит от наличия правильных данных в таблицах
## Допустимые изменения
Способ заливки данных может быть любым, при условии что не изменяются ddl-таблиц и заливаемые данные согласованы между собой
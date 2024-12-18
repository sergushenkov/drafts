## Пример 1
Система транзакций в SQL (учитывая только DML - data manipulation language) для версионных БД (Greenplum) по факту является свободным объектом. В DML не входят команды удаления столбцов/таблиц, а удаление строк в версионных БД происходит не через физическое удаление, а через пометку строки как удаленной, с сохранением предыдущей версии. Собственно, также происходит любое изменение строк. Т.е. при необходимости, если в промежутке не производилось операций (DDL - data definition language), то можно откатить таблицу на любой момент времени

## Пример 2
При CDC-репликации таблиц (CDC - change data capture) обрабатываются логи изменений таблицы-источника и далее на стороне-приемнике эти изменения последовательно применяются к целевой таблице. Сами эти логи не являются свободным объектом - если ты выполнил операцию изменения строки, то вернуться в исходное состояние уже невозможно. Но часто в паре с целевой таблицей создают историческую таблицу, где сохраняются все удаленные/изменненные строки с указанием момента изменений. Целевая таблица в паре с исторической таблицей уже будут свободным объектом

## Пример 3
Система версионирования git - практически свободный объект в чистом виде. Можно вернуть отслеживаемую область в любой момент времени

В своих задачах доводилось делать аналог исторических таблиц, чтобы в момент внесения изменений в отслеживаемую таблицу, сохранялись изменяемые строки вместе с указанием - кто и когда их поменял
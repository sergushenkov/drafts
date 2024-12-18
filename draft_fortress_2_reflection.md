## Задача 1

Логика одинаковая. Различия:

- в правильном варианте выводятся все поля через *, у меня только squad_id и name. Имхо, мой вариант лучше - вся инфа по отрядам не нужна, а id и название однозначно идентифицируют отряд

## Задача 2

Логика одинаковая. Различия:

- в правильном варианте выводятся все поля через *, у меня только id и name. Имхо, мой вариант лучше - вся инфа по дварфам не нужна, а id и название однозначно идентифицируют отряд

## Задача 3

Логика одинаковая. Различия:

- в правильном варианте выводятся все поля через *, у меня только id и name. Имхо, мой вариант лучше - вся инфа по дварфам не нужна, а id и название однозначно идентифицируют отряд
- в правильном варианте используется distinct, у меня group by - план запроса в данном кейсе будет одинаковый. distinct наверное нагляднее

## Задача 4

Логика схожая. Различия:

- В правильном варианте используется только таблица Tasks, у меня Dwarves left join Tasks - это позволяет вывести инфу и по тем дварфам, у которых нет задач
- В правильном варианте выводится только id дварфа, у меня id и name - более читаемо

## Задача 5

Логика схожая, различия:

- у меня почему то стоит left join вместо inner join - скорее всего скопипастил и не исправил, смысла в этом нет
- у меня выводится id задачи и описание, в правильном варианте - вся инфа по задаче

## Задача 6

Логика схожая, различия:

- Правильный вариант использует inner join, мой вариант - left join. Это позволяет не потерять гномов без родственников
- Правильный вариант выводит только имена, мой - дополнительно id. Это позволяет не запутаться при наличии однофамильцев

## Итоговые выводы

- По логике ошибок у меня нет
- Есть ошибка по невнимательности, не влияющая на результат - всё что скопировал и вставил, надо сразу исправлять под свою задачу. Ещё лучше - не копипастить
- В большинстве случаев расхождений, мой вариант мне кажется предпочтительным
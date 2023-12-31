Полноценный механизм добавления в проект нового модуля, подразумевающего повторное использование кода, должен отвечать всем пяти нижеприведённым принципам.

1. Новый модуль может задавать некоторый базовый тип, который потенциально должен допускать параметризацию другими типами (обобщённые типы, типы-генерики);

2. Новый модуль может объединять несколько функций, которые активно обращаются друг к другу;

3. Новый модуль может входить в семейство модулей, ориентированных на решение некоторой общей задачи, которую не удаётся решить с помощью одного модуля;

4. Новый модуль может предлагать конкретную реализацию родительского модуля, которая должна выбираться динамически (полиморфно) -- например, реализация обобщённого типа для конкретного типа-параметра;

5. Новый модуль может интегрировать общее поведение нескольких модулей, которые различаются лишь деталями.

Для python выполняются пункты 2 и 3. Пункт 5 можно реализовать. Пункты 1 и 4 не выполняются
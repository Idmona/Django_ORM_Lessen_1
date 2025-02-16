# Django ORM Watching Storage

## Описание проекта
Это учебный проект по Django, разработанный для отслеживания посещений сотрудников по пропускам. Пользователь может просматривать список посещений по конкретному пропуску и видеть, сколько времени человек провел внутри помещения.

## Функциональность
- Просмотр информации по каждому пропуску.
- Отображение времени входа и выхода для каждого посещения.
- Вывод продолжительности каждого посещения в удобном формате (`чч:мм:сс`).
- Проверка на длительные визиты (больше 1 часа) и их пометка.
- Обработка неправильных номеров пропусков с выводом страницы 404.

## Стек технологий
- **Язык:** Python 3.12
- **Фреймворк:** Django 3.2.25

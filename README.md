# Публикация комиксов

## Описание

Проект создан для публикации комиксов xkcd в Telegram.

## Установка

Скачайте необходимые файлы, затем используйте `рір` (или `рірз` , если есть конфликт с Python2) для установки зависимостей и
установить зависимости. Зависимости можно установить командой, представленной ниже. Создайте бота у отца ботов. Создайте новый канал в Telegram.

Установите зависимости командой:
```
pip install -r requirements.txt
```

## Пример запуска скрипта

Для запуска скрипта у вас уже должен быть установлен Python3.

Для публикации комиксов в Telegram необходимо написать:

```
python main.py
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Переменные окружения - это переменные, значения которых присваиваются программе Python извне. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.
Пример содержания файла `.env`:

```
TELEGRAM_TOKEN = "bot-token"
TG_CHAT_ID = "@chat id"
```

Получить токен `TG_TOKEN` можно у отца ботов. В описании канала получите название и положите в переменную `ТG_CHAT_ID` .
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
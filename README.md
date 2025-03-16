![Logo](logo.png)

## Задание

1. **Интеракция с ботом**:  
   Пользователь пишет боту в Telegram, и бот отвечает сообщением с кнопкой, ведущей на WebApp.

2. **Первый экран WebApp**:  
   Пользователь заходит в WebApp и видит первый экран с формой ввода даты рождения (см. скриншот).

3. **Второй экран WebApp**:  
   После ввода даты рождения, пользователь переходит на следующий экран, где отображаются следующие данные:
   - Имя пользователя
   - Фамилия пользователя
   - Юзернейм пользователя
   - Сколько дней/часов/минут осталось до его дня рождения

4. **Поделиться данными**:  
   На втором экране пользователь (далее "пользователь 1") может нажать на кнопку "Поделиться" и отправить ссылку на свои данные другому пользователю (далее "пользователь 2"). Пользователь 2, перейдя по ссылке, должен видеть те же данные, что и пользователь 1.


# Реализация

**Стек технологий**:  
- **Backend**: Python 3.12, Tortoise ORM, FastAPI, Aiogram, PostgreSQL  
- **Frontend**: Vue 3, TailwindCSS  


## Структура проекта:

- [`back`](back) - backend.
  - [`database`](back/database) - Подключение к бд с помощью Tortoise.
    - [`models`](back/database/models) - все модели бд.
      - [`tg_user.py`](back/database/models/tg_user.py) - модель пользователя TG.
  - [`Dockerfile`](back/Dockerfile) - файл для сборки бэкенда.
  - [`main.py`](back/main.py) - основной файл бэкенда.
  - [`requirements.txt`](back/requirements.txt) - зависимости для бэкенда.
- [`bot`](bot) - бот для Telegram.
  - [`Dockerfile`](bot/Dockerfile) - файл для сборки бота.
  - [`main.py`](bot/main.py) - основной файл бота.
  - [`requirements.txt`](bot/requirements.txt) - зависимости для бота.
- [`front`](front) - клиентская часть приложения на Vue с использованием Tailwind CSS.
  - [`public`](front/public) - статические файлы.
    - [`favicon.ico`](front/public/favicon.ico) - иконка vue для браузера.
  - [`src`](front/src) - исходный код фронтенд-приложения.
    - [`assets`](front/src/assets) - статические ресурсы.
      - [`tailwind.css`](front/src/assets/tailwind.css) - основной файл стилей для Tailwind.
    - [`components`](front/src/components) - Vue-компоненты приложения.
      - [`CreateCard.vue`](front/src/components/CreateCard.vue) - компонент для создания карточки.
      - [`Root.vue`](front/src/components/Root.vue) - корневой компонент приложения.
      - [`ViewCard.vue`](front/src/components/ViewCard.vue) - компонент для просмотра карточки.
    - [`router`](front/src/router) - роутер Vue-приложения.
      - [`index.js`](front/src/router/index.js) - конфигурация маршрутов.
    - [`App.vue`](front/src/App.vue) - главный Vue-компонент приложения.
    - [`main.js`](front/src/main.js) - точка входа в приложение.
  - [`Dockerfile`](front/Dockerfile) - файл для сборки Docker-образа фронтенда.
  - [`index.html`](front/index.html) - основной HTML-файл приложения.
  - [`package.json`](front/package.json) - список зависимостей и скрипты для запуска/сборки.
  - [`postcss.config.cjs`](front/postcss.config.cjs) - конфигурация PostCSS для Tailwind.
  - [`tailwind.config.js`](front/tailwind.config.js) - конфигурация Tailwind CSS.
  - [`vite.config.js`](front/vite.config.js) - конфигурация сборки с помощью Vite.
- [`docker-compose.yml`](docker-compose.yml) - файл для запуска всех сервисов.

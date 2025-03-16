# 1) Этап сборки (build)
FROM node:18-alpine AS build

WORKDIR /app

# Скопируем зависимости
COPY package*.json ./

# Устанавливаем их
RUN npm install

# Копируем оставшиеся файлы
COPY . .

# Собираем приложение в папку dist
RUN npm run build

# 2) Этап для запуска (без Nginx, используем serve)
FROM node:18-alpine

WORKDIR /app

# Устанавливаем "serve" глобально (или локально — на ваш выбор)
RUN npm install -g serve

# Копируем собранное приложение из этапа build
COPY --from=build /app/dist /app

# Порт, на котором будет доступно приложение внутри контейнера
EXPOSE 8080

# Запускаем "serve" на 8080
CMD ["serve", ".", "--single", "-l", "8080"]
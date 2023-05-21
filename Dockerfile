RUN apt-get update && apt-get install -y \
    python3-tk \
    xauth \
    x11-xserver-utils \
    && rm -rf /var/lib/apt/lists/*


# Базовый образ
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Установка зависимостей для Tkinter
RUN apt-get update && apt-get install -y python3-tk

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для взаимодействия с приложением
EXPOSE 8000


# Настройка переменных окружения для подключения к X-серверу
ENV DISPLAY=:0
ENV XAUTHORITY=/.Xauthority

# Добавление текущего пользователя в группу "video" для доступа к видеоустройству
RUN usermod -aG video root

# Запускаем приложение при старте контейнера
CMD ["python", "app.py"]

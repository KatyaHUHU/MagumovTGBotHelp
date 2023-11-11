# Используйте официальный образ Python как родительский образ
FROM python:3.8-slim

# Установите рабочую директорию в контейнере
WORKDIR /bot

RUN git clone https://github.com/KatyaHUHU/MagumovTGBotHelp.git

# Копируйте файлы в контейнер
COPY . /bot

# Установите необходимые пакеты
RUN pip install --no-cache-dir -r requirements.txt

# Запустите бота при запуске контейнера
CMD ["python", "./MagBot.py"]
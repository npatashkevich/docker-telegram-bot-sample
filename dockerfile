FROM python:3.10-slim

# Обновление пакетов и установка зависимостей для сборки
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    libc-dev \
    make

ENV TOKEN='6416166352:AAEfXS_Nx2KSDKHrbwqrFfWsGAd4SjUUMmc'


COPY . . 
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "LatinizatorBot.py"]

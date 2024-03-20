# Используем официальный образ Python в качестве базового образа
FROM python:3.9

# Устанавливаем зависимости FastAPI и uvicorn (ASGI сервер)
RUN pip install fastapi uvicorn

# Копируем код нашего FastAPI приложения в контейнер
COPY main.py .

EXPOSE 8000

# Определяем команду для запуска FastAPI приложения через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

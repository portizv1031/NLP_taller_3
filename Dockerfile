FROM python:3.9

WORKDIR /app
COPY app_translate.py requirements.txt /app/
COPY templates /app/templates

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "app_translate.py"]

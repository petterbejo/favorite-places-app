FROM python:3.11-alpine

WORKDIR /app

RUN pip3 install folium Flask gunicorn psycopg2-binary

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

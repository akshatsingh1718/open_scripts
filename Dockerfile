FROM python:3.11

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . open_scripts

WORKDIR /open_scripts

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
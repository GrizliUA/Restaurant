# Dockerfile

FROM python:3.9.7
LABEL key="Restaurant API Project"

# COPY requirement.txt requirement.txt
RUN pip install -r /requirement.txt

COPY . /restaurant_api
WORKDIR /restaurant_api

EXPOSE 8000

ENTRYPOINT [ "python", "/app/restaurant_api/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

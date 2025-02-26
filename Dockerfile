FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn","app.server:app","--host","0.0.0.0", "--port","8000"]

#docker build -t flower_image_name . 
#docker rm flower_container
#docker run --name flower_container -p 8000:8000 flower_image_name

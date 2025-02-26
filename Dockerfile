
# Use an official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the ports for Flask and Streamlit
EXPOSE 8000 8501

# Start both Flask and Streamlit using a shell script
CMD ["sh", "-c", "python app.py & streamlit run client.py --server.port=8501 --server.address=0.0.0.0"]




#✅ FastAPI runs on port 8000
#✅ Streamlit runs on port 8501
#✅ Both run in separate containers
#✅ Automatically restarts on failure


# FROM python:3.11

# WORKDIR /code

# COPY ./requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

# COPY ./app /code/app


# EXPOSE 8501

#CMD ["uvicorn","app.server:app","--host","0.0.0.0", "--port","8000"]
#ENTRYPOINT ["streamlit", "run", "app/server.py", "--server.port=8501", "--server.address=0.0.0.0"]

#docker build -t flower_image_name . 
#docker rm flower_container
#docker run --name flower_container -p 8501:8501 flower_image_name

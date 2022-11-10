FROM python:3.7-alpine
WORKDIR /app
run apk add --no-cache gcc musl-dev linux-headers 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 7863
COPY . .
CMD ["python3", "service.py"]
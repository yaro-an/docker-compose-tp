FROM python:3-alpine3.23

WORKDIR /app
RUN apk add --no-cache curl

RUN pip install mysql-connector-python fastapi uvicorn pymongo

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
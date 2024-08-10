# syntax=docker/dockerfile:1

FROM alpine:latest
EXPOSE 8000
WORKDIR /app
COPY ./src ./src
RUN apk add --no-cache python3 py3-pip
RUN pip3 install -r ./src/requirements.txt --break-system-packages
ENV PYTHONPATH="${PYTHONPATH}:./src"

# Use uvicorn to re-directing default fastapi 127.0.0.1 to 0.0.0.0
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

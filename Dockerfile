FROM alpine:latest
WORKDIR /app
RUN apk add --no-cache python3 py3-pip py3-pandas py3-requests py3-openpyxl
COPY read_excel.py /app/read_excel.py
ENTRYPOINT ["python3", "/app/read_excel.py"]

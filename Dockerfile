# Alap image használata (Python 3.9)
FROM python:3.9-slim

# Munkakönyvtár beállítása
WORKDIR /app

# Függőségek telepítése
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
RUN pip install pandas openpyxl requests

# A szkript másolása a konténerbe
COPY read_excel.py /app/read_excel.py

# Futtatás a konténer indításakor
ENTRYPOINT ["python", "read_excel.py"]

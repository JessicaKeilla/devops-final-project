# BUILD STAGE
FROM python:3.11 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# RUNTIME STAGE
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]
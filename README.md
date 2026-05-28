# devops-final-project
## 📌 Описание проекта

Данный проект представляет собой простое веб-приложение на Flask, полностью контейнеризированное с использованием Docker Compose.

Проект включает:

- Flask web application
- Docker Compose orchestration
- Multistage Docker build
- Централизованное логирование через Loki
- Просмотр логов через Grafana
- Bash script для автоматической сборки и запуска контейнеров

---

# 🧱 Используемые технологии

- Python 3.11
- Flask
- Docker
- Docker Compose
- Grafana Loki
- Grafana
- Bash scripting
- GitHub Codespaces

---

# 🚀 Функциональность приложения

Приложение запускает простой Flask веб-сервер.

При обращении к главной странице:
- отображается сообщение:
  
```text
DevOps Final Project Running 🚀
```

- создается log entry:
  
```text
Home accessed
```

Логи контейнера собираются Loki и отображаются в Grafana.

---


# 🐳 Multistage Docker Build

В проекте используется multistage Docker build.

### Build stage
Устанавливаются Python зависимости.

### Runtime stage
Создается минимальный production image.

---


# ▶️ Запуск проекта

## 1. Дать права на выполнение скрипта

```bash
chmod +x scripts.sh
```

---

## 2. Запустить проект

```bash
./scripts.sh -t v1
```

---

# 🔍 Проверка контейнеров

```bash
docker ps
```

---

# 🌐 Доступ к сервисам

| Service | URL |
|---|---|
| Flask App | http://localhost:5000 |
| Grafana | http://localhost:3000 |
| Loki | http://localhost:3100 |

---

# 📩 Просмотр логов через Grafana

## Логин в Grafana

```text
login: admin
password: admin
```

---

## Настройка Loki datasource

### URL:

```text
http://loki:3100
```

После подключения Grafana может отображать логи контейнеров.

---

# 🖼 Screenshots


---

## 📌 Docker Containers Running

<img width="1754" height="252" alt="image" src="https://github.com/user-attachments/assets/0c4be639-f8b2-42db-93cd-5badd9434403" />

<img width="1732" height="344" alt="image" src="https://github.com/user-attachments/assets/c1076d1d-9d57-4df2-90ea-ff24af1bfc74" />

---

## 📌 Docker Images

<img width="1775" height="227" alt="image" src="https://github.com/user-attachments/assets/7f972ad3-abf5-48dc-8fa9-5e64b69dc974" />

---

## 📌 Flask Application Running

<img width="1202" height="295" alt="image" src="https://github.com/user-attachments/assets/d4c812c7-3e7d-4bbf-aa4d-34aad97ff7ac" />
<img width="1750" height="553" alt="image" src="https://github.com/user-attachments/assets/47b2db57-6e99-44ba-96e7-2babdcd2b2e8" />


---

## 📌 Grafana Login

<img width="2093" height="1129" alt="image" src="https://github.com/user-attachments/assets/17d33664-3a04-46d6-a1b4-cd6a9bb9337c" />

---

## 📌 Loki Data Source Connected

<img width="1881" height="608" alt="image" src="https://github.com/user-attachments/assets/493990fa-1d96-4193-9d9c-7f43461795fd" />

<img width="1721" height="451" alt="image" src="https://github.com/user-attachments/assets/807c03eb-3aaa-4210-a7a4-cf81726e9de0" />


---



# 🧠 Bash Script

В проекте используется bash script с параметром:

```bash
-t
```

Пример:

```bash
./scripts.sh -t v1
```

Параметр задает tag сборки контейнеров.

---

# 🔐 Централизованное логирование

Для централизованного хранения логов используется Loki.

Grafana подключается к Loki как datasource и позволяет:
- просматривать container logs
- фильтровать logs
- анализировать события приложения

---

# ✅ Результат

В результате работы были реализованы:

- контейнеризация приложения
- multistage build
- orchestration через Docker Compose
- centralized logging
- Grafana logs visualization
- автоматизация через bash script

---

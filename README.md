# docker-telegram-bot-sample

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen)
![Purpose](https://img.shields.io/badge/purpose-educational-blueviolet)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Educational / demo** repository to practice **containerization with Docker** around a tiny Telegram bot (Latinization utility). This is **not production** — just a clean, minimal example.

### What this repo demonstrates
- `Dockerfile` baseline (slim image, no-cache install, non-root user)
- `docker-compose.yml` with env-based config (`.env`)
- Logs to **stdout** (no file logs in repo)
- Clean `.gitignore` for Python & logs

---

## Quickstart

### Local
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # put your token here
python LatinizatorBot.py


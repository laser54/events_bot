# EventBot

Бот платформы для организации мероприятий
https://t.me/event_sgu_bot

## Prerequisites

- Python 3.7 or higher
- Docker (optional, for deployment)
- Aiogram 3.3.0

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/laser54/events_bot.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables by creating a `.env` file and adding your Telegram bot token:

    ```plaintext
    TELEGRAM_BOT_TOKEN=your-telegram-bot-token
    ```

4. Run the bot:

    ```bash
    python main.py
    ```

## Features

soon

## Deployment

This repository includes a GitHub Actions workflow (`deploy.yml`) that automates the deployment process to a VPS. The workflow builds a Docker image and deploys it to your server using SSH.

To deploy the bot to your VPS, follow these steps:

1. Add your DockerHub credentials and SSH details as secrets in your GitHub repository settings.

2. Push your changes to the `main` branch.

3. GitHub Actions will automatically build and deploy your bot to the specified VPS.


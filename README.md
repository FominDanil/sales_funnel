# Title



## Requirements
- Python 3.10
- Docker
- Telegram bot api token

## Installation

First, you need to clone this repository:

```bash
git clone https://github.com/FominDanil/sales_funnel.git
cd sales_funnel
```

## Configuration
### .env
The application uses environment variables for configuration. Rename `.env.example` to `.env` and fill in the necessary details:

```bash
cp .env.example .env
nano .env
```

- BOT_TOKEN: get it from @BotFather


## Usage

Once you have your environment variables set up, you can start the application using Docker Compose:

```bash
docker build -t sales_funnel .
docker run sales_funnel
```

The application will now run in the background, managing the queue and sending messages in your Telegram channel according to the settings defined in the configuration.


from telegram.ext import Application

from bot.core.settings import settings


def main() -> None:
    """Initialize a Telegram bot application."""
    application = Application.builder().token(settings.telegram_token).build()
    application.run_polling()


if __name__ == "__main__":
    main()

# main.wsgi

import os
from your_application.main import create_bot

application = create_bot()

if __name__ == "__main__":
    # This block is executed if the script is run directly (not imported)
    # It's useful for local development
    from aiogram import executor
    executor.start_polling(application)

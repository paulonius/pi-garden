import os
from dotenv import load_dotenv

from api import create_app

load_dotenv()
config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()

from basicapi.config import Config
from basicapi.app import create_app

app = create_app(Config())

if __name__ == '__main__':
    app.run()

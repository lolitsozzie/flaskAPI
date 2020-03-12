from flask_migrate import MigrateCommand
from flask_script import Manager

from basicapi.app import create_app
from basicapi.config import Config

app = create_app(config=Config())

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

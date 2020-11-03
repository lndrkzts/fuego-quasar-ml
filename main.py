from app import create_app
from config import config


enviroment = config['prod']

app = create_app(enviroment)

if __name__ == '__main__':
    app.run()

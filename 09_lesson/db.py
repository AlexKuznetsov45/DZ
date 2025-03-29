from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Данные для подключения к базе данных
USERNAME = "postgres"
PASSWORD = "2539"
HOST = "localhost"
PORT = "5432"
DATABASE = "postgres"

# Создаем движок для подключения к базе данных
engine = create_engine(
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)


def get_session():
    return Session()

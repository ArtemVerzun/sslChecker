from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание базы данных
engine = create_engine('sqlite:///ssl_info.db', echo=False)
Base = declarative_base()


class SSLInfo(Base):
    __tablename__ = 'ssl_info'
    id = Column(Integer, primary_key=True)
    host = Column(String)
    port = Column(Integer)
    ssl_versions = Column(String)
    domains = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Функция для добавления данных в таблицу
def add_ssl(host, port, ssl_version, domains):
    try:
        existing_row = session.query(SSLInfo).filter((SSLInfo.host == host) &
                                                     (SSLInfo.port == port) &
                                                     (SSLInfo.ssl_versions == ssl_version) &
                                                     (SSLInfo.domains == domains)).scalar()

        if existing_row is not None:
            print(f'данная запись c хоста: {host} уже создана')
        else:
            ssl_info = SSLInfo(host=host, port=port, ssl_versions=ssl_version, domains=domains)
            session.add(ssl_info)

            session.commit()
            print(f'запись: {host, port, ssl_version, domains} успешно добавлена')
    except:
        session.rollback()
        print('rolled back')
        raise
    finally:
        session.close()
from sqlalchemy.orm import sessionmaker

from models import create_tables, db_connect


class Controller:

    def __init__(self):
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, instance):
        session = self.Session()

        try:
            session.add(instance)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return instance
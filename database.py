# importing essential stuffs

from google.cloud.sql.connector import Connector
import sqlalchemy

# init


class LLMdb:
    def __init__(self):
        self.conn = self.get_connect()
        self.engine = self.get_engine()

    def get_connect(self):
        return Connector().connect(
            "rich-agency-372104:asia-southeast2:testdb",
            "pg8000",
            user="postgres",
            password="testdb321",
            db="postgres",
        )

    def get_engine(self):
        return sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=self.conn,
        )

    def store_memory(self, data):
        data.to_sql("memory", self.engine, if_exists="append", index=False)

    def get_memory(self):
        return pd.read_sql("SELECT * FROM memory", self.engine)

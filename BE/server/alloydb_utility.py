import psycopg2
import json
import os
from google.cloud import secretmanager


class AlloyDB:
    def __init__(self):

        self.user = self.get_secret_data(
            os.environ["project-id"], os.environ["user-secret"], os.environ["version"]
        )
        self.password = self.get_secret_data(
            os.environ["project-id"], os.environ["pass-secret"], os.environ["version"]
        )
        self.host = self.get_secret_data(
            os.environ["project-id"], os.environ["database-host"], os.environ["version"]
        )
        self.database_nm = self.get_secret_data(
            os.environ["project-id"], os.environ["database-nm"], os.environ["version"]
        )
        self.port = "5432"
        self.cursor = self._connection()

    def get_secret_data(self, project_id, secret_id, version_id):

        client = secretmanager.SecretManagerServiceClient()
        secret_detail = (
            f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
        )
        response = client.access_secret_version(request={"name": secret_detail})
        data = response.payload.data.decode("UTF-8")
        return data

    def _connection(self):

        try:
            conn = psycopg2.connect(
                database=self.database_nm,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            cursor = conn.cursor()
            print(f"Connection Established with {self.host}")
            return cursor
        except Exception as e:
            print(e)
            print(f"Exception {e} occured while connecting to {self.host}")

    def select_query(self, query):

        self.cursor.execute(query)
        result_data = self.cursor.fetchall()
        return result_data
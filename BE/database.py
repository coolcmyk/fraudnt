# importing essential stuffs

from google.cloud.sql.connector import Connector
import sqlalchemy

# init


class LLMdb:
    def __init__(self):
        self.connector = Connector()
        self.engine = self.get_pool()

    def get_connect(self):
        conn = self.connector.connect(
            "rich-agency-372104:asia-southeast2:testdb",
            "pg8000",
            user="postgres",
            password="testdb321",
            db="postgres",
        )
        return conn

    def get_pool(self):
        pool = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator = self.get_connect,
        )
        self.pool = pool

    def function_test(self):
        # connect to connection pool
        with self.pool.connect() as db_conn:
            # create ratings table in our sandwiches database
            db_conn.execute(
                sqlalchemy.text(
                "CREATE TABLE IF NOT EXISTS ratings "
                "( id SERIAL NOT NULL, name VARCHAR(255) NOT NULL, "
                "origin VARCHAR(255) NOT NULL, rating FLOAT NOT NULL, "
                "PRIMARY KEY (id));"
                ) 
            )

            # commit transaction (SQLAlchemy v2.X.X is commit as you go)
            db_conn.commit()

            # insert data into our ratings table
            insert_stmt = sqlalchemy.text(
                "INSERT INTO ratings (name, origin, rating) VALUES (:name, :origin, :rating)",
            )

            # insert entries into table
            db_conn.execute(insert_stmt, parameters={"name": "HOTDOG", "origin": "Germany", "rating": 7.5})
            db_conn.execute(insert_stmt, parameters={"name": "BÀNH MÌ", "origin": "Vietnam", "rating": 9.1})
            db_conn.execute(insert_stmt, parameters={"name": "CROQUE MADAME", "origin": "France", "rating": 8.3})

            # commit transactions
            db_conn.commit()

            # query and fetch ratings table
            results = db_conn.execute(sqlalchemy.text("SELECT * FROM ratings")).fetchall()

            # show results
            for row in results:
                print(row)


    def store_mem(self, data):
        with self.pool.connect() as conn:
        #     data.to_sql('memory', conn, if_exists='append', index=False)

            conn.execute(
                sqlalchemy.text(
                # "CREATE TABLE IF NOT EXISTS memory (user_input TEXT, response TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"   
                # "INSERT INTO memory (user_input, response) VALUES (?, ?)",
                # data['user_input'],
                # data['response'],
                 """
                CREATE TABLE IF NOT EXISTS memory (
                    id SERIAL PRIMARY KEY,
                    user_input TEXT,
                    response TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                )
            )
            conn.commit()
            insert_query = sqlalchemy.text(
                "INSERT INTO memory (user_input, response) VALUES (:user_input, :response)"
            )
            conn.execute(insert_query, data)  # Pass data dictionary directly
            conn.commit()


            # conn.execute(insert_query, data.to_dict(orient='records'))
            # conn.commit()
            results = conn.execute(
                sqlalchemy.text(
                    "SELECT * FROM memory"
                )
                ).fetchall()
            for rows in results:
                print(rows)


    # def store_mem(self, data):
    #     with self.engine.connect() as conn:
    #         insert_query = sqlalchemy.text(
    #             "INSERT INTO memory (user_input, response) VALUES (:user_input, :response)"
    #         )
    #         conn.execute(insert_query, data.to_dict(orient='records'))
    #         conn.commit()

    def get_hist(self, limit=10):
        query = f"""
        SELECT user_input, response, timestamp
        FROM memory
        ORDER BY timestamp DESC
        LIMIT {limit}
        """
        df = pd.read_sql_query(query, self.engine)
        return df.to_dict('records')

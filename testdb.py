# import os
# import ssl
# import sqlalchemy

# def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
#     """Initializes a TCP connection pool for a Cloud SQL instance of Postgres."""
#     # Note: Saving credentials in environment variables is convenient, but not
#     # secure - consider a more secure solution such as
#     # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
#     # keep secrets safe.
#     db_host = os.environ.get("INSTANCE_HOST", "34.50.76.180")
#     db_user = os.environ.get("DB_USER", "postgres")
#     db_pass = os.environ.get("DB_PASS", "testdb321")
#     db_name = os.environ.get("DB_NAME", "testdb")
#     db_port = os.environ.get("DB_PORT", "5432")

#     pool = sqlalchemy.create_engine(
#         # Equivalent URL:
#         # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
#         sqlalchemy.engine.url.URL.create(
#             drivername="postgresql+pg8000",
#             username=db_user,
#             password=db_pass,
#             host=db_host,
#             port=db_port,
#             database=db_name,
#         ),
#         # Pool size is the maximum number of permanent connections to keep.
#         pool_size=5,
#         # Temporarily exceeds the set pool_size if no connections are available.
#         max_overflow=2,
#         # The total number of concurrent connections for your application will be
#         # a total of pool_size and max_overflow.
#         # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
#         # new connection from the pool. After the specified amount of time, an
#         # exception will be thrown.
#         pool_timeout=30,  # 30 seconds
#         # 'pool_recycle' is the maximum number of seconds a connection can persist.
#         # Connections that live longer than the specified amount of time will be
#         # reestablished
#         pool_recycle=1800,  # 30 minutes
#     )
#     return pool

# # Function to insert a name
# def insert_name(name: str):
#     pool = connect_tcp_socket()
#     print(pool)
#     with pool.connect() as conn:
#         conn.execute(sqlalchemy.text("INSERT INTO names (name) VALUES (:name)"), {"name": name})
#         conn.commit()

# # # Function to get names
# # def get_names():
# #     pool = connect_tcp_socket()
# #     with pool.connect() as conn:
# #         result = conn.execute(sqlalchemy.text("SELECT name FROM names"))
# #         names = [row[0] for row in result]
# #     print(names)
# #     return names

# # Main execution
# if __name__ == "__main__":
#     insert_name("John")
#     # get_names()

# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import socket
import psycopg2 

print(socket.create_connection(("34.50.76.180", 5432)))

#check if the connection is successful

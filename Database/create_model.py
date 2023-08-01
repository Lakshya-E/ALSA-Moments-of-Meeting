"""Creating models for database"""
from pgvector.psycopg2 import register_vector
from connect_database import connections

conn = connections()
cur = conn.cursor()

cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
conn.commit()

register_vector(conn)

table_create_command = """
CREATE TABLE embeddings (
            id bigserial primary key,
            embedding vector(1536)
            );
            """

cur.execute(table_create_command)
cur.close()
conn.commit()


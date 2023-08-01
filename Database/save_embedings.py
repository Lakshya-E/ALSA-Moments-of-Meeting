"""This function saves embeddings to pgvector"""
import pandas as pd
import numpy as np
import math
import openai
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector
from connect_database import connections
from psycopg2.extras import execute_values

load_dotenv()

conn = connections()
register_vector(conn)
cur = conn.cursor()

new_list = []


def indexing_list(num_records):
    """Index your data for faster retrieval
    calculate the index parameters according to best practices"""
    num_lists = num_records / 1000
    if num_lists < 10:
        num_lists = 10
    if num_records > 1000000:
        num_lists = math.sqrt(num_records)

    # use the cosine distance measure, which is what we'll later use for querying
    cur.execute(f'CREATE INDEX ON embeddings USING ivfflat (embedding vector_cosine_ops) WITH (lists = {num_lists});')
    conn.commit()


def get_embeddings(text):
    """This function creates embeddings from text"""
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text.replace("\n", " ")
    )
    embedding_func = response['data'][0]['embedding']

    return embedding_func


def save_embeds(text):
    """This function saves embeddings to database"""
    embedding = get_embeddings(text)
    new_list.append(embedding)

    df_new = pd.DataFrame(new_list, columns=['embeddings'])
    df_new.head()
    df_new.to_csv('tabular.csv', index=False)


    # after stop
    data_list = [(np.array(row['embeddings'])) for index, row in df_new.iterrows()]
    execute_values(cur, "INSERT INTO embeddings (embedding) VALUES %s", data_list)
    conn.commit()

    cur.execute("SELECT COUNT(*) as cnt FROM embeddings;")
    num_records = cur.fetchone()[0]
    print("Number of vector records in table: ", num_records, "\n")

    indexing_list(num_records)

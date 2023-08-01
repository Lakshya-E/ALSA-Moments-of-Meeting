"""Connection setup to postgresql db"""
import os
import psycopg2


def connections():
    connection_string = os.environ['TIMESCALE_CONNECTION_STRING']
    conn = psycopg2.connect(connection_string)

    return conn

import os, sys, psycopg2

DB_NAME = os.getenv('TAIGA_DB_NAME')
DB_HOST = os.getenv('TAIGA_DB_HOST')
DB_USER = os.getenv('TAIGA_DB_USER')
DB_PASS = os.getenv('TAIGA_DB_PASSWORD')

if os.getenv('TAIGA_BACKEND_DEBUG') is True:
    print "dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PASS + "'"

conn = psycopg2.connect("dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PASS + "'")

cur = conn.cursor()

cur.execute("select * from information_schema.tables where table_name=%s", ('django_migrations',))
exists = bool(cur.rowcount)

if exists is False:
    print('Database does not appear to be setup.')
    sys.exit(2)

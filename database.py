import os

import sqlalchemy
from sqlalchemy import create_engine, text
import pymysql
db_str = os.environ['SECRET_DB']
engine = create_engine(db_str,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       }
                       )
def load_db(search):
    with engine.connect() as conn:
        result = conn.execute(text("select * from telethon where bagz = '%s'" % search))
        columns = [column[0] for column in result.cursor.description]
        ret = []
        for row in result.fetchall():
            ret.append(dict(zip(columns, row)))
    return ret



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
    search = "%" + search + "%"
    with engine.connect() as conn:
        # result = conn.execute(text("select * from telethon where bagz = '%s'" % search))
        result = conn.execute(text("select distinct t1.bagz, t2.provider, t2.province, t2.muni, t2.name, t1.id from telethon t1 join subburbs t2 on t1.aid = t2.aid where t1.bagz = t2.bagz AND t2.name like '%s' ORDER BY t2.province ASC" % search))
        columns = [column[0] for column in result.cursor.description]
        ret = []
        for row in result.fetchall():
            ret.append(dict(zip(columns, row)))
    return ret



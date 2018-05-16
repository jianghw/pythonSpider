import sqlite3
import time


class SqliteClient(object):
    def __init__(self):
        pass

    def all_proxy_name(self):
        return 'ip_all_proxy'


if __name__ == '__main__':
    sc = SqliteClient()
    table_name = sc.all_proxy_name()

    conn = sqlite3.connect('sq_proxy_ip.db')
    cursor_db = conn.cursor()

    sql_cre = "create table if not exists {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT," \
              "ip_host VARCHAR NOT NULL,ip_port VARCHAR,https INTEGER(2)," \
              "create_time INTEGER,update_time INTEGER)".format(table_name=table_name)
    cursor_db.execute(sql_cre)

    try:
        for host, port, http in zip(
                ['119.251.32.135', '110.39.185.58', '103.108.47.17'], ['9000', '8080', '8080'],
                [True, False, True]):

            if http:
                https = 1
            else:
                https = 0

            sql_ins = "INSERT INTO {table_name}(ip_host,ip_port,https,create_time)" \
                      "VALUES({ip_host},{ip_port},{https},{create_time})" \
                .format(table_name=table_name, ip_host='119.251.32.135', ip_port=str(port), https=https,
                        create_time=time.time())
            print(sql_ins)
            cursor_db.execute(sql_ins)
    except Exception as error:
        sql_dro = 'DROP TABLE {table_name}'.format(table_name=table_name)
        cursor_db.execute(sql_dro)
        print('db_error %s' % error)

    cursor_db.close()
    conn.commit()
    conn.close()
    pass

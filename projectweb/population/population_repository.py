class SurnameRepository:

    def __init__(self):
        self.connection_info = { 'host': 'localhost', 'db': 'projectwebdb', 'user': 'root', 'password': 'myb5370', 'charset': 'utf8' }

    def select_surname_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select distinct(name), sur from surname2015 where concat(sur, ' ', name) like %s"
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["name", "sur"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def select_detail_surname_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        if len(name_key) == 5:
            sql = "select name, sur, region, total from surname2015 where concat(sur, ' ', name) like %s and sur = '';"
            cursor.execute(sql, ("%" + name_key + "%",))
        else:
            sql = "select name, sur, region, total from surname2015 where concat(sur, ' ', name) like %s"
            cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["name", "sur", "region", "total"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result
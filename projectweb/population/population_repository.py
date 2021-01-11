class PopulationRepository:

    def __init__(self):
        self.connection_info = { 'host': 'localhost', 'db': 'projectwebdb', 'user': 'root', 'password': 'myb5370', 'charset': 'utf8' }

    def select_pop_past_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select * from population_past where region like %s"
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["region"
              , "total2015", "man2015", "woman2015"
              , "total2016", "man2016", "woman2016"
              , "total2017", "man2017", "woman2017"
              , "total2018", "man2018", "woman2018"
              , "total2019", "man2019", "woman2019"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def select_pop_future_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select * from population_future where year > %s order by year asc"
        cursor.execute(sql, (name_key))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["year", "total", "man", "woman", "total0_14", "total15_64", "total64_"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def select_age_gender_by_region(self, region_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select * from age_gender where region like %s"
        cursor.execute(sql, ("%" + region_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["region", "age", "man", "woman"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result
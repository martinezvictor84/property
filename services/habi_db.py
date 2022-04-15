from mysql.connector import connect
import os


class Connection:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        print('port: ', self.port)
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.database = os.getenv('DB_NAME')

    def query(self, query, params=None):
        try:
            conn = None
            conn = connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = conn.cursor(dictionary=True)

            cursor.execute(query, params)

            return cursor.fetchall()
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


class HabiDb(Connection):

    def __init__(self, **kwargs):
        super(HabiDb, self).__init__(**kwargs)

    def get_properties(self, filters=None, page=1, per_page=50):
        offset = (0 if page < 0 else page - 1) * per_page
        query = "select p.* from property p "
        sub_query = (
            "select bsh.* from ("
            "select max(id) as id from status_history "
            "group by property_id "
            ") as m "
            "inner join status_history bsh "
            "on m.id = bsh.id "
            "and status_id in (3, 4, 5)"
        )
        query += f"inner join ({sub_query}) sh on p.id = sh.property_id "
        if filters:
            query += "where "
            first = True
            for key, value in filters.items():
                if not first:
                    query += f"and {value['column']} {value['condition']} %({key})s "
                else:
                    first = False
                    query += f"{value['column']} {value['condition']} %({key})s "
        query += f'limit {per_page} offset {offset}'
        print(query)
        params = {key: value['value'] for key, value in filters.items()}
        return self.query(query, params)
    pass


class DatabaseError(Exception):
    pass

from mysql.connector import connect
import os


class Connection:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.database = os.getenv('DB_NAME')

    def query(self, query, params=None):
        try:
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
            if conn.is_connected():
                cursor.close()
                conn.close()


class HabiDb(Connection):

    def __init__(self, **kwargs):
        super(HabiDb, self).__init__(**kwargs)

    def get_properties(self, filters=None):
        query = "select p.* from property p "
        if 'status_id' in filters:
            sub_query = (
                "select bsh.* from ("
                    "select max(id) as id from status_history "
                    "group by property_id "
                ") as m "
                "inner join status_history bsh on m.id = bsh.id and status_id = %(status_id)s "
            )
            query += f"inner join ({sub_query}) sh on p.id = sh.property_id "
        if filters:
            query += "where "
            first = True
            for key in filters:
                if not first:
                    query += f"and {key} = %({key})s "
                else:
                    first = False
                    query += f"{key} = %({key})s "
        return self.query(query, filters)
    pass


class DatabaseError(Exception):
    pass

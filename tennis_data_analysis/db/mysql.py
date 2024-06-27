import mysql.connector


class Database:

    def __init__(self, host, user, password, dbname, port) -> None:
        try:
            self.__conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbname,
                port=port
            )
            self.db = self.__conn.cursor()
        except Exception as error:
            print("Database connection error")
            print(error)
            exit()

    def conn(self) -> mysql.connector.connection_cext.CMySQLConnection:
        return self.__conn

    def commit(self) -> None:
        self.__conn.commit()

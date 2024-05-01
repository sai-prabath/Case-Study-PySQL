import mysql.connector

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Prabath.sql@0000",
                port="3306",
                database="TBS"
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            return None

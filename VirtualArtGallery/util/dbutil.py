import mysql.connector
from mysql.connector import Error

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        try:
            if DBConnection.connection is None or not DBConnection.connection.is_connected():
                connection_string = PropertyUtil.getPropertyString("/Users/saiprabathchowdary/Documents/hexaware/segue foundation -python/Assignment/Case-Study-PySQL/VirtualArtGallery/util/DBdata.txt")
                DBConnection.connection = mysql.connector.connect(**connection_string)
            return DBConnection.connection
        except Error as e:
            print("Error:", e)
            return None


class PropertyUtil:
    @staticmethod
    def getPropertyString(property_file):
        properties = {}
        with open(property_file,'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                properties[key] = value
        return properties

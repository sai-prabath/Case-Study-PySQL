from VirtualArtGallery.dao.IVirtualArtGallery import IVirtualArtGallery
from VirtualArtGallery.util.dbutil import DBConnection
from VirtualArtGallery.exception.myexceptions import ArtWorkNotFoundException

import mysql.connector

class IVirtualArtGalleryImpl(IVirtualArtGallery):

    def __init__(self):
        self.connection = DBConnection.getConnection()

    def createUser(self,user):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO User (userID, username, password, email, FirstName, LastName, DateOfBirth, ProfilePicture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (user.getUserID(), user.getUsername(), user.getPassword(), user.getEmail(), user.getFirstName(), user.getLastName(), user.getBirthDate(), user.getProfilePicture())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error adding user:", err)
            return False

    def getAllArtworks(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork"
            cursor.execute(query)
            artworks = []
            for row in cursor.fetchall():
                #artwork = Artwork(row[0], row[1], row[2], row[3], row[4], row[5])
                artworks.append(row)
            cursor.close()
            return artworks
        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    def addArtwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artwork (title, description, creationDate, medium, imageURL, ArtistID) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (artwork.getTitle(), artwork.getDescription(), artwork.getCreationDate(), artwork.getMedium(), artwork.getImageURL(), artwork.getArtistID())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def updateArtwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Artwork SET title=%s, description=%s, creationDate=%s, medium=%s, imageURL=%s, ArtistID=%s WHERE artworkID=%s"
            values = (artwork.getTitle(), artwork.getDescription(), artwork.getCreationDate(), artwork.getMedium(), artwork.getImageURL(), artwork.getArtistID(), artwork.getArtworkID())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def removeArtwork(self, artworkID):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Artwork WHERE artworkID=%s"
            cursor.execute(query, (artworkID,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def getArtworkById(self, artworkID):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE artworkID=%s"
            cursor.execute(query, (artworkID,))
            result = cursor.fetchone()
            if result:
                #artwork = Artwork(result[0], result[1], result[2], result[3], result[4], result[5])
                return result
            else:
                raise ArtWorkNotFoundException()
        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    def searchArtworks(self, keyword):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE title LIKE %s OR description LIKE %s"
            cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
            results = cursor.fetchall()
            artworks = []
            for result in results:
                #artwork = Artwork(result[0], result[1], result[2], result[3], result[4], result[5])
                artworks.append(result)
            return artworks
        except mysql.connector.Error as err:
            print("Error:", err)
            return []

    def addArtworkToFavorite(self, userId, artworkId):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO User_Favorite_Artwork (userID, artworkID) VALUES (%s, %s)"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def removeArtworkFromFavorite(self, userId, artworkId):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM User_Favorite_Artwork WHERE userID=%s AND artworkID=%s"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def getUserFavoriteArtworks(self, userId):
        try:
            cursor = self.connection.cursor()
            query = "SELECT artworkID FROM User_Favorite_Artwork WHERE userID=%s"
            cursor.execute(query, (userId,))
            results = cursor.fetchall()
            favoriteArtworks = []
            for result in results:
                favoriteArtworks.append(result[0])
            return favoriteArtworks
        except mysql.connector.Error as err:
            print("Error:", err)
            return []

    def displayGalleries(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM gallery"
            cursor.execute(query)
            galleries = []
            for row in cursor.fetchall():
                galleries.append(row)
            cursor.close()
            return galleries
        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    def addArtist(self,artist):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artist (name, biography, birthDate, nationality, website, contactInfo) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (artist.getName(), artist.getBiography(), artist.getBirthDate(), artist.getNationality(),
                      artist.getWebsite(), artist.getContactInfo())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def addGallery(self, gallery):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Gallery (name, description, location, openingHours, curator) VALUES (%s, %s, %s, %s, %s)"
            values = (gallery.getName(), gallery.getDescription(), gallery.getLocation(), gallery.getOpeningHours(),
                      gallery.getCurator())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def updateGallery(self, gallery):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Gallery SET name = %s, description = %s, location = %s, openingHours = %s, curator = %s WHERE galleryID = %s"
            values = (gallery.getName(), gallery.getDescription(), gallery.getLocation(), gallery.getOpeningHours(),
                      gallery.getCurator(), gallery.getGalleryID())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def removeGallery(self, gallery_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Gallery WHERE galleryID = %s"
            cursor.execute(query, (gallery_id,))
            self.connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def searchGalleries(self, keyword):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Gallery WHERE name LIKE %s OR description LIKE %s"
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
            galleries = cursor.fetchall()
            cursor.close()
            return galleries
        except mysql.connector.Error as err:
            print("Error:", err)
            return None



'''

from dao.IVirtualArtGallery import IVirtualArtGallery
from util.DBConnection import DBConnection
from entity.Artwork import Artwork

class IVirtualArtGalleryImpl(IVirtualArtGallery):
    connection = None

    def __init__(self):
        self.connection = DBConnection.getConnection()

    def addArtwork(self, artwork: Artwork) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Error adding artwork:", e)
            return False

    def updateArtwork(self, artwork: Artwork) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Artwork SET Title = %s, Description = %s, CreationDate = %s, Medium = %s, ImageURL = %s WHERE ArtworkID = %s"
            cursor.execute(query, (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Error updating artwork:", e)
            return False

    def removeArtwork(self, artworkID: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(query, (artworkID,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Error removing artwork:", e)
            return False

    def getArtworkById(self, artworkID: int) -> Artwork:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(query, (artworkID,))
            artwork_data = cursor.fetchone()
            cursor.close()
            if artwork_data:
                artwork = Artwork(*artwork_data)
                return artwork
            else:
                return None
        except Exception as e:
            print("Error getting artwork by ID:", e)
            return None

    def searchArtworks(self, keyword: str) -> list[Artwork]:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE Title LIKE %s OR Description LIKE %s"
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
            artworks_data = cursor.fetchall()
            cursor.close()
            artworks = []
            for artwork_data in artworks_data:
                artwork = Artwork(*artwork_data)
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print("Error searching artworks:", e)
            return []
'''

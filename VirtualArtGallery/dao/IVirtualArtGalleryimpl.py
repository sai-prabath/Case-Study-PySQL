from VirtualArtGallery.dao.IVirtualArtGallery import IVirtualArtGallery
from VirtualArtGallery.util.dbutil import DBConnection
from VirtualArtGallery.exception.myexceptions import ArtWorkNotFoundException
from VirtualArtGallery.entity.artwork import Artwork
from VirtualArtGallery.entity.gallery import Gallery

import mysql.connector

class IVirtualArtGalleryImpl(IVirtualArtGallery):

    def __init__(self):
        self.connection = DBConnection.getConnection()

    def createUser(self,user):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO User (username, password, email, FirstName, LastName, DateOfBirth, ProfilePicture) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (user.getUsername(), user.getPassword(), user.getEmail(), user.getFirstName(), user.getLastName(), user.getBirthDate(), user.getProfilePicture())
            cursor.execute(query, values)
            self.connection.commit()

            query = "SELECT max(userID) FROM User"
            cursor.execute(query)
            uid = cursor.fetchone()
            self.connection.commit()

            cursor.close()
            return [True, uid]

        except mysql.connector.Error as err:
            print("Error adding user:", err)
            return False

    def getAllArtworks(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork"
            cursor.execute(query)
            artwork_data = cursor.fetchall()
            cursor.close()
            artworks = [Artwork(*data) for data in artwork_data]
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
                artwork = Artwork(*result)
                return artwork

        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    def searchArtworks(self, keyword):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE title LIKE %s OR description LIKE %s"
            cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
            artwork_data = cursor.fetchall()
            cursor.close()
            artworks = [Artwork(*data) for data in artwork_data]
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
            query = "SELECT uf.artworkID, title, description, creationDate, medium, imageURL, artistID FROM User_Favorite_Artwork uf join artwork aw on uf.artworkID=aw.artworkID WHERE userID=%s"
            cursor.execute(query, (userId,))
            artwork_data = cursor.fetchall()
            cursor.close()
            favoriteArtworks = [Artwork(*data) for data in artwork_data]
            return favoriteArtworks
        except mysql.connector.Error as err:
            print("Error:", err)
            return []

    def displayGalleries(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM gallery"
            cursor.execute(query)
            gallery_data = cursor.fetchall()
            cursor.close()
            galleries = [Gallery(*data) for data in gallery_data]
            return galleries
        except mysql.connector.Error as err:
            print("Error:", err)
            return []

    def addArtist(self,artist):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artist (name, biography, birthDate, nationality, website, ContactInformation) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (artist.getName(), artist.getBiography(), artist.getBirthDate(), artist.getNationality(),
                      artist.getWebsite(), artist.getContactInformation())
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
            gallery_data = cursor.fetchall()
            cursor.close()
            galleries=[Gallery(*data) for data in gallery_data]
            return galleries
        except mysql.connector.Error as err:
            print("Error:", err)
            return []


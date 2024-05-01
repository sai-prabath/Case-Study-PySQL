from abc import ABC, abstractmethod

class IVirtualArtGallery(ABC):

    @abstractmethod
    def createUser(self,user):
        pass

    @abstractmethod
    def getAllArtworks(self):
        pass

    @abstractmethod
    def addArtwork(self, artwork):
        pass

    @abstractmethod
    def updateArtwork(self, artwork):
        pass

    @abstractmethod
    def removeArtwork(self, artworkID):
        pass

    @abstractmethod
    def getArtworkById(self, artworkID):
        pass

    @abstractmethod
    def searchArtworks(self, keyword):
        pass

    @abstractmethod
    def addArtworkToFavorite(self, userID, artworkID):
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self, userID, artworkID):
        pass

    @abstractmethod
    def getUserFavoriteArtworks(self, userID):
        pass

    @abstractmethod
    def displayGalleries(self):
        pass

    @abstractmethod
    def addArtist(self,artist):
        pass

    @abstractmethod
    def addGallery(self, gallery):
        pass

    @abstractmethod
    def updateGallery(self, gallery):
        pass

    @abstractmethod
    def removeGallery(self, gallery_id):
        pass

    @abstractmethod
    def searchGalleries(self, keyword):
        pass
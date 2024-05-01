class Artwork:
    def __init__(self, artworkID, title, description, creationDate, medium, imageURL, ArtistID):
        self.__artworkID = artworkID
        self.__title = title
        self.__description = description
        self.__creationDate = creationDate
        self.__medium = medium
        self.__imageURL = imageURL
        self.__ArtistID = ArtistID

    # Getters
    def getArtworkID(self):
        return self.__artworkID

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getCreationDate(self):
        return self.__creationDate

    def getMedium(self):
        return self.__medium

    def getImageURL(self):
        return self.__imageURL

    def getArtistID(self):
        return self.__ArtistID

    # Setters
    def setTitle(self, title):
        self.__title = title

    def setDescription(self, description):
        self.__description = description

    def setCreationDate(self, creationDate):
        self.__creationDate = creationDate

    def setMedium(self, medium):
        self.__medium = medium

    def setImageURL(self, imageURL):
        self.__imageURL = imageURL

    def setArtistID(self, ArtistID):
        self.__ArtistID = ArtistID





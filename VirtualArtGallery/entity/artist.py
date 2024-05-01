class Artist:
    def __init__(self, artistID, name, biography, birthDate, nationality, website, contactInformation):
        self.__artistID = artistID
        self.__name = name
        self.__biography = biography
        self.__birthDate = birthDate
        self.__nationality = nationality
        self.__website = website
        self.__contactInformation = contactInformation

    # Getters
    def getArtistID(self):
        return self.__artistID

    def getName(self):
        return self.__name

    def getBiography(self):
        return self.__biography

    def getBirthDate(self):
        return self.__birthDate

    def getNationality(self):
        return self.__nationality

    def getWebsite(self):
        return self.__website

    def getContactInformation(self):
        return self.__contactInformation

    # Setters
    def setName(self, name):
        self.__name = name

    def setBiography(self, biography):
        self.__biography = biography

    def setBirthDate(self, birthDate):
        self.__birthDate = birthDate

    def setNationality(self, nationality):
        self.__nationality = nationality

    def setWebsite(self, website):
        self.__website = website

    def setContactInformation(self, contactInformation):
        self.__contactInformation = contactInformation

# Similar implementations for User and Gallery classes...

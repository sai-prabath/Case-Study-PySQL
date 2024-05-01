class Gallery:
    def __init__(self, galleryID, name, description, location, curator, openingHours):
        self.__galleryID = galleryID
        self.__name = name
        self.__description = description
        self.__location = location
        self.__curator = curator
        self.__openingHours = openingHours

    # Getters
    def getGalleryID(self):
        return self.__galleryID

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getLocation(self):
        return self.__location

    def getCurator(self):
        return self.__curator

    def getOpeningHours(self):
        return self.__openingHours

    # Setters
    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description

    def setLocation(self, location):
        self.__location = location

    def setCurator(self, curator):
        self.__curator = curator

    def setOpeningHours(self, openingHours):
        self.__openingHours = openingHours

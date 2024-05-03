class User:
    def __init__(self, userID, username, password, email, firstName, lastName, birthDate, profilePicture):
        self.__userID = userID
        self.__username = username
        self.__password = password
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthDate = birthDate
        self.__profilePicture = profilePicture

    # Getters
    def getUserID(self):
        return self.__userID

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getEmail(self):
        return self.__email

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getBirthDate(self):
        return self.__birthDate

    def getProfilePicture(self):
        return self.__profilePicture

    # Setters
    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setEmail(self, email):
        self.__email = email

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setBirthDate(self, birthDate):
        self.__birthDate = birthDate

    def setProfilePicture(self, profilePicture):
        self.__profilePicture = profilePicture

    def __str__(self):
        return f"User ID: {self.__userID}\nUserName: {self.__username}, email id: {self.__email}\nFirst Name: {self.__firstName}, Last Name: {self.__lastName}\nBirth Date: {self.__birthDate}, Profile Pic: {self.__profilePicture}\n"

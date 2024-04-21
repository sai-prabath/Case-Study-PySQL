-- Artwork table
CREATE TABLE Artwork (
    ArtworkID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255),
    Description TEXT,
    CreationDate DATE,
    Medium VARCHAR(100),
    ImageURL VARCHAR(255),
    ArtistID INT, -- Foreign Key referencing Artist.ArtistID
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

-- Artist table
CREATE TABLE Artist (
    ArtistID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Biography TEXT,
    BirthDate DATE,
    Nationality VARCHAR(100),
    Website VARCHAR(255),
    ContactInformation VARCHAR(255)
);

-- User table
CREATE TABLE User (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50),
    Password VARCHAR(255),
    Email VARCHAR(255),
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DateOfBirth DATE,
    ProfilePicture VARCHAR(255)
);

-- Gallery table
CREATE TABLE Gallery (
    GalleryID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Description TEXT,
    Location VARCHAR(255),
    Curator INT, -- Reference to ArtistID
    OpeningHours VARCHAR(255),
    FOREIGN KEY (Curator) REFERENCES Artist(ArtistID)
);

-- junction table for User - Favorite Artwork relationship
CREATE TABLE User_Favorite_Artwork (
    UserID INT,
    ArtworkID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
    PRIMARY KEY (UserID, ArtworkID)
);

-- junction table for Artwork - Gallery relationship
CREATE TABLE Artwork_Gallery (
    ArtworkID INT,
    GalleryID INT,
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
    FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID),
    PRIMARY KEY (ArtworkID, GalleryID)
);


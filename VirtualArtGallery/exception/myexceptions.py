class ArtWorkNotFoundException(Exception):
    def __init__(self, message="Artwork not found."):
        self.message = message
        super().__init__(self.message)

class UserNotFoundException(Exception):
    def __init__(self, message="User not found."):
        self.message = message
        super().__init__(self.message)

class UserCreationException(Exception):
    def __init__(self, message="Error Creating User"):
        self.message = message
        super().__init__(self.message)

class ArtworkCreationException(Exception):
    def __init__(self, message="Error Creating Artwork"):
        self.message = message
        super().__init__(self.message)

class GalleryCreationException(Exception):
    def __init__(self, message="Error Creating Gallery"):
        self.message = message
        super().__init__(self.message)

class ArtistNotFoundException(Exception):
    def __init__(self, message="Artist not found."):
        self.message = message
        super().__init__(self.message)

class GalleryNotFoundException(Exception):
    def __init__(self, message="Gallery not found."):
        self.message = message
        super().__init__(self.message)



#except ArtWorkNotFoundException as e:
#    print("Artwork not found:", e.message)

#except UserNotFoundException as e:
#    print("User not found:", e.message)

#except Exception as e:
#    print("An error occurred:", str(e))

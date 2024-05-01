from VirtualArtGallery.dao.IVirtualArtGalleryimpl import IVirtualArtGalleryImpl
from VirtualArtGallery.exception.myexceptions import ArtWorkNotFoundException, UserNotFoundException
from VirtualArtGallery.exception.myexceptions import ArtistNotFoundException, GalleryNotFoundException
from VirtualArtGallery.entity.artwork import Artwork
from VirtualArtGallery.entity.user import User
from VirtualArtGallery.entity.gallery import Gallery
from VirtualArtGallery.entity.artist import Artist

class MainModule:
    def __init__(self):
        self.virtual_gallery = IVirtualArtGalleryImpl()

    # artwork
    def create_user(self):
        try:
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            firstName = input("Enter first Name: ")
            lastName = input("Enter last Name: ")
            birthDate = input("Enter : birthDate")
            profilePicture = input("select profilePicture(enter url): ")
            user = User(username, password, email, firstName, lastName, birthDate, profilePicture)
            self.virtual_gallery.createUser(user)
            print("User created successfully!")
            return user.getUserID()
        except Exception as e:
            print(f"Error creating user: {e}")

    def display_artworks(self):
        try:
            artworks = self.virtual_gallery.getAllArtworks()
            if artworks:
                print("Artworks:")
                for artwork in artworks:
                    print(artwork)
                return True
            else:
                print("No artworks found.")
                return False
        except Exception as e:
            print(f"Error displaying Artworks: {e}")

    def add_artwork(self):
        try:
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            creation_date = input("Enter Creation Date: ")
            medium = input("Enter Medium: ")
            image_url = input("Enter Image URL: ")
            artist_id = int(input("Enter Artist ID: "))

            artwork = Artwork(1, title, description, creation_date, medium, image_url, artist_id)

            self.virtual_gallery.addArtwork(artwork)
            print("Artwork added successfully!")
        except Exception as e:
            print(f"Error adding artwork: {e}")

    def update_artwork(self):
        arts = self.display_artworks()
        if not arts:
            return

        try:
            artwork_id = int(input("Enter Artwork ID to update: "))
            title = input("Enter new Title: ")
            description = input("Enter new Description: ")
            creation_date = input("Enter new Creation Date: ")
            medium = input("Enter new Medium: ")
            image_url = input("Enter new Image URL: ")
            artist_id = int(input("Enter Artist ID: "))

            artwork = Artwork(artwork_id, title, description, creation_date, medium, image_url, artist_id)

            self.virtual_gallery.updateArtwork(artwork)
            print("Artwork updated successfully!")
        except ArtWorkNotFoundException as e:
            print(f"Artwork not found: {e}")
        except Exception as e:
            print(f"Error updating artwork: {e}")

    def remove_artwork(self):
        arts = self.display_artworks()
        if not arts:
            return

        try:
            artwork_id = int(input("\nEnter Artwork ID to remove: "))
            self.virtual_gallery.removeArtwork(artwork_id)
            print("Artwork removed successfully!")
        except ArtWorkNotFoundException as e:
            print(f"Artwork not found: {e}")
        except Exception as e:
            print(f"Error removing artwork: {e}")

    def get_artwork_by_id(self):
        artwork_id = input("Enter Artwork ID to retrieve: ")

        try:
            artwork = self.virtual_gallery.getArtworkById(artwork_id)
            print("Artwork details:")
            print(artwork)
        except ArtWorkNotFoundException as e:
            print(f"Artwork not found: {e}")
        except Exception as e:
            print(f"Error retrieving artwork: {e}")

    def search_artworks(self):
        keyword = input("Enter keyword to search artworks: ")
        try:
            artworks = self.virtual_gallery.searchArtworks(keyword)
            if artworks:
                print("Search results:")
                for artwork in artworks:
                    print(artwork)
            else:
                print("No Artworks Found")
        except Exception as e:
            print(f"Error searching artworks: {e}")

    def add_artwork_to_favorite(self):
        existing_user = input("Are you an existing user? (y/n): ").lower()
        if existing_user == 'y':
            user_id = input("Enter your user ID: ")
        else:
            user_id = self.create_user()
            print(f"Your user id = {user_id}")

        if not user_id:
            print("Failed to add artwork to favorites. User ID not provided.")
            return

        arts = self.display_artworks()

        if not arts:
            print("no artworks found to add")
            return

        artwork_id = input("Enter Artwork ID to add to favorites: ")

        try:
            self.virtual_gallery.addArtworkToFavorite(user_id, artwork_id)
            print("Artwork added to favorites successfully!")
        except (ArtWorkNotFoundException, UserNotFoundException) as e:
            print(f"Error adding artwork to favorites: {e}")
        except Exception as e:
            print(f"Error adding artwork to favorites: {e}")

    def remove_artwork_from_favorite(self):
        try:
            user_id = self.get_user_favorite_artworks()
            artwork_id = input("Enter Artwork ID to remove from favorites: ")
            self.virtual_gallery.removeArtworkFromFavorite(user_id, artwork_id)
            print("Artwork removed from favorites successfully!")
        except (ArtWorkNotFoundException, UserNotFoundException) as e:
            print(f"Error removing artwork from favorites: {e}")
        except Exception as e:
            print(f"Error removing artwork from favorites: {e}")

    def get_user_favorite_artworks(self):
        user_id = input("Enter User ID to retrieve favorite artworks: ")
        try:
            favorite_artworks = self.virtual_gallery.getUserFavoriteArtworks(user_id)
            print("User's favorite artworks:")
            for artwork in favorite_artworks:
                print(artwork)
            return user_id
        except UserNotFoundException as e:
            print(f"User not found: {e}")
        except Exception as e:
            print(f"Error retrieving user's favorite artworks: {e}")

    # Gallery

    def display_galleries(self):
        try:
            galleries = self.virtual_gallery.displayGalleries()
            if galleries:
                print("Available Galleries:")
                for gallery in galleries:
                    print(gallery)
                    return True
            else:
                print("No galleries found.")
                return False
        except Exception as e:
            print(f"Error displaying galleries: {e}")

    def create_artist(self):
        try:
            name = input("Enter artist name: ")
            biography = input("Enter artist biography: ")
            birth_date = input("Enter artist birth date: ")
            nationality = input("Enter artist nationality: ")
            website = input("Enter artist website: ")
            contact_info = input("Enter artist contact information: ")
            artist = Artist(1,name, biography, birth_date, nationality, website, contact_info)
            self.virtual_gallery.addArtist(artist)
            print("Artist added successfully!")
        except Exception as e:
            print(f"Error adding artist: {e}")

    def create_gallery(self):
        name = input("Enter gallery name: ")
        description = input("Enter gallery description: ")
        location = input("Enter gallery location: ")
        opening_hours = input("Enter opening hours: ")
        curator = input("Enter curator name : ")
        gallery = Gallery(1,name, description, location, curator, opening_hours)
        try:
            self.virtual_gallery.addGallery(gallery)
            print("Gallery created successfully!")
        except Exception as e:
            print(f"Error creating gallery: {e}")

    def update_gallery(self):
        gall = self.display_galleries()
        if not gall:
            return

        try:
            gallery_id = int(input("Enter the ID of the gallery you want to update: "))
            name = input("Enter new name : ")
            description = input("Enter new description: ")
            location = input("Enter new location : ")
            opening_hours = input("Enter new opening hours : ")
            curator = input("Enter new curator name : ")
            gallery = Gallery(gallery_id, name, description, location, curator, opening_hours)
            if self.virtual_gallery.updateGallery(gallery):
                print("Gallery updated successfully!")
            else:
                print("Failed to update gallery.")
        except GalleryNotFoundException as e:
            print(f"Gallery not found: {e}")
        except Exception as e:
            print(f"Error updating gallery: {e}")

    def remove_gallery(self):
        gall = self.display_galleries()
        if not gall:
            return

        try:
            gallery_id = int(input("Enter the ID of the gallery you want to remove: "))
            self.virtual_gallery.removeGallery(gallery_id)
            print("Gallery removed successfully!")
        except GalleryNotFoundException as e:
            print(f"Gallery not found: {e}")
        except Exception as e:
            print(f"Error removing gallery: {e}")

    def search_galleries(self):
        keyword = input("Enter keyword to search galleries: ")
        try:
            galleries = self.virtual_gallery.searchGalleries(keyword)
            if galleries:
                print("Search Results:")
                for gallery in galleries:
                    print(gallery)
            else:
                print("No galleries found matching the keyword.")
        except Exception as e:
            print(f"Error searching galleries: {e}")

    def main(self):
        while True:
            print("\n==== Virtual Art Gallery Menu ====")
            print("1. Add Artwork")
            print("2. Update Artwork")
            print("3. Remove Artwork")
            print("4. Get Artwork by ID")
            print("5. Search Artworks")
            print("6. Add Artwork to Favorites")
            print("7. Remove Artwork from Favorites")
            print("8. Get User's Favorite Artworks")
            print("9. Add Artist")
            print("10. Add Gallery")
            print("11. Update Gallery")
            print("12. Remove Gallery")
            print("13. Search Galleries")
            print("14. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_artwork()
            elif choice == "2":
                self.update_artwork()
            elif choice == "3":
                self.remove_artwork()
            elif choice == "4":
                self.get_artwork_by_id()
            elif choice == "5":
                self.search_artworks()
            elif choice == "6":
                self.add_artwork_to_favorite()
            elif choice == "7":
                self.remove_artwork_from_favorite()
            elif choice == "8":
                self.get_user_favorite_artworks()
            elif choice == "9":
                self.create_artist()
            elif choice == "10":
                self.create_gallery()
            elif choice == "11":
                self.update_gallery()
            elif choice == "12":
                self.remove_gallery()
            elif choice == "13":
                self.search_galleries()
            elif choice == "14":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")



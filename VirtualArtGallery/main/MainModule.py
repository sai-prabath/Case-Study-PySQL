from VirtualArtGallery.dao.IVirtualArtGalleryimpl import IVirtualArtGalleryImpl
from VirtualArtGallery.exception.myexceptions import ArtWorkNotFoundException, UserNotFoundException, UserCreationException, ArtworkCreationException
from VirtualArtGallery.exception.myexceptions import ArtistNotFoundException, GalleryNotFoundException, GalleryCreationException
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
            print("\n------Creating User------\n")
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            firstName = input("Enter first Name: ")
            lastName = input("Enter last Name: ")
            birthDate = input("Enter birth Date: ")
            profilePicture = input("select profilePicture(enter url): ")
            user = User(None, username, password, email, firstName, lastName, birthDate, profilePicture)

            result = self.virtual_gallery.createUser(user)
            if result[0]:
                print("User created successfully!")
                print("-------------------\n")
                return result[1][0]
            else:
                raise UserCreationException()

        except Exception as e:
            print(e)
            return None

    def display_artworks(self):
        try:
            artworks = self.virtual_gallery.getAllArtworks()
            if artworks:
                print("\n------Artworks------\n")
                for artwork in artworks:
                    print(artwork)
                print("--------------------")
                return True
            else:
                raise ArtWorkNotFoundException()
        except Exception as e:
            print(e)
            return False

    def add_artwork(self):
        try:
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            creation_date = input("Enter Creation Date: ")
            medium = input("Enter Medium: ")
            image_url = input("Enter Image URL: ")
            artist_id = int(input("Enter Artist ID: "))

            artwork = Artwork(None, title, description, creation_date, medium, image_url, artist_id)
            if self.virtual_gallery.addArtwork(artwork):
                print("Artwork Added Successfully")
            else:
                raise ArtworkCreationException()
        except Exception as e:
            print(e)

    def get_artwork_by_id(self):
        try:
            artwork_id = input("Enter Artwork ID to retrieve: ")
            artwork = self.virtual_gallery.getArtworkById(artwork_id)
            if artwork:
                print("\n--------Artwork details--------\n")
                print(artwork)
                print("-------------------------------\n")
                return artwork
            else:
                raise ArtWorkNotFoundException()

        except Exception as e:
            print(e)
            return False

    def update_artwork(self):
        try:
            artwork = self.get_artwork_by_id()
            if not(artwork):
                return

            title = input("Enter new Title: ")
            if title:
                artwork.setTitle(title)
            description = input("Enter new Description: ")
            if description:
                artwork.setDescription(description)
            creation_date = input("Enter new Creation Date: ")
            if creation_date:
                artwork.setCreationDate(creation_date)
            medium = input("Enter new Medium: ")
            if medium:
                artwork.setMedium(medium)
            image_url = input("Enter new Image URL: ")
            if image_url:
                artwork.setImageURL(image_url)
            artist_id = input("Enter Artist ID: ")
            if artist_id:
                artwork.setArtistID(artist_id)
            print("\n------ Updated Artwork ------\n")
            print(artwork)
            print("-----------------------------\n")

            ch = input("Conform Update (y-yes)(n-no) : ")
            if ch == 'y':
                if self.virtual_gallery.updateArtwork(artwork):
                    print("Artwork updated successfully!")
                else:
                    raise ArtworkCreationException("Updating Unsuccessful!!!")
            else:
                print("Updation Cancelled")

        except Exception as e:
            print(e)

    def remove_artwork(self):
        arts = self.display_artworks()
        if not arts:
            return

        try:
            artwork_id = int(input("\nEnter Artwork ID to remove: "))
            if self.virtual_gallery.removeArtwork(artwork_id):
                print("Artwork removed successfully!")
            else:
                raise ArtWorkNotFoundException()

        except Exception as e:
            print(e)

    def search_artworks(self):
        keyword = input("Enter keyword to search artworks: ")
        try:
            artworks = self.virtual_gallery.searchArtworks(keyword)
            if artworks:
                print("\n--------Search results--------\n")
                for artwork in artworks:
                    print(artwork)
                print("--------------------------------\n")
            else:
                raise ArtWorkNotFoundException()
        except Exception as e:
            print(e)

    def add_artwork_to_favorite(self):
        try:
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
                return

            artwork_id = input("Enter Artwork ID to add to favorites: ")
            if self.virtual_gallery.addArtworkToFavorite(user_id, artwork_id):
                print("Artwork added to favorites successfully!")
            else:
                raise ArtWorkNotFoundException("User/Artwork not found")

        except Exception as e:
            print(e)

    def get_user_favorite_artworks(self):
        try:
            user_id = input("Enter User ID to retrieve favorite artworks: ")
            favorite_artworks = self.virtual_gallery.getUserFavoriteArtworks(user_id)
            if favorite_artworks:
                print(f"\n-----User {user_id}'s favorite artworks:-----\n")
                for artwork in favorite_artworks:
                    print(artwork)
                print(f"---------------------------------------")
                return user_id
            else:
                raise UserNotFoundException()

        except Exception as e:
            print(e)
            return None

    def remove_artwork_from_favorite(self):
        try:
            user_id = self.get_user_favorite_artworks()
            if not user_id:
                return

            artwork_id = input("Enter Artwork ID to remove from favorites: ")
            if self.virtual_gallery.removeArtworkFromFavorite(user_id, artwork_id):
                print("Artwork removed from favorites successfully!")
            else:
                raise ArtWorkNotFoundException()

        except Exception as e:
            print(e)

    # Gallery

    def display_galleries(self):
        try:
            galleries = self.virtual_gallery.displayGalleries()
            if galleries:
                print("\n--------Available Galleries--------\n")
                for gallery in galleries:
                    print(gallery)
                print("---------------------------------------")
                return True
            else:
                raise GalleryNotFoundException()
        except Exception as e:
            print(e)
            return False

    def create_artist(self):
        try:
            print("\n---------Creating Artist---------\n")
            name = input("Enter artist name: ")
            biography = input("Enter artist biography: ")
            birth_date = input("Enter artist birth date: ")
            nationality = input("Enter artist nationality: ")
            website = input("Enter artist website: ")
            contact_info = input("Enter artist contact information: ")
            artist = Artist(None, name, biography, birth_date, nationality, website, contact_info)
            print("----------------------------------\n")
            if self.virtual_gallery.addArtist(artist):
                print("Artist added successfully!")
            else:
                raise ArtistNotFoundException("Error Creating Artist")
        except Exception as e:
            print(e)

    def create_gallery(self):
        try:
            name = input("Enter gallery name: ")
            description = input("Enter gallery description: ")
            location = input("Enter gallery location: ")
            opening_hours = input("Enter opening hours: ")
            curator = input("Enter curator ID : ")
            gallery = Gallery(None, name, description, location, curator, opening_hours)
            if self.virtual_gallery.addGallery(gallery):
                print("Gallery created successfully!")
            else:
                raise GalleryCreationException()

        except Exception as e:
            print(e)

    def get_gallery_by_id(self):
        try:
            gallery_id = input("Enter Gallery ID to retrieve: ")
            gallery = self.virtual_gallery.getGalleryById(gallery_id)
            if gallery:
                print("\n--------Gallery details--------\n")
                print(gallery)
                print("-------------------------------\n")
                return gallery
            else:
                raise GalleryNotFoundException()

        except Exception as e:
            print(e)
            return False

    def update_gallery(self):
        try:
            gallery = self.get_gallery_by_id()
            if gallery == False:
                return

            name = input("Enter new Title: ")
            if name:
                gallery.setName(name)
            description = input("Enter new Description: ")
            if description:
                gallery.setDescription(description)
            location = input("Enter new Location: ")
            if location:
                gallery.setLocation(location)
            curator = input("Enter Artist ID ")
            if curator:
                gallery.setCurator(curator)
            opening_hours = input("Enter new Image URL: ")
            if opening_hours:
                gallery.setOpeningHours(opening_hours)

            print("\n------ Updated Artwork ------\n")
            print(gallery)
            print("-----------------------------\n")

            ch = input("Conform Update (y-yes)(n-no) : ")
            if ch == 'y':
                if self.virtual_gallery.updateGallery(gallery):
                    print("Gallery updated successfully!")
                else:
                    raise GalleryNotFoundException("Error Updating Gallery!")
            else:
                print("Updation Cancelled")

        except Exception as e:
            print(e)

    def remove_gallery(self):
        gall = self.display_galleries()
        if not gall:
            return

        try:
            gallery_id = int(input("Enter the ID of the gallery you want to remove: "))
            if self.virtual_gallery.removeGallery(gallery_id):
                print("Gallery removed successfully!")
            else:
                raise GalleryNotFoundException("Error Removing Gallery")

        except Exception as e:
            print(e)

    def search_galleries(self):
        keyword = input("Enter keyword to search galleries: ")
        try:
            galleries = self.virtual_gallery.searchGalleries(keyword)
            if galleries:
                print("Search Results:")
                for gallery in galleries:
                    print(gallery)
            else:
                raise GalleryNotFoundException()
        except Exception as e:
            print(e)

    def main(self):
        while True:
            print("\n------ Virtual Art Gallery Menu ------")
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
            print("--------------------------------------\n")
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



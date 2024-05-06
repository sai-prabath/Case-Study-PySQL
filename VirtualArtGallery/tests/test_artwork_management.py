
import pytest
from VirtualArtGallery.dao.IVirtualArtGalleryimpl import IVirtualArtGalleryImpl
from VirtualArtGallery.entity.artwork import Artwork
@pytest.fixture
def virtual_gallery():
    return IVirtualArtGalleryImpl()


# Artwork Management
def test_add_artwork(virtual_gallery):
    artwork = Artwork(None, "Test Artwork", "Description", "2024-04-25", "Oil on canvas", "http://example.com/image.jpg", 1)
    assert virtual_gallery.addArtwork(artwork) == True

def test_update_artwork(virtual_gallery):
    artwork = Artwork(7, "Updated Artwork", "Updated Description", "2024-04-25", "Updated Medium", "http://example.com/updated_image.jpg", 1)
    assert virtual_gallery.updateArtwork(artwork) == True

def test_remove_artwork(virtual_gallery):
    artwork_id = 7  # Assuming the ID of the artwork to be removed
    assert virtual_gallery.removeArtwork(artwork_id) == True

def test_search_artworks(virtual_gallery):
    keyword = "Test"
    artworks = virtual_gallery.searchArtworks(keyword)
    assert len(artworks) > 0

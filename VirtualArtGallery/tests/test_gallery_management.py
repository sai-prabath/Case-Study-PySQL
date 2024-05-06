# tests/test_virtual_art_gallery.py

import pytest
from VirtualArtGallery.dao.IVirtualArtGalleryimpl import IVirtualArtGalleryImpl
from VirtualArtGallery.entity.gallery import Gallery

@pytest.fixture
def virtual_gallery():
    return IVirtualArtGalleryImpl()


# Gallery Management
def test_add_gallery(virtual_gallery):
    gallery = Gallery(None, "Test Gallery", "Description", "Location", "2", "Mon-Sat 9AM-5PM")
    assert virtual_gallery.addGallery(gallery) == True

def test_update_gallery(virtual_gallery):
    gallery = Gallery(4, "Updated Gallery", "Updated Description", "Updated Location", "Updated Curator", "Mon-Sat 10AM-6PM")
    assert virtual_gallery.updateGallery(gallery) == True

def test_remove_gallery(virtual_gallery):
    gallery_id = 4  # Assuming the ID of the gallery to be removed
    assert virtual_gallery.removeGallery(gallery_id) == True

def test_search_galleries(virtual_gallery):
    keyword = "Test"
    galleries = virtual_gallery.searchGalleries(keyword)
    assert len(galleries) > 0

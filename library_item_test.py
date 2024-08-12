import pytest
from library_item import LibraryItem

def test_initialization():
    item = LibraryItem("Dummy name", "Dummy director", 5)
    assert item.name == "Dummy name"
    assert item.director == "Dummy director"
    assert item.rating == 5
    assert item.play_count == 0
    item1 = LibraryItem("Dummy name", "Dummy director")
    assert item1.name == "Dummy name"
    assert item1.director == "Dummy director"
    assert item1.play_count == 0

def test_info():
    item = LibraryItem("Dummy name", "Dummy director", 5)
    assert item.info() == "Dummy name - Dummy director ***** (Plays: 0)"
    item1 = LibraryItem("Dummy1 name", "Dummy director")
    expected_info = "Dummy1 name - Dummy director  (Plays: 0)"
    assert item1.info() == expected_info, "Info should reflect the default rating with no stars"
def test_stars():
    item = LibraryItem("Dummy name", "Dummy director", 5)
    assert item.stars() == "*****"
    item.rating = 2
    assert item.stars() == "**"
    item.rating = 0
    assert item.stars() == ""
    item1 = LibraryItem("Dummy name", "Dummy director")
    assert item1.stars() == "", "Default rating should result in no stars"
def test_increment_play_count():
    item = LibraryItem("Dummy", "Dummy director", 5)
    assert item.play_count == 0
    item.increment_play_count()
    assert item.play_count == 1
    item.increment_play_count()
    assert item.play_count == 2
    item1 = LibraryItem("Dummy name", "Dummy director")
    assert item1.play_count == 0
    item1.increment_play_count()
    assert item1.play_count == 1
    item1.increment_play_count()
    assert item1.play_count == 2



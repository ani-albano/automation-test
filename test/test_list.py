# Inherits from BaseClass
from utilities.BaseClass import BaseClass
from pageObjects.PageContents import HomePage


class TestCreate(BaseClass):

    # Creates a new item
    def test_create_item(self):
        create = HomePage(self.driver)
        create.creation()

    # Deletes the created item
    def test_delete(self):
        delete = HomePage(self.driver)
        delete.deleting()

    # Edits another item on the list
    def test_edit_item(self):
        edition = HomePage(self.driver)
        edition.edition()

    # Checks the maxlong of item creation box
    def test_maxlong(self):
        maxchar = HomePage(self.driver)
        maxchar.count()

    # Checks the precense of a certain item
    def test_present(self):
        item = HomePage(self.driver)
        item.presentitem()

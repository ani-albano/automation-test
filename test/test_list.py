# Inherits from BaseClass
from utilities.BaseClass import BaseClass
from pageObjects.PageContents import HomePage


class TestCreate(BaseClass):

    def test_create_item(self):
        create = HomePage(self.driver)
        create.creation()

    def test_edit_item(self):
        edition = HomePage(self.driver)
        edition.edition()

    def test_maxlong(self):
        maxchar = HomePage(self.driver)
        maxchar.count()

    def test_delete(self):
        delete = HomePage(self.driver)
        delete.deleting()

import unittest
from databaseFunc import databaseNeeds

class DBTest():
    def open_connection(self):
        self.assertFalse(databaseNeeds.connection("gg"))
        return True

    def store_data(self):
        self.assertFalse(databaseNeeds.connection({}))
        return False;

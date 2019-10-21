import unittest
from DBTest import DBTest

from flask_python import app

class testFlask(unittest.TestCase):
    def test_distance_response(self):
        openOrNot = DBTest.open_connection(self)
        self.assert(openOrNot)

    def test_retirement_response(self):
        openOrNot = DBTest.open_connection(self)
        self.assert(openOrNot)

    def test_retirement_data(self):
        dataAvl = DBTest.store_data(self)
        if response.data:
            dataAvl
        else:
            dataAvl

    def test_distance_data(self):
        dataAvl = DBTest.store_data(self)
        if response.data:
            dataAvl
        else:
            dataAvl

if __name__ == "__main__":
  unittest.main()

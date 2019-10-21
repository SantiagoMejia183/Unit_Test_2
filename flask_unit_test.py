import unittest
from DBTest import DBTest

from flask_python import app

class testFlask(unittest.TestCase):
    def test_distance_response(self):
        openOrNot = DBTest.open_connection(self)
        c = app.test_client()
        response = c.get('/distance/')
        self.assertEqual(openOrNot)

    def test_retirement_response(self):
        openOrNot = DBTest.open_connection(self)
        c = app.test_client()
        response = c.get('/retirement/')
        self.assertEqual(openOrNot)

    def test_retirement_data(self):
        dataAvl = DBTest.store_data(self)
        c = app.test_client()
        response = c.get('/retirement/')
        if response.data:
            dataAvl
        else:
            dataAvl

    def test_distance_data(self):
        dataAvl = DBTest.store_data(self)
        c = app.test_client()
        response = c.get('/distance/')
        if response.data:
            dataAvl
        else:
            dataAvl

if __name__ == "__main__":
  unittest.main()

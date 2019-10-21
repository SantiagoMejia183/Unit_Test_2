import unittest

from flask_python import app

class testFlask(unittest.TestCase):
    def test_distance_response(self):
        c = app.test_client()
        response = c.get('/distance/')
        self.assertEqual(response.status_code, 200)

    def test_retirement_response(self):
        c = app.test_client()
        response = c.get('/retirement/')
        self.assertEqual(response.status_code, 200)

    def test_retirement_data(self):
        c = app.test_client()
        response = c.get('/retirement/')
        if response.data:
            print('true')
        else:
            print('false')

    def test_distance_data(self):
        c = app.test_client()
        response = c.get('/distance/')
        if response.data:
            print('true')
        else:
            print('false')

if __name__ == "__main__":
  unittest.main()

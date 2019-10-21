import unittest
from datetime import datetime

from databaseFunc import databaseNeeds
# from Assignment2 import shortestDistance, retirement


class TestRetire(unittest.TestCase):
    def test_Mock_Connection(self):
        self.assertFalse(databaseNeeds.connection("gg"))

    def test_setUp(self):
        # Stub to return 20 if no data to print
        self.assertAlmostEqual(databaseNeeds.printData({}),20);

    def test_retire_insert(self):
        self.assertTrue({
                'age': 10,
                'annualSalary': 200000,
                'percentSaved': 15,
                'retirementSaveGoal': 5,
                'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

            }
        )
    def test_retire_insert_result(self):
        self.assertFalse(databaseNeeds.insertResults({}))

class TestShort(unittest.TestCase):
    def test_Mock_Connection(self):
        self.assertFalse(databaseNeeds.connection("mongodb://localhost:270/"))

    def test_setUp(self):
        # Stub to return 20 if no data to print
        self.assertNotEqual(databaseNeeds.printData({}),10);
    def test_insert(self):
        self.assertTrue( {'x1': 3, 'x2': 4, 'y1': 8,'y2': 2,'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) })

    def test_short_insert_result(self):
        self.assertFalse(databaseNeeds.insertResults({}))

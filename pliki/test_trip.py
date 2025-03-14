import unittest
from src.trip import Trip

class TestTripInitialization(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation(self):
        trip1 = Trip("Paris",7)
        self.assertIsInstance(trip1,Trip)

    def test_initialization(self):
        trip1 = Trip("Paris",7)
        self.assertEqual(trip1.destination, "Paris")
        self.assertEqual(trip1.duration, 7)

    def test_calculate_cost(self):
        trip1 = Trip("Paris",7)
        trip2 = Trip("Rome",5)
        trip3 = Trip("",0)
        self.assertEqual(trip1.calculate_cost(),700)
        self.assertEqual(trip2.calculate_cost(),500)
        self.assertEqual(trip3.calculate_cost(),0)

    def test_add_participant(self):
        trip1 = Trip("Paris",7)
        trip1.add_participant("John")
        self.assertIn("John",trip1.participants)

        trip1.add_participant("Alice")
        self.assertIn("Alice", trip1.participants)

        trip1.add_participant("Bob")
        self.assertIn("Bob", trip1.participants)

        trip1.add_participant("John")
        self.assertIn("John", trip1.participants)

        trip1.add_participant("John")
        self.assertIn("John", trip1.participants)

        trip1.add_participant("John")
        self.assertIn("John", trip1.participants)

    def test_add_empty_participant(self):
        trip1 = Trip("Paris",7)
        with self.assertRaises(ValueError) as context:
            trip1.add_participant("")
        self.assertEqual(str(context.exception),"Participant name cannot be empty")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

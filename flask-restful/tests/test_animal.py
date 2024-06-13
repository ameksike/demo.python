import unittest
from src.app import app

class AnimalTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_animals(self):
        response = self.app.get('/api/animals')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Lion', response.data.decode('utf-8'))

    def test_get_animal(self):
        response = self.app.get('/api/animals/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Panthera leo', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()

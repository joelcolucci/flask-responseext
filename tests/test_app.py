import json
import unittest

from mock_app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_status(self):
        """Test response contains expected status code"""
        response = self.app.get('/status')

        status_code = response.status_code

        self.assertEqual(status_code, 200)

    def test_content(self):
        """Test response contains expected content"""
        response = self.app.get('/content')

        content = response.data
        expected_content = 'hello, world'

        self.assertEqual(content, expected_content)

    def test_json_mimetype(self):
        """Test response contains expected json/json configuration"""
        response = self.app.get('/json')

        mimetype = response.mimetype

        self.assertEqual(mimetype, 'application/json')

    def test_json_serialization(self):
        """Test response contains expected json/json configuration"""
        response = self.app.get('/json')

        data = response.data

        try:
            decoded_data = json.loads(data)
        except ValueError:
            self.fail('Error: No JSON object could be decoded')


if __name__ == '__main__':
    unittest.main()
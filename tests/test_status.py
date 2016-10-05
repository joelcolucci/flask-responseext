"""Contains unittests for Response package status module.
"""


from unittest import TestCase, main

from flask_responseext import status


class StatusTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_200_status_code(self):
        """Test that 200 status code is named OK"""
        self.assertEqual(status.OK, 200)

    def test_201_status_code(self):
        """Test that 201 status code is named CREATED"""
        self.assertEqual(status.CREATED, 201)

    def test_204_status_code(self):
        """Test that 204 status code is named NO_CONTENT"""
        self.assertEqual(status.NO_CONTENT, 204)

    def test_301_status_code(self):
        """Test that 301 status code is named PERMANENT_REDIRECT"""
        self.assertEqual(status.PERMANENT_REDIRECT, 301)

    def test_302_status_code(self):
        """Test that 302 status code is named TEMPORARY_REDIRECT"""
        self.assertEqual(status.TEMPORARY_REDIRECT, 302)

    def test_400_status_code(self):
        """Test that 400 status code is named BAD_REQUEST"""
        self.assertEqual(status.BAD_REQUEST, 400)

    def test_401_status_code(self):
        """Test that 401 status code is named UNAUTHORIZED"""
        self.assertEqual(status.UNAUTHORIZED, 401)

    def test_403_status_code(self):
        """Test taht 403 status code is named FORBIDDEN"""
        self.assertEqual(status.FORBIDDEN, 403)

    def test_404_status_code(self):
        """Test that 404 status code is named NOT_FOUND"""
        self.assertEqual(status.NOT_FOUND, 404)

    def test_405_status_code(self):
        """Test that 405 status code is named METHOD_NOT_ALLOWED"""
        self.assertEqual(status.METHOD_NOT_ALLOWED, 405)

    def test_408_status_code(self):
        """Test that 408 status code is named REQUEST_TIMEOUT"""
        self.assertEqual(status.REQUEST_TIMEOUT, 408)

    def test_409_status_code(self):
        """Test that 409 status code is named CONFLICT"""
        self.assertEqual(status.CONFLICT, 409)

    def test_500_status_code(self):
        """Test that 500 status code is name SERVER_ERROR"""
        self.assertEqual(status.SERVER_ERROR, 500)


if __name__ == '__main__':
    main()

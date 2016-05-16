"""Contains unittests for Response package status module.
"""


from unittest import TestCase, main

from flask_responsefactory import Status


class StatusTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_200_status_code(self):
        """Test that 200 status code is named OK"""
        self.assertEqual(Status.OK, 200)

    def test_201_status_code(self):
        """Test that 201 status code is named CREATED"""
        self.assertEqual(Status.CREATED, 201)

    def test_204_status_code(self):
        """Test that 204 status code is named NO_CONTENT"""
        self.assertEqual(Status.NO_CONTENT, 204)

    def test_301_status_code(self):
        """Test that 301 status code is named PERMANENT_REDIRECT"""
        self.assertEqual(Status.PERMANENT_REDIRECT, 301)

    def test_302_status_code(self):
        """Test that 302 status code is named TEMPORARY_REDIRECT"""
        self.assertEqual(Status.TEMPORARY_REDIRECT, 302)

    def test_400_status_code(self):
        """Test that 400 status code is named BAD_REQUEST"""
        self.assertEqual(Status.BAD_REQUEST, 400)

    def test_401_status_code(self):
        """Test that 401 status code is named UNAUTHORIZED"""
        self.assertEqual(Status.UNAUTHORIZED, 401)

    def test_403_status_code(self):
        """Test taht 403 status code is named FORBIDDEN"""
        self.assertEqual(Status.FORBIDDEN, 403)

    def test_404_status_code(self):
        """Test that 404 status code is named NOT_FOUND"""
        self.assertEqual(Status.NOT_FOUND, 404)

    def test_405_status_code(self):
        """Test that 405 status code is named METHOD_NOT_ALLOWED"""
        self.assertEqual(Status.METHOD_NOT_ALLOWED, 405)

    def test_408_status_code(self):
        """Test that 408 status code is named REQUEST_TIMEOUT"""
        self.assertEqual(Status.REQUEST_TIMEOUT, 408)

    def test_409_status_code(self):
        """Test that 409 status code is named CONFLICT"""
        self.assertEqual(Status.CONFLICT, 409)

    def test_500_status_code(self):
        """Test that 500 status code is name SERVER_ERROR"""
        self.assertEqual(Status.SERVER_ERROR, 500)


if __name__ == '__main__':
    main()

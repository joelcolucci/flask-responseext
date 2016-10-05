"""Contains unit tests for Response package response module.
"""

from unittest import TestCase, main

from flask import Response as FlaskResponse

from flask_responseext import Response


class ResponseTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_subclass_of_flask_response(self):
        """Test that build method returns flask response object"""
        response = Response()

        self.assertIsInstance(response, FlaskResponse)


if __name__ == '__main__':
    main()

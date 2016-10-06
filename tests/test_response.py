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


    def test_set_status_method_success(self):
        """Test method sets Response status"""
        response = Response()

        response.set_status(404)

        self.assertEqual(response.status_code, 404)

    def test_set_status_returns_self(self):
        """Test method returns self"""
        response = Response()

        return_val = response.set_status(404)

        self.assertIsInstance(return_val, Response)

    def test_set_headers_success(self):
        """Test method assigns headers to Response object"""
        response = Response()

        response.set_headers({'Access-Control-Allow-Origin': '*'})

        accessControlMatcher = response.headers['Access-Control-Allow-Origin']
        
        self.assertEqual(accessControlMatcher, '*')

    def test_set_headers_returns_self(self):
        """Test method returns self"""
        response = Response()

        return_val = response.set_headers({'Access-Control-Allow-Origin': '*'})

        self.assertIsInstance(return_val, Response)

    def test_to_json_success(self):
        pass

if __name__ == '__main__':
    main()

"""Contains unit tests for Response package response module.
"""

from unittest import TestCase, main

from flask import Response as FlaskResponse

from flask_responsefactory import Response


class ResponseTestCase(TestCase):
    def setUp(self):
        Response.status(200)

    def tearDown(self):
        pass

    def test_build_method_returns_flask_response(self):
        """Test that build method returns flask response object"""
        response = Response.build()

        self.assertIsInstance(response, FlaskResponse)

    def test_build_method_returns_default_200(self):
        """Test that build method returns flask response with 200 status code"""
        response = Response.build()

        self.assertEqual(response.status_code, 200)

    def test_build_method_returns_payload(self):
        """Test that build methods accepts arg and converts to Flask response object"""
        payload = '<message>hello</message>'

        response = Response.build(payload)

        data = response.data

        self.assertEqual(payload, data)

    def test_json_method_returns_flask_response(self):
        """Test that json method returns flask response object"""
        payload = {'status': 'success'}

        response = Response.json(payload)

        self.assertIsInstance(response, FlaskResponse)

    def test_json_method_returns_default_200(self):
        """Test that json method returns flask response with 200 status code"""
        payload = {'status': 'success'}

        response = Response.json(payload)

        self.assertEqual(response.status_code, 200)

    def test_json_method_returns_response_with_mimetype(self):
        """Test that JSON method returns with correct mimetype header"""
        payload = {'status': 'success'}

        response = Response.json(payload)

        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_status_method_sets_class_variable(self):
        """Test that status method set class variable status_code"""
        new_status_code = 400

        Response.status(new_status_code)

        self.assertEqual(new_status_code, Response.status_code)

    def test_status_method_returns_class(self):
        """Test that status method returns class"""
        response = Response.status(200)

        self.assertEqual(type(response), type(Response))

    def test_chained_status_build_successful(self):
        """Test that chaining status and build works as expected"""
        new_status_code = 300
        response = Response.status(new_status_code).build()

        self.assertIsInstance(response, FlaskResponse)
        self.assertEqual(response.status_code, 300)

    def test_chained_status_json_successful(self):
        """Test that chaining status and build works as expected"""
        new_status_code = 300
        payload = {'status': 'success'}

        response = Response.status(new_status_code).json(payload)

        self.assertIsInstance(response, FlaskResponse)
        self.assertEqual(response.status_code, 300)


if __name__ == '__main__':
    main()

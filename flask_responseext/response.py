"""Module contains Response class. The Response class follows the factory
pattern for producing Flask's Response object with applicable HTTP status codes.
"""


import json

from flask import Response as FlaskResponse


class Response(FlaskResponse):
    """Flask Response class with extended functionality"""

    def __init__(self):
        pass
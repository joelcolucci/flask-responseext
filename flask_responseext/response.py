"""
    flask_responseext.response

    Contains Response subclass of Flask Response object
"""


import json

from flask import Response as FlaskResponse


class Response(FlaskResponse):
    """Flask Response subclass providing ability to chain
    setter methods"""

    def __init__(self, rv=None, **kwargs):
        FlaskResponse.__init__(self, rv, **kwargs)

    def set_status(self, status_code):
        self.status_code = status_code

        return self

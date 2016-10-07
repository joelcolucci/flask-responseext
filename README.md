# Flask ResponseExt [![Build Status](https://travis-ci.org/joelcolucci/flask-responseext.svg?branch=master)](https://travis-ci.org/joelcolucci/flask-responseext)
An extension of the Flask Response class. Provides convenience methods and method chaining on the Response object.

## Installation
```
$ pip install Flask-ResponseExt
```

## Getting Started
```python
from flask_responseext import Response
from flask_responseext import status


@app.route('/api/v1/item', methods=['GET'])
def get_items():
    """Return items from database"""
    items = db.items.get()

    return Response(items)
            .set_status(status.OK)
            .set_headers({'Access-Control-Allow-Origin': '*'})
            .to_json()
```

## Documentation
Coming soon..

## License
MIT License Copyright (c) 2016 Joel Colucci

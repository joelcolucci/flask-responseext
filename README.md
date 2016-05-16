# Flask Response Factory

## Description
Create Flask response objects in a declarative way.

## Installation
1. Create a new virtual environment:
```
$ virtualenv venv
```

2. Activate the environment
```
$ source venv/bin/activate
```
3. Install project dependencies
```
$ pip freeze > requirements.txt
```

## Usage
```
from flask_responsefactory import Response
from flask_responsefactory import Status


@app.route('/api/v1/item', methods=['GET'])
def get_items():
    """Return items from database"""

    try:
        items = db.item.get()
    except exceptions.InvalidDatabaseRequest:
        response = Response.status(Status.BAD_REQUEST).build()
    except Exception:
        response = Response.status(Status.SERVER_ERROR).build()
    else:
        response = Response.status(Status.OK).json(items)

    return response
```

## License

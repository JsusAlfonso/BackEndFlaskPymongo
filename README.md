# Pymongo Data Base
This project was generated with [Python](https://www.python.org/downloads/release/python-395/) version 3.9.5

## Development server
Run `python .\server\server.py` for a dev server. Navigate to `http://localhost:5050/`.

## Installers
pip install requests
pip install Flask
pip install Flask-PyMongo
`--------optional--------`
pip install Flask-WTF
pip install Flask-RESTful
pip install flask_cors
pip install pymongo
pip install pyjwt
pip install reportlab
`------------------------`

## How to get info

we needed to use:
`request.args.get('paramName')` to get information from the query.
`request.headers.get('headerName')` to get information from the headers.
`request.form['bodyName']` to get information from the body.
`request.files['file'].filename` to get information from the file.
`request.json["parameter"]` to get information from json parameters.

## Config
we have the connection and the mongo uri in this file.

## Help
To get more help on the [Pymongo-Flask](https://flask-pymongo.readthedocs.io/en/latest/) version 2.3.0 show this url.

## VS-Code
 Install [REST-Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
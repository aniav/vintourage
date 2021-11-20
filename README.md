This project is deployed to:

http://bezmetki.org

Requirements:
- python 3

Pre-requirements for OS X:
```
brew install postgresql openssl
```

### Setup virtual environment
`python3 -m venv venv`

### Activate virtual environment
`source venv/bin/activate`


### Preparing the database
```
flask db init
flask db upgrade
```


### Running the flask app locally
Acivate the virtual environment and run:
```
export FLASK_APP=vintourage
export FLASK_ENV=development
flask run
```

Running the spiders:
```
python -m crawler.executor
```
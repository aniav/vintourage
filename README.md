This project is deployed to:

http://bezmetki.org

Running the flask app locally. Activate virtualenv and run:
```
export FLASK_APP=vintourage
export FLASK_ENV=development
flask run
```

Running the spiders:
```
python vintourage/crawler/executor.py
```
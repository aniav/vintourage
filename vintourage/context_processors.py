from datetime import datetime

from . import app

@app.context_processor
def inject_user():
    return dict(now=datetime.now())
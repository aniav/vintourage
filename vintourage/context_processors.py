from datetime import datetime

from . import app

@app.context_processor
def inject_now():
    return dict(now=datetime.now())
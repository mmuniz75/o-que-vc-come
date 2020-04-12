from sql_alchemy import db
from gevent.pywsgi import WSGIServer
from routes import app

import os

@app.before_first_request
def create_db():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    if 'OQVC_DEVELOP' in os.environ:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run()

    ''''
    if 'OQVC_DEVELOP' in os.environ:
        db.init_app(app)
        app.run(host='0.0.0.0', port=5000, debug=True)
        
    else:
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
    '''


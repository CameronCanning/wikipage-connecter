import os
from flask import Flask, request
#from linksearch import LinkSearch

print('importing wpc')
def create_app(test_config = None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    #try:
        #os.makedirs(app.instance_path)
    #except OSError:
        #pass

    @app.route('/link', methods=['GET'])
    def link():
        params = request.args.to_dict()
        return params
    
    return app
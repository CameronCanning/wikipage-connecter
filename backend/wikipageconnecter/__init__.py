import os

from .wikiclient import WikiClient
from .linksearch import LinkSearch
from flask import Flask, request

def create_app(test_config = None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY')
        #SECRET_KEY='dev',
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
        start = request.args.get('start', type = str)
        end = request.args.get('end', type = str)

        if not start or not end:
            return 'bad', 400

        start = start.replace(' ','_') 
        end = end.replace(' ','_')
        print(start, end)
        chain = LinkSearch(start, end).search()

        for i in range(len(chain)):
            chain[i] = chain[i].replace('_', ' ')
            
        return {'chain': chain}
    
    @app.route('/search', methods=['GET'])
    def search():
        string = request.args.get('string')

        if string == '':
            return {'results': []}

        results = WikiClient().getSearch(string)
        return {'results': results}


    return app
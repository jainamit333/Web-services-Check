
from flask import Flask, render_template
import json
import requests
import os
from settings import APP_STATIC

app = Flask(__name__)


@app.route('/')
def index():


    return 'CMS : cms , Dhruv : dhruv , drools : drools'

@app.route('/<type>')
def cms(type):

    result = {}
    with open(os.path.join(APP_STATIC, type+'.json')) as f:
        json_file = f.read()
        json_file = json.loads(json_file)
        headers = json.loads(json_file['header'])
        for pay in json_file['payload']:
            url = pay['url']
            payload = pay['pay']
            response = requests.request("POST", url, data=payload, headers=headers)
            result[url] = response

        return render_template('result.html',result=result);

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

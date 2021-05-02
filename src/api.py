from flask import Flask, request
from flask_cors import CORS     

app = Flask(__name__)
CORS(app)

import preprocessing
import queryprocessing



app.run(host='0.0.0.0')
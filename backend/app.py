from flask import Flask, send_from_directory, Response,jsonify, request
from helper import randomize_infile, randomize_inmemory
import os

app = Flask(__name__)

@app.after_request
def apply_caching(res):
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Content-Type']='application/json'
    return res

@app.route("/generate")
def generate():    
    if app.config['processor'] == 'file':
        result = randomize_infile(max_size=2000000)
    else:
        result = randomize_inmemory(max_size=2000000)
    out =  {
        "state":True,
        "message":"Success",
        "processor": app.config['processor'],
        "file_url" : f"{request.scheme}://{request.host}/result/{result['filename']}",
        "file_size": result['size'],
        "report" : result['report'],
        "timecost": str(result['eta']),
    }
    print(out)
    return jsonify(out)


@app.route("/result/<filename>")
def get_result(filename):
    if not os.path.exists(f"output/{filename}"):
        return "<div align='center'><h1>Are you lost something?</h4></div>",404
    return send_from_directory("output", filename, as_attachment=True)

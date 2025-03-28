from flask import Flask, request, jsonify
import flask
from PubSub import pubsub
import threading
import queue
import time
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def process_file(upload_id, filename,pubsub):
    """ Simulate file upload with progress updates """
    
    for i in range(1, 6):
        time.sleep(10)  # Simulating upload time
        pubsub.Publish(event= upload_id,msg= f"Uploading {filename}... {i*20}%")

    pubsub.Publish(event=upload_id, msg="Completed")

@app.route('/upload', methods=['POST'])
def upload_file():
    """ Handle file upload and return upload ID immediately """
    
    file = request.files['file']
    filename = file.filename
    upload_id = str(int(time.time()))  # Generate a unique ID
    
    pubsub.Publish(event=upload_id,msg="Upload Started")
    # Start upload in background thread
    
    threading.Thread(target=process_file, args=(upload_id, filename,pubsub)).start()
    
    return jsonify({"upload_id": upload_id, "message": "Upload started"}), 202

@app.route('/status/<upload_id>', methods=['GET'])
def upload_status(upload_id):
    
    """ Get upload status """
    def stream():
            messages = pubsub.Subscribe(event_type=upload_id)  # returns a queue.Queue
            while True:
                try :
                    msg = messages.get(timeout=30)  # blocks until a new message arrives
                    yield msg
                except queue.Empty:
                    print("Empty Queue")
                    yield "event : end\ndata:Connection closed"
                    pubsub.Unsubscribe(upload_id,queue=messages)
                    break
    return flask.Response(stream(), mimetype='text/event-stream')
  
if __name__ == '__main__':
    Mode = "prod"
    if Mode=="dev" :
        app.run(port=5000)
    elif Mode=="prod":
        serve(app,port=5000)

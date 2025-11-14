from flask import Flask, Response
from prometheus_flask_exporter import PrometheusMetrics

# Create the Flask app
app = Flask(__name__)

# Add metrics /metrics endpoint
metrics = PrometheusMetrics(app)

# A simple main route
@app.route('/')
def hello():
    return "Hello! App is running. Check /metrics for Prometheus data."

# A status route, just like in the lab example
@app.route('/status')
def status():
    return Response('{"status":"OK"}', mimetype='application/json')

# This makes the app runnable with 'python app.py'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
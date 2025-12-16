from flask import Flask, request, jsonify
from renderer import start_render, jobs

app = Flask(__name__)

@app.route("/render", methods=["POST"])
def render():
    data = request.json
    job_id = start_render(data["video"], data["quote"])
    return jsonify({"job_id": job_id}), 202

@app.route("/status/<job_id>", methods=["GET"])
def status(job_id):
    return jsonify(jobs.get(job_id, {"error": "not found"}))

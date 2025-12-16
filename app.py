from flask import Flask, request, jsonify
from renderer import start_render, get_status

app = Flask(__name__)


@app.route("/render", methods=["POST"])
def render():
    data = request.json

    video = data.get("video")
    quote = data.get("quote")

    if not video or not quote:
        return jsonify({"error": "video and quote required"}), 400

    job_id = start_render(video, quote)

    return jsonify({
        "job_id": job_id,
        "status": "processing"
    })


@app.route("/status/<job_id>", methods=["GET"])
def status(job_id):
    job = get_status(job_id)

    if job is None:
        return jsonify({"error": "job not found"}), 404

    return jsonify(job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

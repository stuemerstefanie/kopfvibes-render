@app.route("/render", methods=["POST"])
def render():
    data = request.json

    video_url = data.get("video")   # <-- DAS ist der Fix
    quote = data.get("quote")

    print("RENDER REQUEST:", video_url, quote)

    if not video_url or not quote:
        return jsonify({"error": "video and quote required"}), 400

    job_id = start_render(video_url, quote)

    return jsonify({
        "job_id": job_id,
        "status": "processing"
    })

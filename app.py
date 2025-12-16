from flask import Flask, request, send_file
import subprocess, uuid, os

app = Flask(__name__)

@app.route("/render", methods=["POST"])
def render():
    data = request.json
    video = data["video"]
    quote = data["quote"]

    out = f"/tmp/{uuid.uuid4()}.mp4"

    cmd = [
        "ffmpeg", "-y",
        "-i", video,
        "-vf",
        f"drawtext=text='{quote}':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=(h-text_h)/2,format=gray",
        out
    ]

    subprocess.run(cmd, check=True)
    return send_file(out, mimetype="video/mp4")

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

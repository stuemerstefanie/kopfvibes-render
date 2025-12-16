import threading
import time
import uuid

jobs = {}

def render_video(job_id, video_url, quote):
    jobs[job_id]["status"] = "rendering"
    time.sleep(20)  # simuliert Rendering
    jobs[job_id]["status"] = "done"
    jobs[job_id]["video_url"] = f"https://example.com/{job_id}.mp4"

def start_render(video_url, quote):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued", "video_url": None}

    t = threading.Thread(
        target=render_video,
        args=(job_id, video_url, quote),
        daemon=True
    )
    t.start()

    return job_id

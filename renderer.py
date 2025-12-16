import threading
import uuid
import time

jobs = {}

def render_video(job_id, video_url, quote):
    # SIMULATION – hier kommt dein echtes Rendern rein
    time.sleep(25)  # simuliert langes Rendern

    # später: echtes ffmpeg / moviepy Ergebnis
    jobs[job_id]["status"] = "done"
    jobs[job_id]["video_url"] = f"https://example.com/{job_id}.mp4"


def start_render(video_url, quote):
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "processing",
        "video_url": None
    }

    thread = threading.Thread(
        target=render_video,
        args=(job_id, video_url, quote)
    )
    thread.start()

    return job_id


def get_status(job_id):
    return jobs.get(job_id)

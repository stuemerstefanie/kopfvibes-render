import threading
import time
import uuid

jobs = {}


def render_video(job_id, video_url, quote):
    try:
        print("START RENDER:", job_id)

        time.sleep(10)  # absichtlich kürzer zum Test

        jobs[job_id]["status"] = "done"
        jobs[job_id]["video_url"] = f"https://example.com/{job_id}.mp4"

        print("RENDER DONE:", job_id)

    except Exception as e:
        print("RENDER ERROR:", e)
        jobs[job_id]["status"] = "error"



def start_render(video_url, quote):
    print("START_RENDER CALLED", video_url)



def get_status(job_id):
    job = jobs.get(job_id)

    if not job:
        return {
            "status": "processing"
        }

    return job


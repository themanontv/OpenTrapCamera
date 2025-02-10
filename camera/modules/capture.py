from datetime import datetime
from picamzero import Camera


def photo(cwd):
    """
    Takes a still photo using the attached camera
    :param cwd: Current working directory
    """
    cam = Camera()
    time = datetime.now()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")

    file_path = cwd + "/images/" + formatted_time + "_capture.jpg"
    cam.take_photo(file_path)

    return file_path


def video(cwd, duration):
    """
    Takes a video using the attached camera
    Requires FFMPEG to be installed
    :param cwd: Current working directory
    :param duration: Length of the video in seconds
    """
    cam = Camera()
    time = datetime.now()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")

    file_path = cwd + "/videos/" + formatted_time + "_capture.mp4"
    cam.record_video(file_path, duration=duration)

    return file_path

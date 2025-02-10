from datetime import datetime
from picamzero import Camera

def still(cwd):
	cam = Camera()
	time = datetime.now()
	formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
	
	file_path = cwd + "/images/" + formatted_time + "_capture.jpg"
	cam.take_photo(file_path)
	
	return file_path
	
def video(cwd):
	# Requires FFMPEG to be installed
	cam = Camera()
	time = datetime.now()
	formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
	
	file_path = cwd + "/images/" + formatted_time + "_capture.jpg"
	cam.record_video(file_path, duration=5)
	
	return file_path
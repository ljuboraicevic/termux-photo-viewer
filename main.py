import subprocess
from flask import Flask, send_file
import os 

app = Flask(__name__)

@app.route("/")
def main():
	
	if not ('TPV_PORT' in os.environ and 'TPV_USER' in os.environ and 'TPV_HOST' in os.environ):
		return "Port, user or host env vars are not set."
	
	port = os.environ.get('TPV_PORT')
	user = os.environ.get('TPV_USER')
	host = os.environ.get('TPV_HOST')
	photo_name = "photo.jpg"
	local_path = os.path.dirname(os.path.realpath(__file__))
	remote_path = f"/data/data/com.termux/files/home"
	# this option allows ssh to proceed even if the remote server's keys
	# are not in authorized keys
	accept_new = "StrictHostKeyChecking=accept-new"
	
	command0 = f'rm -f {local_path}/{photo_name}'
	subprocess.run(command0, shell=True)
	
	command1 = f'ssh -i /app/.ssh/id_rsa -o {accept_new} -p {port} {user}@{host} "rm -f {photo_name} && termux-camera-photo {photo_name}"'
	subprocess.run(command1, shell=True)
	
	command2 = f'scp -i /app/.ssh/id_rsa -o {accept_new} -P {port} {user}@{host}:{remote_path}/{photo_name} {local_path}/'
	subprocess.run(command2, shell=True)
	
	return send_file(f'{local_path}/{photo_name}', mimetype='image/jpeg')

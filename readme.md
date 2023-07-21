# termux-photo-viewer

Take photos on Android devices using Termux and view them in your browser.

## Building the Docker image

    docker build --progress=plain --tag termux-photo-viewer .

## Running the image

    docker run -p 5000:5000 --restart unless-stopped --name termux-photo-viewer-cont -v /home/user/.ssh:/app/.ssh termux-photo-viewer

## Viewing the photos in the browser

    http://localhost:5000/?port=<PORT>&user=<TERMUX_USER>&host=<TERMUX_DEVICE_IP>

## Termux setup

1. Install Termux (https://termux.dev/en/) on a compatible Android device

2. Install openssh

	a. apk install openssh
	
	b. set up password (https://wiki.termux.com/wiki/Remote_Access#Using_the_SSH_server)
	
	c. run sshd
	
	d. obtain a wake lock in the Termux notification item

3. The device is now ready to receive ssh connections

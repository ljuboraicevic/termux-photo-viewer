# termux-photo-viewer

Take photos on Android devices using Termux and view them in your browser.

## Building the Docker image

    docker build --progress=plain --tag termux-photo-viewer .

## Running the image

The image can only be run on a host that has ssh keys that are needed to connect to the Android device. These keys need to be mounted as a volume into the container.

    docker run -d \
        -p 5000:5000 \
        --restart unless-stopped \
        --name termux-photo-viewer-cont \
        -v /home/user/.ssh:/app/.ssh \
        -e TPV_PORT='TERMUX_SSH_PORT' \
        -e TPV_USER='TERMUX_USER' \
        -e TPV_HOST='TERMUX_IP' \
        termux-photo-viewer

## Viewing the photos in the browser

    http://localhost:5000/

## Termux setup

1. Install Termux (https://termux.dev/en/) on a compatible Android device

2. Install openssh

	a. apk install openssh
	
	b. set up password (https://wiki.termux.com/wiki/Remote_Access#Using_the_SSH_server)
	
	c. run sshd
	
	d. obtain a wake lock in the Termux notification item

3. The device is now ready to receive ssh connections

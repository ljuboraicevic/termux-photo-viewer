# termux-photo-viewer

Take photos on Android phones using Termux and view them in your browser.

## Building the Docker image

    docker build --progress=plain --tag termux-photo-viewer .

## Running the image

    docker run --restart unless-stopped --net=host --name termux-photo-viewer-cont -v /home/user/.ssh:/app/.ssh termux-photo-viewer

## Viewing the photos in the browser

    http://localhost:5000/?port=<PORT>&user=<TERMUX_USER>&host=<TERMUX_PHONE_IP>

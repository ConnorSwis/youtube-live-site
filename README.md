# Youtube Live Site

This Docker image is a simple web server that displays the live stream of a YouTube channel.

![example image](demo.png)

## Usage

Docker run:

```
docker run -d --name youtube-live-site \
  -e YOUTUBE_CHANNEL_ID=[YOUTUBE CHANNEL ID] \
  -p [HOST PORT]:8000 \
  connorswislow/youtube-live-site:latest
```

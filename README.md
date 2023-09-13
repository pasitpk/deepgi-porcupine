# Deepgi Porcupine

This repository illustrates the application of Porcupine with the wake word "Hey, Deep GI," following this [tutorial](https://picovoice.ai/blog/python-wake-word-detection-tutorial/).

(the custom keywords are "hey deep g i" and "hey dip g i")

Install the Python SDK:

```console
pip install pvporcupine pvrecorder python-dotenv
```

Get access key from [Picovoice](https://console.picovoice.ai/) and save to ".env":

```bash
ACCESS_KEY=YOUR_ACCESS_KEY_HERE
```

Run the programe:
```console
python run.py
```

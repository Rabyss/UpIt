import requests
import requests.exceptions
import json
import sys
import base64
from subprocess import Popen, PIPE


def to_clipboard(text: str):
    clipboard_proc = Popen(['xclip', '-selection', 'c'], stdin=PIPE)
    clipboard_proc.communicate(input=bytes(text, 'utf-8'))


# replace with any notification logic you like
def notify(notif_type: str, title: str, msg: str):
    notif_proc = Popen(["notify-send", "-i", notif_type,  title, msg])
    notif_proc.communicate()


def notify_info(title: str, msg: str):
    notify("info", title, msg)


def notify_error(title: str, msg: str):
    notify("error", title, msg)


API_KEY = "YOUR_API_KEY"
URL = "https://api.imgur.com/3/upload.json"
TITLE = "Screenshot"


with open(sys.argv[1], 'rb') as image:
    b64_image = base64.b64encode(image.read())

payload = {"key": API_KEY,
           "image": b64_image,
           "title": TITLE}

req_result = None
try:
    req_result = requests.post(URL, data=payload, headers={'Authorization': "Client-ID YOUR_CLIENT_ID"})
except requests.exceptions.ConnectionError:
    notify_error("Connection Error", "Verify your internet connection")

if req_result is not None:
    result_json = json.loads(req_result.text)

    try:
        to_clipboard(result_json["data"]["link"])
        notify_info("Upload succeeded", "The URL of your upload has been placed in your clipboard.")
    except KeyError:
        notify_error("Request malformed", "Imgur answered \"" + result_json["data"]["error"] + "\"")

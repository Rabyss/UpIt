import requests
import json
import sys
import base64
from subprocess import Popen, PIPE


def to_clipboard(text):
    clipboard_proc = Popen(['xclip', '-selection', 'c'], stdin=PIPE)
    clipboard_proc.communicate(input=bytes(text, 'utf-8'))

api_key = "YOUR_API_KEY"
 
url = r"https://api.imgur.com/3/upload.json"
 
image_path = sys.argv[1]
 
f = open(image_path, 'rb')

binary_data = f.read()
b64image = base64.b64encode(binary_data)

title = "Screeny"

payload = {"key": api_key,
           "image": b64image,
           "title": title}

req_result = requests.post(url, data=payload, headers={'Authorization': "Client-ID YOUR_CLIENT_ID"})
 
result_json = json.loads(req_result.text)

to_clipboard(result_json["data"]["link"])
# Replace this with any notification logic you'd want to have
notif_proc = Popen(["notify-send", "-i", "info",  "Screenshot uploaded", "URL has been copied to clipboard"])
notif_proc.communicate()

# UpIt
Python script to upload images on imgur.com

### Prerequisites

1. You should have an anonymous API key from Imgur, you can get one and a client id here : [Imgur application register](https://api.imgur.com/oauth2/addclient)
2. You should have xclip installed on your system, however you can replace the ```to_clipboard``` method by any method that could suit you to copy a text to your clipboard.
3. And of yourse you need python3 installed

### How to run the project

1. Replace the ```API_KEY``` and ```CLIENT_ID``` in the script by the right values
2. Simply run  ```python3 upit.py /path/to/image```
3. You can also use it in combination of other programs, for instance you can take a screenshot in your xfce4 desktop environment like this ``` xfce4-screenshooter -r -o "python3 /path/to/upit.py"```, which will automatically upload it to imgur.

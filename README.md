# PokeFriends

This little python-adb script iterates over your pokemon go friends, gets its name, and saves it to the [friends.txt](https://github.com/davidfegyver/pokefriend/friends.txt) file.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

You need the [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Downloads) too.


## Usage
Edit the config.yaml 
They are the coordinates where the name/tap point is. 
```
[x1,y1,x2,y2]: gives a box
or
[x,y]: gives a point
```

Enable USB debugging on your phone

Open Pokemon Go
Go to your friend list
Tap your first friend
Run the pokefriends.py



## Contributing
Pull requests are welcome.

## TODO

Auto config
Comments for easier learning
Auto friend count
get Level + team 
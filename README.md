# SongQR
SongQR is a Python program that generates a QR code for any song name. Scanning the QR code automatically opens YouTube and searches for the song, making it easy to play music instantly.
# SongQR

**SongQR** is a Python project that generates a QR code for any song name. When scanned, the QR code automatically opens YouTube and searches for the song, making it easy to play music directly from your phone.

## Features

- Generate a QR code from any song name.  
- Automatically opens YouTube search results when scanned.  
- Saves the QR code as an image (`.png`) that can be shared.  
- Simple and beginner-friendly Python project.

## Requirements

- Python 3.x  
- `qrcode` library  
- `Pillow` library (for saving the QR code image)

Install the required libraries with:

```bash
pip install qrcode[pil]

How to Use

Clone or download this project.

Open the project folder in your terminal or code editor.

Run the Python script:

python mainproject.py


Enter the song name when prompted.

A QR code image (song_name_qr.png) will be generated in the project folder.

Scan the QR code with your phone — it will open YouTube with the song search results.

Example

Input:

Enter the song name: Shape of You


Output:
A QR code image named song_name_qr.png. Scanning it searches the song on YouTube automatically.

How It Works

User enters the song name.

Spaces in the song name are replaced with + to form a valid YouTube search URL.

The qrcode library generates the QR code.

The QR code is saved as an image and ready to scan.

Future Improvements

Auto-play the first YouTube result directly.

Support multiple songs at once.

Add other platforms like Spotify or SoundCloud.

License

This project is open-source and free to use.


---

If you want, I can also **make a shorter, cleaner version specifically for GitHub**, with badges and professional look, ready to attract viewers.  

Do you want me to do that?

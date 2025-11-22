import qrcode

# Step 1: Ask for song name
song_name = input("Enter the song name: ")

# Step 2: Make a YouTube search link (optional for auto-play)
search_url = "https://www.youtube.com/results?search_query=" + song_name.replace(" ", "+")

# Step 3: Generate QR code (use the URL, not just the song name)
qr = qrcode.QRCode()
qr.add_data(search_url)  # Add the URL so it opens YouTube


# Step 4: Save QR code image
img = qr.make_image()  # You forgot the parentheses ()
img.save("song_name_qr.png")

print("QR code generated! Scan it to play the song on YouTube.")

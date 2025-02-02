import qrcode as qr
img=qr.make("https://www.youtube.com/@selfgrowth5721")
img.save("youtube_qr.png")
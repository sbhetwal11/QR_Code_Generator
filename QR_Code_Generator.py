import qrcode

url = input("Please Enter URL for QR code Generation: ")
img = qrcode.make(url)
img.save("URL_qrcode.png")
print("QR code saved as URL_qrcode.png")
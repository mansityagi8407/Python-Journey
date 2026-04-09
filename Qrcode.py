import qrcode
qr = qrcode.make("https://www.linkedin.com/in/mansi-tyagi-07204")
qr.save("My_qrcode.png")
print("qrcode generated successfully.")

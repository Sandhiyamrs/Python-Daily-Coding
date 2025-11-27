import qrcode

def generate_qr(text, filename="qr.png"):
    img = qrcode.make(text)
    img.save(filename)
    print("QR code generated!")

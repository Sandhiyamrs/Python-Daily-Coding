import cv2
from pyzbar import pyzbar

def scan_qr(image_path):
    img = cv2.imread(image_path)
    codes = pyzbar.decode(img)
    for code in codes:
        print("QR Code Data:", code.data.decode('utf-8'))

image_path = input("Enter image path with QR code: ")
scan_qr(image_path)

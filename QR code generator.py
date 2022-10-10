import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
# str that rep the qr

url = pyqrcode.create(s)
# generating the code

url.svg('myyoutube.svg', scale=8)
# create and save the png file namng "myqr.png"

import os
import qrcode

img = qrcode.make("jeantheron.online")

img.save("qr.png", "PNG")

os.system("display qr.png")
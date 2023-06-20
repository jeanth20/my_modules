# Importing library
import qrcode
import os

 
# Data to encode
data = "Lets add some data to the QR code"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'green',
                    back_color = 'white')
 
img.save('MyQRCode2.png')
os.system("display MyQRCode2.png")
import qrcode
from qrcode.console_scripts import error_correction

qr = qrcode.QRCode(
    #version is for constructing the size of the QRCode, 1 means qrcode is a 21 by 21 matrix
    version = 1,
    #error_correction is for handling errors in our qrcode
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    #box_size is to set the size of the small squares required to set up the QRCode,
    #the size right now is 10 by 10 pixels
    box_size = 10,

    border = 4
)
#this is where you need to input the link to get a QR code.
qr.add_data("https://www.youtube.com/watch?v=T0u5nwSA0w0")

#to change the color of the qr code
img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qrcode.jpg")
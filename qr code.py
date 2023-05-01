import qrcode as qr
img = qr.make("https://www.javatpoint.com/generate-a-qr-code-using-python#:~:text=Installing%20the%20Python%20qrcode%20package,%24%20pip%20install%20qrcode")
img.save("qrcodepython.png")
# this qrcode can be detected and decoded using opencv library
import qrcode
data ="i love someone Who never love me "


image = qrcode.make(data)

image.save("F:/projects/Projects/project02/myqrcode.png")


# qr =qrcode.QRCode(version=1,box_size=10,border=5)
# qr.add_data(data)
# qr.make(fit=True)
# image =qr.make_image(fill_color='red',back_color='white')
# image.save("F:/projects/Projects/project02/myqrcode1.png")
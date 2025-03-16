from pyzbar.pyzbar import decode
from PIL  import Image
img=Image.open('F:/projects/Projects/project02/myqrcode1.png')
result = decode(img)
print(result)
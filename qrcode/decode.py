from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('darkblue_qrcode.png'))
print(decocdeQR[0].data.decode('ascii'))

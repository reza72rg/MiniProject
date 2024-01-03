import segno

qrcode = segno.make_qr("I am reza latifi")
qrcode.save(
    "darkblue_qrcode.png",
    scale=10,
    dark="darkblue",
)

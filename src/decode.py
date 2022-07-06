from pyzbar.pyzbar import decode
import json
import zlib
 
import base45
import cbor2
from cose.messages import CoseMessage

# filename = "greenpass.jpeg"
# img = cv2.imread(filename)

def decodeQr(qrcode):
    # decode QR code into raw bytes:
    # qr_data_zlib_b45 = decode(img)[0].data.decode('utf-8')

    qr_data_zlib_b45 = qrcode
    
    # strip header ('HC1:') and decompress data:
    qr_data_zlib = base45.b45decode(qr_data_zlib_b45[4:])

    # decompress:
    qr_data = zlib.decompress(qr_data_zlib)

    # decode COSE message (no signature verification done)
    cose = CoseMessage.decode(qr_data)

    # decode the CBOR encoded payload and print as json
    dict = cbor2.loads(cose.payload)
    name_file = dict.get(-260).get(1).get("nam").get("gnt") + dict.get(-260).get(1).get("nam").get("fnt")
    with open(name_file.lower() + '_greenpass'+ '.json', 'w') as outfile:
        json.dump(cbor2.loads(cose.payload), outfile, indent=2)

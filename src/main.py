#import libraries
import cv2
from pyzbar import pyzbar

from decode import decodeQr

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        decodeQr(barcode_info)
        
    return frame

def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Greenpass reader', cv2.flip(frame, 1))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
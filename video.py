import cv2
import numpy as np
from pyzbar import pyzbar

# open video file
cap = cv2.VideoCapture('qrcode.mp4')

# check video exists or not
if (cap.isOpened() == False):
  print("Error opening video stream or file")


# read video frame by frame
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
      barcodes = pyzbar.decode(frame)
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break
      
      for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        
        
        cv2.imshow('qr code',frame)
  
  else:
    break

cap.release()

cv2.destroyAllWindows()



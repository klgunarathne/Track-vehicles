print("Hello world")
import cv2;
from pyzbar import pyzbar


img = cv2.imread("qr code.png", cv2.IMREAD_COLOR)

barcodes = pyzbar.decode(img)

# loop over the detected barcodes
for barcode in barcodes:
	(x, y, w, h) = barcode.rect
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type
	text = "{} ({})".format(barcodeData, barcodeType)
	cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)
	print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
 
cv2.imshow("qr code", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
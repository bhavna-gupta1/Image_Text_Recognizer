import cv2
from PIL import Image
import pytesseract as tess

camera = cv2.VideoCapture(0)

while True:
    _, image = camera.read()
    cv2.imshow('Text detection', image)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test1.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()


def tesseract():
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = 'test1.jpg'
    tess.tesseract_cmd = path_to_tesseract
    text = tess.image_to_string(Image.open(image_path))
    print(text[:-1])

tesseract()

import cv2
import pytesseract
import numpy as np

image_path = "images/img5.jpg"

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'


def image_preprocessing(image):
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(gray,0,255,type = cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # blur = cv2.GaussianBlur(threshold,(7,7),0)
    # kernel = np.ones((3, 3), np.uint8)
    # dilated = cv2.dilate(threshold, kernel, iterations=1)
    
    return threshold
    

def text_extractor(image):
    preprocessed_image = image_preprocessing(image)
    custom_config = r'--psm 1'
    extracted_text = pytesseract.image_to_string(preprocessed_image,config=custom_config).split("\n")
    extracted_text = [item for item in extracted_text if item]
    return extracted_text




# processed_image = image_preprocessing(image_path)

# extracted_text = text_extractor(image_path)
# print(type(extracted_text))
# print(extracted_text)
# cv2.imshow("Image",processed_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
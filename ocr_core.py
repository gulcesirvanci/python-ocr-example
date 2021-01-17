import cv2
import ocr_final


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = ocr_final(filename)
    #text = pytesseract.image_to_string()  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image

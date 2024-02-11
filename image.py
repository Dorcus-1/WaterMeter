import cv2
import pytesseract

# Path to Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

# Load the image
image_path = 'image_roi.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the text
_, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Perform OCR using Tesseract
text = pytesseract.image_to_string(threshold_image)

# Print the extracted text
print("Extracted Text:")
print(text)

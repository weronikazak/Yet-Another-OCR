import pytesseract
import cv2


def find_text(filename):
    img = cv2.imread(filename, 0)
    ret, gray = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(gray, lang="pol+eng")
    text = text.split("\n")
    r_text = []
    for line in text:
        if not line.isspace():
            if line != "\n":
                r_text.append(line)
    text = "\n".join(r_text[1:])
    return text.replace('|', "I")

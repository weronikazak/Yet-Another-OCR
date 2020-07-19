try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

def find_text(filename):
    text = pytesseract.image_to_stripng(Image.open(filename))

    return text

def change_to_png(filename):
    file_ext = filename.split(".")[-1]
    if file_ext.lower() is not "png":
        img = cv2.imread(filename)
        os.remove(filename)
        filename = filename[:-len(file_ext)] + "png"
        cv2.imwrite(filename, img)
    return filename
import cv2
import pytesseract


def ocr_final(filename):
    print("AAAa")
    img = cv2.imread(filename)
    img = cv2.cvtColor(filename, cv2.COLOR_BGR2RGB)

    resized = cv2.resize(img, (0, 0), fx=5, fy=5)

    # Detecting Words
    hImg, wImg, _ = resized.shape
    cong = r' --oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_data(resized)
    #print(boxes)

    a = ""
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(resized, (x, y), (w + x, h + y), (0, 250, 0), 3)
                cv2.putText(resized, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 250, 50), 2)
                a += b[11] + " "
    print(a)
    return a


# cv2.imshow('original', resized)
# cv2.waitKey()

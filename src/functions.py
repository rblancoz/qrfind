import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import base64
import os
from pyzbar.wrapper import ZBarSymbol


def decode_img_base64(img_base64):
    decoded_file = base64.b64decode(img_base64)
    img_arr3 = np.asarray(bytearray(decoded_file), dtype=np.uint8)

    im_cv2_3 = cv2.imdecode(img_arr3, 0)
    result = "--"

    if im_cv2_3 is not None:
        decodedObjects3 = decode(im_cv2_3)

        print(decodedObjects3)
        result = decodedObjects3[0].data
    else:
        print("Error decoding")

    return result


def decode(im):
    # Find barcodes and QR codes
    decoded_objects = pyzbar.decode(im, symbols=[ZBarSymbol.CODABAR, ZBarSymbol.DATABAR, ZBarSymbol.CODE128, ZBarSymbol.CODE39, ZBarSymbol.CODE93, ZBarSymbol.PDF417
                                                 ])

    # Print results
    for obj in decoded_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decoded_objects


def decode_img(img_path):
    # cwd = os.getcwd()
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # img_path = dir_path + '/barcode_img/label.png'
    # print(cwd)
    print(img_path)

    # Variante 1

    im_cv2_1 = cv2.imread(img_path)

    decodedObjects1 = decode(im_cv2_1)

    print("Variante 1")
    print(decodedObjects1)

    # Variante 2

    f = open(img_path, "rb")
    img_arr2 = np.asarray(bytearray(f.read()), dtype=np.uint8)
    f.close()

    im_cv2_2 = cv2.imdecode(img_arr2, 0)
    decodedObjects2 = decode(im_cv2_2)

    print("Variante 2")
    print(decodedObjects2)

    # Variante 3

    f3 = open(img_path, "rb")
    img_base64 = base64.b64encode(f3.read())
    f3.close()

    decoded_file = base64.b64decode(img_base64)
    img_arr3 = np.asarray(bytearray(decoded_file), dtype=np.uint8)

    im_cv2_3 = cv2.imdecode(img_arr3, 0)
    result = "--"

    if im_cv2_3 is not None:
        decodedObjects3 = decode(im_cv2_3)

        print("Variante 3")
        print(decodedObjects3)
        result = decodedObjects3[0].data
    else:
        print("Variante 3 Error")

    return result

import cv2
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images



imgs=load_images_from_folder('../src')

for im in imgs:
    cv2.imshow('<----brak zniżkia    zniżka--->',im)
    k = cv2.waitKey(0)
    if k == 81:
        print('Left')
    elif k == 83:
        print('Right')


import cv2
import os
from text_from_img import detect_text
import pandas as pd


def classfie(folder):
    idexes = []
    labels = []
    values = []
    i = 1
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))

        if img is not None:
            idexes.append(i)
            i = i + 1

            cv2.imshow('<----brak zniżkia    zniżka--->', img)

            values.append(detect_text(os.path.join(folder,filename)))
            k = cv2.waitKey(0)
            if k == 81:
                labels.append(False)

            elif k == 83:
                labels.append(True)

    print(values)
    print(labels)
    print(idexes)
    dat=pd.Series(values,index=idexes)
    res=pd.Series(labels,index=idexes)

    dic={'text':dat,'answer':res}

    return pd.DataFrame(dic)

classfie('src')
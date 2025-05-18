import glob
import os
import random

import cv2
import numpy as np
from PIL import Image


def npz(path, path2, split=False):
    test_num = 0
    train_num = 0
    if not os.path.exists(path2):
        os.makedirs(path2)

    for i, img_path in enumerate(glob.glob(path)):

        # 读入图像
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image=np.array(image)
        # image[image>0]=1
        # 读入标签
        label_path = img_path.replace('images', 'masks')

        # print(img_path)
        # print(label_path)
        if not os.path.exists(img_path):
            print(111)
        if not os.path.exists(label_path):
            print(222)
        label = cv2.imread(label_path, flags=0)
        label=np.array(label)
        label[label>0]=1
        # for i in label:
        #     print(i)
        # break
        path_save = path2
        if split:
            train2test = random.random()
            if train2test >= 0.85:
                path_save = path_save.replace('train_npz', 'test_vol_h5')
                if not os.path.exists(path_save):
                    os.makedirs(path_save)
                test_num += 1
            else:
                train_num += 1
        else:train_num+=1

        # 保存npz
        np.savez(path_save + str(i + 1), image=image, label=label)
        print('------------', i + 1)

    print('ok')
    print('train_num:', train_num)
    print('test_num', test_num)


if __name__ == "__main__":
    aiot = {
        'BUSI-256': {
            'train': {
                "path": r'D:\Visual studio\code\pycharm\TransUNet\data\BUSI-256\images\*.png',
                "path2": r'D:\Visual studio\code\pycharm\TransUNet\data\BUSI-256\train_npz\\'
            },
            'test': None
        },
        'isic2018': {
            'train': {
                "path": r'D:\Visual studio\code\pycharm\TransUNet\data\isic2018\train\images\*.png',
                "path2": r'D:\Visual studio\code\pycharm\TransUNet\data\isic2018\train\train_npz\\'

            },
            'test': {
                "path": r'D:\Visual studio\code\pycharm\TransUNet\data\isic2018\test\images\*.png',
                "path2": r'D:\Visual studio\code\pycharm\TransUNet\data\isic2018\test\test_vol_h5\\'
            }
        }
    }

    npz(aiot['BUSI-256']['train']['path'], aiot['BUSI-256']['train']['path2'], split=True)
    #npz(aiot['isic2018']['train']['path'],aiot['isic2018']['train']['path2'])
    #npz(aiot['isic2018']['test']['path'], aiot['isic2018']['test']['path2'])

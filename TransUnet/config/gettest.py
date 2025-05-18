import os
import shutil

dir='D:\Visual studio\code\pycharm\TransUNet\data\BUSI-256\masks'
list=r'D:\Visual studio\code\pycharm\TransUNet\TransUnet\lists\lists_BUSI-256\test_vol.txt'

with open(list,'r') as f:
    lists=f.readlines()
if not os.path.exists(dir.replace('masks','test')):
    os.mkdir(dir.replace('masks','test'))
for l in lists:
    l=l.rstrip()+'.png'
    shutil.copy(dir+'\\'+l,dir.replace('masks','test'))


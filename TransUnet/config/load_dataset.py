import os


def load_dataset(dir_data, path_txt):
    npzs = os.listdir(dir_data)
    if not os.path.exists(os.path.dirname(path_txt)):
        os.makedirs(os.path.dirname(path_txt))
    with open(path_txt, 'w', encoding='utf-8') as f:
        for npz in npzs:
            f.write(npz.split('.')[0]+'\n')


if __name__ == '__main__':
    aiot = {
        'BUSI-256': {
            'train': {
                'dir': r'D:\Visual studio\code\pycharm\TransUNet\data\BUSI-256\train_npz',
                'txt': r'D:\Visual studio\code\pycharm\TransUNet\TransUnet\lists\lists_BUSI-256\train.txt'
            },
            'test': {
                'dir': r'D:\Visual studio\code\pycharm\TransUNet\data\BUSI-256\test_vol_h5',
                'txt': r'D:\Visual studio\code\pycharm\TransUNet\TransUnet\lists\lists_BUSI-256\test_vol.txt'
            }
        },
        'isic2018': {
            'train': {
                'dir': r'D:\Visual studio\code\pycharm\TransUNet\data\isic2018\train\train_npz',
                'txt': r'D:\Visual studio\code\pycharm\TransUNet\TransUnet\lists\lists_isic2018\train.txt'
            },
            'test': {
                'dir': r'D:\Visual studio\code\pycharm\TransUNet\data\isic2018\test\test_vol_h5',
                'txt': r'D:\Visual studio\code\pycharm\TransUNet\TransUnet\lists\lists_isic2018\test_vol.txt'
            }
        }
    }
    load_dataset(aiot['BUSI-256']['train']['dir'],aiot['BUSI-256']['train']['txt'])
    load_dataset(aiot['BUSI-256']['test']['dir'], aiot['BUSI-256']['test']['txt'])
    load_dataset(aiot['isic2018']['train']['dir'], aiot['isic2018']['train']['txt'])
    load_dataset(aiot['isic2018']['test']['dir'], aiot['isic2018']['test']['txt'])

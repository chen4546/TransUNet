import json


def read_log(file_path):
    loss_avg=[]
    with open(file_path, 'r') as f:
        loss_total = f.readlines()
        for loss_epoch in loss_total:
            loss_epoch=json.loads(loss_epoch.replace("'",'"'))
            loss_avg.append(sum(loss_epoch["loss"])/len(loss_epoch["loss"]))
    with open(file_path.replace("loss.txt","loss_avg.txt"),"w")as f:
        for i in loss_avg:
            f.write(i.__str__())
            f.write('\r')



#read_log(r'D:\Visual studio\code\pycharm\TransUNet\model\TU_BUSI-256256\TU_pretrain_R50-ViT-B_16_skip3_epo100_bs6_256\loss.txt')
read_log(r'D:\Visual studio\code\pycharm\TransUNet\model\TU_isic2018256\TU_pretrain_R50-ViT-B_16_skip3_epo100_bs6_256\loss.txt')

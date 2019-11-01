<<<<<<< HEAD
# coding: utf-8
=======
# coding: shift_jis
>>>>>>> fb059716a8c240ce15c6ce135a249be77fb3b230
import json
from domains.getSuidoNet import getSuidoNet

def paymentSummary():

    #jsonファイルディレクトリ
    input_json = 'C:\\Users\\spdc3\\OneDrive\\デスクトップ\payment_summary\\json\\account.json'

    with open (input_json) as f:
        json_dict = json.load(f)

    #各サイトのスクレイピング
    for i,d in enumerate(json_dict):
        domain = json_dict[i]['domain']
        url = json_dict[i]['url']
        id = json_dict[i]['id']
        password = json_dict[i]['pass']

        #水道ネット
        if domain == 'suidonet':
            target_date,receipt_amount = getSuidoNet(url,id,password)
            print('対象年月:{}'.format(target_date))
            print('領収金額:{}'.format(receipt_amount))

<<<<<<< HEAD

=======
>>>>>>> fb059716a8c240ce15c6ce135a249be77fb3b230

paymentSummary()

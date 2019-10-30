import sys
import json

def paymentSummary():

    #jsonファイルディレクトリ
    input_json = 'C:\\Users\\spdc3\\OneDrive\\デスクトップ\\payment_summary\\json\\account.json'

    with open (input_json) as f:
        json_dict = json.load(f)

    #各サイトのスクレイピング
    for i,d in enumerate(json_dict):
        domain = json_dict[i]['domain']
        #水道ネット
        if domain == 'suidonet':
            print()
        #マイガス
        elif domain == 'suidonet':
            print()
        #スマ電
        elif domain == 'suidonet':
            print()
        else:
            print()
        # url = json_dict[i]['url']
        # id = json_dict[i]['id']
        # password = json_dict[i]['pass']
        # print(url)
        # print(id)
        # print(password)

paymentSummary()

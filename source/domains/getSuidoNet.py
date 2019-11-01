# coding: utf-8
import requests
import datetime

def getSuidoNet(url,id,password):
    now = datetime.datetime.now()
    # response = requests.get(url)
    print(url)
    #
    # print(response)
    # # <Response [200]>
    #
    # print(type(response))
    # # <class 'requests.models.Response'>

    target_date = '{0:%Y%m}'.format(now)
    receipt_amount = 0
    return target_date,receipt_amount

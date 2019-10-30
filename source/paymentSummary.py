import sys
import json

def main():

    input_json = 'C:\\Users\\spdc3\\OneDrive\\デスクトップ\\payment_summary\\json\\account.json'

    with open (input_json) as f:
        json_dict = json.load(f)

    for i,d in enumerate(json_dict):
        url = json_dict[i]['url']
        id = json_dict[i]['id']
        password = json_dict[i]['pass']
        print(url)
        print(id)
        print(password)

main()

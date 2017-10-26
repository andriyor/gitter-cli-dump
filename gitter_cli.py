import json
import argparse
import os
import sys

import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, help='Personal OAuth Gitter token; or use GITTER_TOKEN env var')
    parser.add_argument('--room', type=str, help='list - retrieve rooms and IDs', choices=['list'])
    parser.add_argument('--dump', type=str, help='get all messages from room please specify "id <room_id>')
    args = parser.parse_args()

    if args.token:
        token = args.token
    else:
        token = os.environ.get('GITTER_TOKEN')

    if token:
        if args.room == "list":
            get_room_list(token)
        if args.dump:
            get_all_messages(token, args.dump)
    else:
        print('Please specify token via "--token <token>" or GITTER_TOKEN environment variable')


def get_messages(token, before_id, room_id):
    api_chat_messages = 'https://api.gitter.im/v1/rooms/{}/chatMessages'.format(room_id)
    chat_params = {'access_token': token, 'limit': 100, 'beforeId': before_id}
    messages = requests.get(api_chat_messages, params=chat_params)
    return messages.json()


def get_all_messages(token, room_id):
    messages = []
    before_id = None
    while True:
        mes = get_messages(token, before_id, room_id)
        if not mes:
            break
        messages.extend(mes)
        before_id = mes[0]['id']
        sys.stderr.write('.')
        sys.stderr.flush()
    sys.stdout.write(json.dumps(messages, ensure_ascii=False, indent=4))


def get_room_list(token):
    url_list_rooms = 'https://api.gitter.im/v1/rooms'
    rooms_params = {'access_token': token}
    rooms_list = requests.get(url_list_rooms, params=rooms_params)
    for i in rooms_list.json():
        print(i['id'], i['name'])


if __name__ == '__main__':
    main()

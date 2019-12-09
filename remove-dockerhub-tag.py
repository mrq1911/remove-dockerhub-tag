#!/usr/bin/python3.6
import requests
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--user', required=True, help='dockerhub username')
parser.add_argument('--password', required=True, help='dockerhub password')
parser.add_argument('image', nargs='+', help='org/image:tag')
args = parser.parse_args()

login = {"username": args.user, "password": args.password}
token = requests.post("https://hub.docker.com/v2/users/login/", data = login).json()['token']

p = re.compile('(.+)\/(.+):(.+)')
for image in args.image:
    m = p.match(image)
    if not m:
        print('invalid image indetifier "{}"'.format(image))
    else:
        org = m.group(1)
        name = m.group(2)
        tag = m.group(3)
        r = requests.delete(f'https://hub.docker.com/v2/repositories/{org}/{name}/tags/{tag}/', headers={"Authorization": f'JWT {token}'})
        if r.status_code == 200:
            print(f'tag removed: {image}')
        else:
            print(f'failed to remove tag "{image}": {r.text}')

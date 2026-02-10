#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        r_json = r.json()
        for i in r_json:
            print(i['title'])


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        keys = ['id', 'title', 'body']
        with open('posts.csv', mode='w', encoding='utf-8') as file:
            file_writes = csv.DictWriter(file, fieldnames= keys, extrasaction='ignore')
            file_writes.writeheader()
            file_writes.writerows(posts)

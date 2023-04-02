from exceptions import RequestFailedException
from useful_methods import write_list_to_file
from plugin import Plugin
import requests
import json


class DummyApiPlugin(Plugin):
    def __init__(self, api_key):
        self.api_key = api_key

    def connectivity_test(self):
        api_url = 'https://dummyapi.io/data/v1/user'
        headers = {'app-id': self.api_key}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            raise RequestFailedException(response.status_code)

    def collect(self):
        self.collectUsers()
        self.collectPosts()

    def collectUsers(self):
        all_users_list = []
        base_url = 'https://dummyapi.io/data/v1/user'
        headers = {'app-id': self.api_key}
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            raise RequestFailedException(response.status_code)
        total_pages = response.json()['totalPages']

        for page in range(total_pages):
            url = f'{base_url}?page={page}&limit=20'
            headers = {'app-id': self.api_key}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                raise RequestFailedException(response.status_code)
            users = response.json()['data']
            all_users_list.extend(users)

        write_list_to_file('users.json', all_users_list)

    def collectPosts(self):
        all_posts_list = []
        base_url = 'https://dummyapi.io/data/v1/post?limit=50'
        headers = {'app-id': self.api_key}
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            raise RequestFailedException(response.status_code)
        posts = response.json()['data']

        for post in posts:
            post_id = post['id']
            url = f'https://dummyapi.io/data/v1/post/{post_id}/comment'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                raise RequestFailedException(response.status_code)
            comments = response.json()['data']
            post['comments'] = comments
            all_posts_list.append(post)

        write_list_to_file('posts_includes_comments.json', all_posts_list)

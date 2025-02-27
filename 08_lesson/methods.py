import requests


class Projects:
    def __init__(self, base_url):
        self.base_url = base_url
        self.base_url = 'https://ru.yougile.com'

    def authorization(self):
        my_headers = {"Authorization": "здесь токен"}
        return my_headers

    def get_list(self):
        resp = requests.get(f'{self.base_url}/api-v2/projects',
                            headers=self.authorization())
        return resp.json()

    def positive_create_project(self, title='', users=None):
        users = {"2836faf7-0371-48b4-b504-23dc900eaa1d": "admin"}
        body = {
                "title": title,
                "users": users
                }
        resp = requests.post(f'{self.base_url}/api-v2/projects',
                             headers=self.authorization(), json=body)
        return resp.json()

    def negative_create_project(self, title='', users=None):
        users = {"2836faf7-0371-48b4-b504-23dc900eaa1d": "admin"}
        body = {
                "title": title,
                "users": users
                }
        resp = requests.post(f'{self.base_url}/api-v2/projects', json=body)
        return resp.json()

    def change_project(self, id, title=''):
        body = {
                "title": title
               }
        resp = requests.put(f'{self.base_url}/api-v2/projects/{id}',
                            headers=self.authorization(), json=body)
        return resp.json()

    def get_by_id(self, id):
        resp = requests.get(f'{self.base_url}/api-v2/projects/{id}',
                            headers=self.authorization())
        return resp.json()

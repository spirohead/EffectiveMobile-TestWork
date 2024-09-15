import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Получение переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
GITHUB_API_URL = 'https://api.github.com'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def create_repo():
    url = f'{GITHUB_API_URL}/user/repos'
    payload = {
        'name': REPO_NAME,
        'description': 'This is a test repository',
        'private': False
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f'Repository {REPO_NAME} created successfully.')
    else:
        print(f'Failed to create repository: {response.json()}')


def show_repos():
    url = f'{GITHUB_API_URL}/user/repos'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]
        if REPO_NAME in repo_names:
            print(f'Repository {REPO_NAME} exists.')
        else:
            print(f'Repository {REPO_NAME} does not exist.')
    else:
        print(f'Failed to list repositories: {response.json()}')


def delete_repo():
    url = f'{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Repository {REPO_NAME} deleted successfully.')
    else:
        print(f'Failed to delete repository: {response.json()}')


if __name__ == '__main__':
    show_repos()
    create_repo()
    show_repos()
    delete_repo()
    show_repos()

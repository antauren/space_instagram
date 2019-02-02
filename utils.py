import requests
import os


def download_file(url, path):
    response = requests.get(url)

    if not response.ok:
        print('Ошибка:', response.status_code)
        return None

    with open(path, 'wb') as file:
        file.write(response.content)

    return True


def get_files_path_from_dir(path):
    for root, _, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)

import requests
import os


def download_file(url, path):
    response = requests.get(url)

    if not response.ok:
        response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)

    return True


def get_ext(path):
    return os.path.splitext(path)[-1]


def get_files_path_from_dir(path):
    for root, _, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)

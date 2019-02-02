import os
import requests

from utils import download_file


def fetch_spacex_last_launch(dir_path):
    os.makedirs(dir_path, exist_ok=True)

    response = requests.request('GET', 'https://api.spacexdata.com/v3/launches/latest')

    images_urls = response.json()['links']['flickr_images']

    for num, url in enumerate(images_urls):
        ext = os.path.splitext(url)[-1]
        path = os.path.join(dir_path, 'spacex_{}{}'.format(num, ext))

        download_file(url, path)

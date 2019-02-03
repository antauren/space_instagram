import os
import requests

from utils import download_file, get_ext


def fetch_hubble_collection(collection, dir_path):
    for image_id in get_collection_ids(collection):
        fetch_hubble_image(image_id, dir_path)


def get_collection_ids(collection):
    params = {'collection_name': collection,
              'page': 'all'}

    response = requests.request('GET', 'http://hubblesite.org/api/v3/images/', params=params)

    for i in response.json():
        yield i['id']


def fetch_hubble_image(image_id, dir_path):
    os.makedirs(dir_path, exist_ok=True)

    response = requests.request('GET', 'http://hubblesite.org/api/v3/image/{}'.format(image_id))

    file_url = response.json()['image_files'][-1]['file_url']

    ext = get_ext(file_url)
    path = os.path.join(dir_path, 'hubble_img_{}{}'.format(image_id, ext))

    download_file(file_url, path)


if __name__ == '__main__':
    fetch_hubble_collection('wallpaper', 'images')

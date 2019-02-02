from dotenv import get_variables

from instabot import Bot

from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_image, fetch_hubble_collection

from utils import get_files_path_from_dir

if __name__ == '__main__':
    dir_path = 'images'

    # скачиваем файлы
    fetch_hubble_collection('wallpaper', dir_path)
    fetch_spacex_last_launch(dir_path)
    fetch_hubble_image(image_id=67, dir_path=dir_path)

    image_files = get_files_path_from_dir(dir_path)

    variables = get_variables('.env')

    bot = Bot()
    bot.login(username=variables['USERNAME'], password=variables['PASSWORD'])

    # загружаем файлы
    for file in image_files:
        bot.upload_photo(file)

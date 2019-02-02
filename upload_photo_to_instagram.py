from dotenv import get_variables

from instabot import Bot

from utils import get_files_path_from_dir, get_ext

IMG_EXT_SET = {'.png', '.jpg', '.jpeg', '.gif', '.tif'}


def upload_photo_to_instagram(img_dir):
    files = get_files_path_from_dir(img_dir)

    image_files = filter(lambda path: get_ext(path).lower() in IMG_EXT_SET, files)

    variables = get_variables('.env')

    bot = Bot()
    bot.login(username=variables['USERNAME'], password=variables['PASSWORD'])

    for img in image_files:
        bot.upload_photo(img)

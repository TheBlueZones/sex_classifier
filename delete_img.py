import os
import shutil

# 修改为你的男性和女性图片文件夹路径
male_images_path = 'male_images'
female_images_path = 'female_images'

# 限制的图片数量
image_limit = 2000

# 删除男性图片
male_images = os.listdir(male_images_path)
for image in male_images[image_limit:]:
    os.remove(os.path.join(male_images_path, image))

# 删除女性图片
female_images = os.listdir(female_images_path)
for image in female_images[image_limit:]:
    os.remove(os.path.join(female_images_path, image))

print(f'已删除多余的图片，现在每个文件夹只剩下 {image_limit} 张图片')

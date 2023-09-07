import os
import shutil
from tqdm import tqdm
import time

# 修改为你的CelebA数据集图片和list_attr_celeba.txt文件所在路径
celeba_images_path = 'img_align_celeba'
attr_file_path = 'list_attr_celeba.txt'

# 修改为你创建的男性和女性图片文件夹路径
male_images_path = 'male_images'
female_images_path = 'female_images'

# 如果文件夹不存在，则创建文件夹
os.makedirs(male_images_path, exist_ok=True)
os.makedirs(female_images_path, exist_ok=True)

# 读取list_attr_celeba.txt文件
with open(attr_file_path, 'r') as f:
    lines = f.readlines()

# 记录开始时间
start_time = time.time()

# 跳过前两行（文件头和列名）
# 使用tqdm包装循环以显示进度条
for line in tqdm(lines[2:], ncols=100, desc="处理图片", unit="张"):
    tokens = line.strip().split()
    image_name = tokens[0]
    gender = int(tokens[21])  # 21是性别属性的列索引

    # 根据性别将图片复制到对应的文件夹
    src_path = os.path.join(celeba_images_path, image_name)
    if gender == 1:
        dest_path = os.path.join(male_images_path, image_name)
    else:
        dest_path = os.path.join(female_images_path, image_name)
    shutil.copy(src_path, dest_path)

# 计算耗时
elapsed_time = time.time() - start_time

print('图片分类完成')
print(f'总耗时: {elapsed_time:.2f} 秒')

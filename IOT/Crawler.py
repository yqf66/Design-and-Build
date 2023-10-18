import requests
import os
import time

# 文件保存目录
download_folder = r'C:\Users\86166\Desktop\DSS'

# 确保目标文件夹存在
os.makedirs(download_folder, exist_ok=True)

# 定义目标网站的URL
url = 'http://www.hepou.com/images/2020/08/imagebaidu-1024x502.jpg'

# 初始化图片编号计数器
image_count = 0

# 每隔一秒刷新一次网页并重新爬取图片
while True:
    # 发送HTTP请求并获取图片内容
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 提取文件名并添加编号
        img_name = f"{image_count + 1}.jpg"

        # 将图片内容保存到文件夹
        with open(os.path.join(download_folder, img_name), 'wb') as img_file:
            img_file.write(response.content)
        print(f"第 {image_count + 1} 张图片下载成功")

        # 增加图片编号计数器
        image_count += 1

    else:
        print("无法下载图片，状态码:", response.status_code)

    # 暂停一秒
    time.sleep(1)

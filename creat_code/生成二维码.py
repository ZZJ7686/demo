from PIL import Image
import qrcode
import os
import sys
import time

# # 简易版二维码生成
# img = qrcode.make('https://github.com/ZZJ7686')
# img.show()

# 复杂点的
def creat_code(url):
    QRImagePath = os.getcwd() + '/qrcode.png'  # 临时存储位置
    # 设置图片格式
    qr = qrcode.QRCode(
        version=1,# 格子矩阵大小 1-40
        error_correction=qrcode.constants.ERROR_CORRECT_H,#错误容错率L7%，M115%,Q25%,H30%
        box_size=10,# 每格包含的像素数量
        border=2,#二维码到边框的空白小格子数，默认4，
    )

    # data = input()  # 运行时输入数据
    qr.add_data(url) #添加数据
    qr.make(fit=True)# fit参数为True，二维码自动调整大小
    # 生成图片
    img = qr.make_image(fill_color="#008988")
    # 添加logo图片并打开
    icon = Image.open("aj.jpg")
    # 获取二维码图片宽高
    img_w,img_h = img.size
    # 设置logo的大小和图片各个参数
    factor = 5
    size_w = int(img_w/factor)
    size_h = int(img_h/factor)
    icon_w,icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重置logo图片大小
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    #获取logo坐标位置
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    #组合二维码和logo
    img.paste(icon, (w, h), mask=None)
    img.save('qrcode.png')  # 保存图片
    """检测当前系统平台返回值 以下是各系统的
    Linux (2.x and 3.x) 'linux2'
    Windows 'win32'
    Windows/Cygwin 'cygwin'
    Mac OS X 'darwin'
    OS/2 'os2'
    OS/2 EMX 'os2emx'
    RiscOS 'riscos'
    AtheOS 'atheos'"""
    if sys.platform.find('darwin') >= 0:
        os.system('open %s' % QRImagePath)

    elif sys.platform.find('linux') >= 0:
        os.system('xdg-open %s' % QRImagePath)
    else:
        os.system('call %s' % QRImagePath)

    time.sleep(5)  # 系统等待5秒
    os.remove(QRImagePath)  # 删除图片

creat_code('https://github.com/ZZJ7686')




# 验证码生成库
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
from PIL import Image
import random
import sys
#生成数字0-9 
number = ['0','1','2','3','4','5','6','7','8','9']
#生成小写字母a-z
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 生成大写字母A-Z
# ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def random_captcha_text(char_set=number, captcha_size=4):
    # 验证码列表
    captcha_text = []
    for i in range(captcha_size):
        #随机选择
        c = random.choice(char_set)
        #加入验证码列表
        captcha_text.append(c)
    return captcha_text
 
# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    #获得随机生成的验证码
    captcha_text = random_captcha_text()
    #把验证码列表转为字符串
    captcha_text = ''.join(captcha_text)
    #生成验证码
    captcha = image.generate(captcha_text)
    #文件存入的位置以及文件的标注
    # 文件异常做判断处理
    image.write(captcha_text, '/Users/haitao/Desktop/CNN/captcha/images/' + captcha_text + '.jpg')  #

#数量少于10000，因为重名
num = 10000
if __name__ == '__main__':
    for i in range(num):
        gen_captcha_text_and_image()
        sys.stdout.write('\r>> Creating image %d/%d' % (i+1, num))
        sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()
    print("生成完毕")
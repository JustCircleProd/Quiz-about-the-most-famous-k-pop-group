from simple_image_download import simple_image_download as simp
import requests

def download(query, limit):
    response = simp.simple_image_download()
    response.download(query, limit)

names = ('Kim Nam Joon', 'Kim Seok Jin', 'Min Yoon Gi', 'Jung Ho Seok', 'Park Ji Min', 'Kim Tae Hyung', 'Jeon Jung Kook')

try:
    for name in names:
        download(name, 100)
except Exception as e:
    print(e)
else:
    print('Success')


from simple_image_download import simple_image_download as simp
import os
import requests

def download(query, limit):
    response = simp.simple_image_download()
    response.download(query, limit)
    
    return response.urls(query, limit)


names = ('Kim Nam Joon', 'Kim Seok Jin', 'Min Yoon Gi', 'Jung Ho Seok', 'Park Ji Min', 'Kim Tae Hyung', 'Jeon Jung Kook')

for name in names:
    download(name, 100)

if os.path.isdir(os.path.join(os.getcwd(), 'simple_images')):
    print("Success")

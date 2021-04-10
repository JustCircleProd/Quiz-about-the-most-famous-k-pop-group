import os

try:
    base_path = os.path.join(os.getcwd(), 'simple_images')
    for name in os.listdir(base_path):
        os.rename(os.path.join(base_path, name), os.path.join(base_path, name.replace('_', ' ')))
except:
    print("Error")
else:
    print("Success")
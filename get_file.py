import os
from glob import glob

path = r"D:\LCJ\img_data\fastimg\SV-2_20220723_L2A0000176260_1012201670020003"
pan_img = r''
ms_img = r''

files = glob(path + '/*.tiff')
files_list = []
for file in files:
    size = os.path.getsize(file)
    files_list.append([file, size])

files_list.sort(key=lambda x: x[1], reverse=True)
for [file, size] in files_list:
    print(file)


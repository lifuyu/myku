#coding=utf-8
#convert tiff to jpg
#just choose the general folder
import tkinter.filedialog as filedialog
import os
from PIL import Image

folderPath = filedialog.askdirectory(title = "请选择图库文件夹")

for root, dirs, files in os.walk(folderPath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".png":
            outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
            try:
                im = Image.open(os.path.join(root, name)).convert('RGBA')
                r,g,b,a=im.split()
                im=Image.merge("RGB",(r,g,b)) #若没有这两行，会错误。png图像有RGBA四个通道，而BMP、JPG图像只有RGB三个通道，所以PNG转BMP、JPG时候程序不知道A通道怎么办，就会产生错误。
                print ("Generating jpeg for %s" % name)
          
                im.save(outfile, "JPEG", quality=100)
            except Exception as e:
                print (e)

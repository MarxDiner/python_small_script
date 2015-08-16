# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Idea\.spyder2\.temp.py
"""


import Image  
import glob, os  

 #图片批处理  
def timage():  
     #find jpgs
     for files in glob.glob('D:\\1\\*.JPG'):  
         filepath,filename = os.path.split(files)  
         filterame,exts = os.path.splitext(filename)  
         #输出路径  
         opfile = r'D:\\22\\'  
         #判断opfile是否存在，不存在则创建  
         if (os.path.isdir(opfile)==False):  
             os.mkdir(opfile)  
         im = Image.open(files)  
         w,h = im.size  
         im_ss = im.resize((400,h*400/w))  
         #im_ss = im.convert('P')  
         #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
         im_ss.save(opfile+filterame+'.jpg')  

if __name__=='__main__':  
     timage()  

     print 'all right!'
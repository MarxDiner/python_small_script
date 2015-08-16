# -*- coding: utf-8 -*-
"""
this script can get CurrentPath and find jpgs in the folder 
what you should do is:
      1.create a folder under your current path named 1 like \usr\1
      2.put all the jpgs in the folder
      3.then run the script and wait
           
"""


import Image  
import glob, os  

 #图片批处理  
def timage():  
     CurrentPath = os.getcwd()    
     print CurrentPath   
     print CurrentPath+'1\*.JPG'
    #find jpgs
     for files in glob.glob(CurrentPath+'1\*.JPG'):  
         filepath,filename = os.path.split(files)  
         filterame,exts = os.path.splitext(filename)  
         #输出路径  

         opfile =CurrentPath+ '\\22\\'  
         #判断opfile是否存在，不存在则创建  
         if (os.path.isdir(opfile)==False):  
             os.mkdir(opfile)  
         im = Image.open(files)  
         w,h = im.size  
         im_ss = im.resize((400,h*400/w))  #400*n
         #im_ss = im.convert('P')  
         #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
         im_ss.save(opfile+filterame+'.jpg')  



if __name__=='__main__':  
     timage()  

     print 'all right!'
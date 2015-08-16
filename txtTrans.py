# -*- coding: cp936 -*-
import os
import sys

def txtTrans(filepath_in,filepath_out):
	txt_withFormat=open(filepath_in,'r')
	txt_withHtml=open(filepath_out,'w')
	txt_withHtml.write('<meta http-equiv="content-type" content="text/html;charset=utf-8">')
	while (True):
	    paragraph=txt_withFormat.readline()  #will get the text and '\n' if have
	  #  print paragraph
	    if len(paragraph) > 1:
	       paragraph=paragraph.decode('utf8')
	       #print paragraph[-2]
	       if paragraph[-2]=='s':
	          temp='<p style="white-space: normal; text-align: center;"><strong><span style="font-family:  SimHei; font-size: 20px;">'.decode('utf8')+paragraph[0:-2]+'</span></strong></p>'
	       elif paragraph[-2]=='t':
	          temp='<table cellpadding="0" cellspacing="0"><tbody><tr><td style="padding: 0px 7px; word-break: break-all;" valign="top" width="568"></td></tr><tr><td style="padding: 0px 7px; word-break: break-all;" valign="top" width="568"><p style="text-align: center;">xxxxx</p></td></tr></tbody></table>'
	       else:
	          temp='<p style="white-space: normal; text-indent: 2em; line-height: 1.5em;"><span style="">'+paragraph+'</span></p>'
	    
	       txt_withHtml.write(temp)	


	    elif (paragraph==''):
                 # print paragraph.decode('utf8')
	       #print temp	
	       break
	txt_withFormat.close()
	txt_withHtml.close()
if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding('utf8')
	txtTrans("D:\\a.txt","D:\\b.html")
 	print 'OK!'
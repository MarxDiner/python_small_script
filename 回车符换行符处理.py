'''
there is a diffrence between Windows and Linux in how
to deal with a paragraph.
For Windows,every paragraph will end with a '\n' and '\t'
But for Linux, every paragraph will just end with a '\n' 
it's very important to make it clear if you want to deal with strings in both os
(ps:carriage return(\n) and linefeed(\r) character)
'''
import os
 
def replace(filePath, w2u):
  try:
    oldfile = open(filePath, "rb+")     #这里必须用b打开
    path, name = os.path.split(filePath)
    newfile = open(path + '$' + name, "ba+")
     
    old = b''
    new = b''
    if w2u == True:
      old = b'\r'
      new = b''
    else:
      old = b'\n'
      new = b'\r\n'
 
    data = b''
    while (True):
      data = oldfile.read(200)
      newData = data.replace(old, new)
      newfile.write(newData)
      if len(data) < 200:
        break
    newfile.close()
    oldfile.close()
     
    os.remove(filePath)
    os.rename(path + '$' + name, filePath)
  except IOError as e:
    print(e)
     
if __name__ == "__main__":
  print("请输入文件路径：")
  filePath = input()
  replace(filePath, False)  #这个改为True就可以实现\n变成\r\n
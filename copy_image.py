#wap to copy an image into a file
f1=open('cat.jpg','rb')
f2=open('new.jpg','wb')

bytes=f1.read()
f2.write(bytes)
f1.close()
f2.close() #it will copy the image file cat.jpg into another neew  file new.jpg



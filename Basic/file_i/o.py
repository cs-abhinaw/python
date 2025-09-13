# f=open("k.txt")
# data=f.read()
# print(data)
# f.close()

#to write in a file
st="print('i love you baby') "
f=open("abhi1.py","w")
f.write(st)
f.close()
#by using with satatement we dont need to close the file

with open("file.txt","w") as f :
    f.write("hey")
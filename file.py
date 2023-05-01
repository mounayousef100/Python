# w / a / r / r+ للكتابة و للاضافة باخر الملف و للقراءة و للقراءة و الكتابة معا 
# w/w+ بمسحو كل شي و بيكتبو 
# /n لحتى تنزل سطر جديد مع ال a
files = open("text.txt","r+")
for x in files.readlines():
    print(x)
files.read()
files.close()
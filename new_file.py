import os

print(os.getcwd())

os.mkdir("files")
os.chdir("files")

print(os.getcwd())

for i in range(10):
    os.mkdir("file" + str(i))

print(os.path.isfile("files/file5/book.txt"))

os.chdir("files")
for i in range(7,10):
    direct_name = "file" + str(i)
    os.rmdir(direct_name)



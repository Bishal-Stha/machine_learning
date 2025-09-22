import os

allFiles = os.listdir()
for num,filename in enumerate(allFiles):
    print(f"{num+1}. {filename}")


print(os.getcwd())                
print(os.path.exists("hello.txt")) 
print(os.path.abspath("hello.txt"))

# with open("old.txt","w") as f:
#     f.write("Old is gold.")
# os.rename("old.txt", "new.txt")   # rename
# os.remove("new.txt")             # delete
os.mkdir("new_folder")            # create folder
os.rmdir("new_folder")            # remove folder

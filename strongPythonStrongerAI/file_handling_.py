import os

folder_name = "test_files"
file_list = os.listdir(folder_name)
print(file_list)

text = ""
for file in file_list:
    with open(f"{folder_name}/{file}","r") as f:
        content = f.read()
        text = text + content

with open(f"{folder_name}/Nepal.txt","x") as F:
    F.write(text)


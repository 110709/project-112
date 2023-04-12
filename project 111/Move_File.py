import os
import shutil

from_dir="C:/Users/avika/Downloads"
to_dir="C:/Whitehat"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
  name,extension = os.path.splitext(file_name)
  #print(name)
 # print(extension)

  if extension == '':
    continue
  if extension in  [ '.txt', '.doc', '.docx', '.pdf']:

    path_1= from_dir +'/' + file_name
    path_2= from_dir +'/' + "Document_Files"
    path_3= from_dir +'/' + "Document_Files"+'/'+ file_name
    print(path_1)
    print(path_2)
    print(path_3)

    if os.path.exists(path_2):
      print("Moving" + file_name + ".....")

      shutil.move(path_1,path_2)

    else:
      os.makedirs(path_2)
      print("Moving" + file_name + "....")
      shutil.move(path_1,path_3)



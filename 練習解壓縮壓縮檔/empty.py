# import zipfile

# # # 這樣的話research.zip裡面就有2個txt檔按了 這是做壓縮的
# # zipped_file = zipfile.ZipFile("research.zip" , "w")
# # zipped_file.write("research.txt", compress_type=zipfile.ZIP_DEFLATED)
# # zipped_file.write("research2.txt", compress_type=zipfile.ZIP_DEFLATED)
# # zipped_file.close()

#########################################################################################################################

# import zipfile

# # 解壓縮 解壓縮那個檔案 然後都放在result這個檔案
# zipped_object = zipfile.ZipFile("research.zip", "r")
# zipped_object.extractall("result")
# zipped_object.close()

#########################################################################################################################

## 整個檔案壓縮
# import shutil

# folder_we_want_to_zip = "C:\\Users\\MIS01\\Desktop\\pythonooxx\\Zippt"
# output_name = "C:\\Users\\MIS01\\Desktop\\pythonooxx\\Zippt\\output"

# shutil.make_archive(output_name, "zip" , folder_we_want_to_zip)

#########################################################################################################################

## 壓縮檔用出來

import shutil

folder_we_want_to_unzip = "C:\\Users\\MIS01\\Desktop\\pythonooxx\\Zippt\\output.zip"
unzip_folder_name = "C:\\Users\\MIS01\\Desktop\\unzipfolder"

shutil.unpack_archive(folder_we_want_to_unzip, unzip_folder_name , "zip")

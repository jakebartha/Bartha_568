# # Create the directory where we will dump these folders
# root_path = "D:\Empty_Dir"
# os.mkdir(root_path)
#
# # Now make folders
# first_level = ["draft_code", "includes", "layouts", "site"]
#
# for folder in first_level:
#     # I am using os.path.join to join my folders
#     os.mkdir(os.path.join(root_path, folder))
#
# # Same again, for draft code folders
# second_level = ["pending", "complete"]
#
# for folder in second_level:
#     # I am using os.path.join to join my folders
#     os.mkdir(os.path.join(root_path, "draft_code", folder))
# 

#
# # delete all folders, find by Googling "delete files and folders python"
# import shutil
# shutil.rmtree(root_path)
# Part1 #1 making simple directory
import os
# os.system('dir')
path = r"C:\NRS568_Bartha_workfolder"
#
# os.mkdir(path + "/draft_code")
# os.mkdir(path + "/draft_code/pending")
# os.mkdir(path + "/draft_code/complete")
# os.mkdir(path + "/includes")
# os.mkdir(path + "/layouts")
# os.mkdir(path + "/layouts/default")
# os.mkdir(path + "/layouts/post")
# os.mkdir(path + "/layouts/post/posted")
# os.mkdir(path + "/site")

# os.rmdir(path + "/site")
# os.rmdir(path + "/layouts/post/posted")
# os.rmdir(path + "/layouts/post")
# os.rmdir(path + "/layouts/default")
# os.rmdir(path + "/layouts")
# os.rmdir(path + "/includes")
# os.rmdir(path + "/draft_code/complete")
os.rmdir(path + "/draft_code/pending")
os.rmdir(path + "/draft_code")
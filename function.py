import shutil
import os
import hashlib

import logging


logging.basicConfig(
    level=logging.INFO,
    filename="log_file.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
)

# def get_hash_md5(filename):
#     """function get hash sum object"""
#     with open(filename, "rb") as f:
#         hash_object = hashlib.md5(f.read())
#         return hash_object.hexdigest()



def create_folder(path_to_storage, device_id):
    """function create folder device_id""" 
    if not os.path.isdir(f'{path_to_storage}\\{device_id}'):
        os.mkdir(f'{path_to_storage}\\{device_id}')
        print(f'Folder {device_id} created successfully')

    else:
        print(f"Folder {device_id} exists")   
   
    

def get_new_file_name(file_name):
    """function get new file name""" 
    list_name = (file_name.split("_"))
    year = list_name[1][6:10]
    month = list_name[1][10:12]
    day = list_name[1][12:14]
    time = list_name[1][14:20]
    new_file_name = f"{list_name[0]}_{year}_{month}_{day}_{time}_{list_name[-1]}"
    return new_file_name

def create_folder_date(hdd_storage, device_id, new_file_name):
    """function create folder date"""
    year = new_file_name.split("_")[1]
    month = new_file_name.split("_")[2]
    """create folder year"""
    if not os.path.isdir(f'{hdd_storage}\\{device_id}\\{year}'):
        os.mkdir(f'{hdd_storage}\\{device_id}\\{year}')
        print(f"Folder year {year} create successfully")
        logging.info(f"Folder year {year} create successfully")

    """create folder month"""
    if not os.path.isdir(f'{hdd_storage}\\{device_id}\\{year}\\{month}'):
        os.mkdir(f'{hdd_storage}\\{device_id}\\{year}\\{month}')
        print(f"Folder year {month} create successfully")
        logging.info(f"Folder year {month} create successfully")

    else:
        logging.info("folder date exists")


def copy_video(hdd_storage, file_path, file_name, device_id, new_file_name, year, month):  
    """function copy video file""" 
    try:
        logging.info(file_name)
        shutil.copy((file_path + "\\" + file_name),
                    f'{hdd_storage}\\{device_id}\\{year}\\{month}\\{new_file_name}')
        logging.info("func copy_video: True")
        os.remove(file_path + "\\" + file_name)
        
    except Exception as ex:
        logging.info(f"func copy_video:{ex}")    

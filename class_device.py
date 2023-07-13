# import os
import psutil
# import shutil
# import hashlib
# import logging


# logging.basicConfig(
#     level=logging.INFO,
#     filename="log_file.log",
#     filemode="a",
#     format="%(asctime)s %(levelname)s %(message)s",
# )

# hdd = "D:\\storage\\"


class Device:
    
    def __str__(self):
        return(Device.__name__)
 




    # """metod create folder device_id"""  
    # def create_folder(self):
    #     if not os.path.isdir(hdd + self.device_id):
    #         os.mkdir(hdd + self.device_id)
    #     else:
    #         print(f"Folder {self.device_id} exists")
    #         logging.info(f"Folder {self.device_id} exists")


    # """metod get hash sum object"""  "проверить работу с не совпадающим хешем !!!!!!!  ВАЖНО!!!!!!!!!!!"

    # def get_hash_md5(self):
    #     with open(self.file_name, "rb") as f:
    #         hash_object = hashlib.md5(f.read())
    #         return hash_object.hexdigest()   
    

    # """metod get new file name""" 
    # def get_new_file_name(self):
    #     list_name = (self.file_name.split("_"))
    #     year = list_name[1][6:10]
    #     month = list_name[1][10:12]
    #     day = list_name[1][12:14]
    #     time = list_name[1][14:20]
    #     new_file_name = f"{list_name[0]}_{year}_{month}_{day}_{time}_{list_name[-1]}"
    #     return new_file_name

"""_______________________________________________________________"""
"""function create folder date"""
def create_folder_date(device_id, new_file_name):
    year = new_file_name.split("_")[1]
    month = new_file_name.split("_")[2]
    """create folder year"""
    if not os.path.isdir(hdd + device_id + "\\" + year):
        os.mkdir(hdd + device_id + "\\" + year)
        print(f"Folder month {year} create successfully")
        logging.info(f"Folder month {year} create successfully")

    """create folder month"""
    if not os.path.isdir(hdd + device_id + "\\" + year + "\\" + month):
        os.mkdir(hdd + device_id + "\\" + year + "\\" + month)
        print(f"Folder month {month} create successfully")
        logging.info(f"Folder month {month} create successfully")



"""function copy video file"""  

def copy_video(file_path, file_name, device_id, new_file_name, year, month):  
    shutil.copy((file_path + "\\" + file_name),
                hdd + device_id + "\\" + year + "\\" + month + "\\" + new_file_name)
    q = hdd + device_id + "\\" + year + "\\" + month + "\\" + new_file_name
    if get_hash_md5(q) == get_hash_md5(file_path + "\\" + file_name):
        print("File copied successfully.")
        os.remove(file_path + "\\" + file_name)
        print("File deleted successfully")



"""___________________START_SCRIPT_________________________________________"""


list_devices = psutil.disk_partitions(all=False)  #  Get a list of all devices
for device in list_devices:
    device = Device()
print(device)
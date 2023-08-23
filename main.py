import os
import psutil
import shutil
import hashlib
import logging

import concurrent.futures  # Модуль concurrent.futures позволяет запускать несколько потоков/процессов и получать из них данные.


logging.basicConfig(
    level=logging.INFO,
    filename="log_file.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
)


hdd_storage = 'C:'


def get_hash_md5(filename):
    """function get hash sum object"""
    with open(filename, "rb") as f:
        hash_object = hashlib.md5(f.read())
        return hash_object.hexdigest()
 

def create_folder(device_id):
    """function create folder device_id""" 
    if not os.path.isdir(hdd_storage + "\\storage\\" + device_id):
        os.mkdir(hdd_storage + "\\storage\\" + device_id)
    else:
        print(f"Folder {device_id} exists")
        logging.info(f"Folder {device_id} exists")
    

def get_new_file_name(file_name):
    """function get new file name""" 
    list_name = (file_name.split("_"))
    year = list_name[1][6:10]
    month = list_name[1][10:12]
    day = list_name[1][12:14]
    time = list_name[1][14:20]
    new_file_name = f"{list_name[0]}_{year}_{month}_{day}_{time}_{list_name[-1]}"
    return new_file_name


def create_folder_date(device_id, new_file_name):
    """function create folder date"""
    year = new_file_name.split("_")[1]
    month = new_file_name.split("_")[2]
    """create folder year"""
    if not os.path.isdir(hdd_storage + "\\storage\\" + device_id + "\\" + year):
        os.mkdir(hdd_storage + "\\storage\\" + device_id + "\\" + year)
        print(f"Folder year {year} create successfully")
        logging.info(f"Folder year {year} create successfully")

        """create folder month"""
        if not os.path.isdir(":\\storage\\" + device_id + "\\" + year + "\\" + month):
            os.mkdir(hdd_storage + "\\storage\\" + device_id + "\\" + year + "\\" + month)
            print(f"Folder month {month} create successfully")
            logging.info(f"Folder month {month} create successfully")

        else:
            print(f"Folder {month} exists")
            logging.info(f"Folder {month} exists")

    else:
        print(f"Folder {year} exists")
        logging.info(f"Folder {year} exists")


def copy_video(file_path, file_name, device_id, new_file_name, year, month):  
    """function copy video file""" 

    try:
        logging.info(file_name)
        shutil.copy((file_path + "\\" + file_name),
                    hdd_storage + "\\storage\\" + device_id + "\\" + year + "\\" + month + "\\" + new_file_name)
        print(f"File {file_name } copied successfully.")
        os.remove(file_path + "\\" + file_name)
        print(f"File {file_name } deleted successfully")
    except:
        logging.info(f"Cannot copy file {file_name }")    
        



def process_device_disk(link_disk):
    if "FILE" in os.listdir(link_disk):
        if (
            "100RECOR" in os.listdir(link_disk + "FILE")
            and len(os.listdir(link_disk + "FILE\\100RECOR")) > 0):
            file_path = link_disk + "FILE\\100RECOR"   #  get path to video file
            list_video_file = os.listdir(file_path)  #  get file list with device
            device_id = (list_video_file[0].split("_"))[0]  #  get id device
            print(device_id)
            logging.info(device_id)  # write in log file device_id
            logging.info(f"On device {device_id} is {len(list_video_file)} files") # write in log file len file list        
            
            create_folder(device_id)    #  function create folder device_id
            
            for file_name in list_video_file:
            
                create_folder_date(device_id, get_new_file_name(file_name))
                year = (get_new_file_name(file_name)).split("_")[1]
                month = (get_new_file_name(file_name)).split("_")[2]
                try:
                    copy_video(file_path, file_name, device_id, get_new_file_name(file_name), year, month)

                # If source and destination are same
                except:
                    logging.info(f"Can not function copy")
        
        else:
            print(f"{device_id} device is cleaned, disk {link_disk} can be disabled")
            logging.info(f"{device_id} device is cleaned")
        
        
    elif "DCIM" in os.listdir(link_disk):
        if (
            "100RECORD" in os.listdir(link_disk + "DCIM")
            and len(os.listdir(link_disk + "DCIM\\100RECORD")) > 0):
            file_path = link_disk + "DCIM\\100RECORD"
            list_video_file = os.listdir(file_path)  #  get file list with device
            device_id = (list_video_file[0].split("_"))[0]  #  get id device
            print(device_id)
            logging.info(device_id)  # write in log file device_id
            logging.info(f"On device {device_id} is {len(list_video_file)} files") # write in log file len file list        
            create_folder(device_id)    #  function create folder device_id
            for file_name in list_video_file:
                create_folder_date(device_id, get_new_file_name(file_name))
                year = (get_new_file_name(file_name)).split("_")[1]
                month = (get_new_file_name(file_name)).split("_")[2]
                try:
                    print(file_name)
                    copy_video(file_path, file_name, device_id, get_new_file_name(file_name), year, month)

                # If source and destination are same
                except:
                    logging.info(f"Can not copy {file_name}")
        
        else:
            print(f"{device_id} device is cleaned, disk {link_disk} can be disabled")
            logging.info(f"{device_id} device is cleaned")


def main():
    list_disk = psutil.disk_partitions(all=False)

    # while len(list_disk) > 2:
        # list_disk = psutil.disk_partitions(all=False)  #  Get a list of all disks
    for disk in list_disk:
        link_disk = disk.device
            


    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_device = {executor.submit(process_device_disk, disk.device): disk for disk in list_disk}
        for future in concurrent.futures.as_completed(future_to_device):
            disk = future_to_device[future]
            future.result()
            # except Exception as exc:
            #     print(f"Processing {disk.device} generated an exception: {exc}")
            # else:
            #     print(f"Finished processing {disk.device}")

if __name__ == "__main__":
    main()


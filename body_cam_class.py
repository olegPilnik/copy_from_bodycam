import pyzipper
import os
import shutil

"""Импортирую функцию disk_partitions библиотеки psutil 
для  получения информации о разделах диска."""
from psutil import disk_partitions

class Device:
    def __init__(self, device):
        self.device = device
 
    def __str__(self):
        return self.device

    def get_type_device(self):
        if os.path.exists(self.device + "FILE"):
            print(f'Device {self.device} is CammPro I-826')
            return True
        elif os.path.exists(self.device + "DCIM"):
            print(f'Device {self.device} is CammPro M-852')
            return True
        else:
            print(f'Device {self.device} is not bodycam')
            return False
        
    def get_device_id(self, password_for_arhive): 
        try:
            archive_location = f'{self.device}info.zip'
            # Распаковка файла из архива
            with pyzipper.AESZipFile(archive_location) as zf:
                zf.setpassword(password_for_arhive.encode())
                info = zf.read('info.ini')
                device_id = (info.decode().split('='))[1]
            return device_id

        except FileNotFoundError:
            print('На пристрої відсутній файл info.zip')    
        
# class File:
#     def __init__(self, file_name, new_file_name):
#         self.file_name = file_name
#         self.new_file_name = new_file_name

#     def copy_file(self, disk):
#         self.disk = disk
#         copy_video(hdd_storage, file_path, file_name, device_id, new_file_name, year, month):  
#         try:
#             if os.path.exists(f'{self.disk}FILE\\100RECOR\\{self.file_name}'):
#                 shutil.copy(f'{self.disk}FILE\\100RECOR\\{self.file_name}', 
#                 f'{hdd_storage}\\{device_id}\\{year}\\{month}\\{self.new_file_name}')
#             logging.info("func copy_video: True")
#             os.remove(file_path + "\\" + self.file_name)
            
#         except Exception as ex:
#             print(f"func copy_video:{ex}")    


    # def get_file_list(self):
    #     pass

  
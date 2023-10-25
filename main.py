from function import create_folder, create_folder_date, copy_video, get_new_file_name
from multiprocessing import Pool
from body_cam_class import Device
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log_file.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
)


"""Импортирую функцию disk_partitions библиотеки psutil 
для  получения информации о разделах диска."""
from psutil import disk_partitions

path_to_storage = 'C:\\storage\\' # хранилище на ноутбуке
# path_to_storage = '\\\\192.168.12.20\\storage' #  хранилище на докстанции
password = "asd_351462"  #  пароль для чтения архива info.zip
body_cam_list = [] # список подключенных бодикамер
   
def main(disk):
    device = Device(disk.device) # создается экземпляр класса Device
    print(device)
    try:
        if device.get_type_device(): # если устройство бодикамера
            device_id = device.get_device_id(password) # получение device_id устр-ва
            print(device_id)
            body_cam_list.append({'device': device.__str__(), 'device_id': device_id}) # disk name и id устр-ва добавляется в список
            print(body_cam_list)
            create_folder(path_to_storage, device_id)    #  function create folder device_id

            try:
                if os.path.exists(f'{device}FILE\\100RECOR'):
                    print(f'Device {device} is CammPro I-826')   
                    file_path = f'{device}FILE\\100RECOR'   #  get path to video file
                    list_video_file = os.listdir(file_path)  #  get file list with device
                    if len(list_video_file) > 0:
                        print(f'The device contains {len(list_video_file)} files')
                        device_id = (list_video_file[0].split("_"))[0]  #  get id device
                        for file_name in list_video_file:
                            try: 
                                new_file_name = get_new_file_name(file_name)
                                year = new_file_name.split("_")[1]
                                month = new_file_name.split("_")[2]
                                create_folder_date(path_to_storage, device_id, new_file_name)
                                copy_video(path_to_storage, file_path, file_name, device_id, new_file_name, year, month)

                            except Exception as ex:
                                print(ex)

                    else:
                        pass

                    print(f'Process {device} finished')


                elif os.path.exists(f'{device}DCIM\\100RECORD'):
                    print(f'Device {device} is CammPro M-852')
                    file_path = f'{device}DCIM\\100RECORD'   #  get path to video file
                    list_video_file = os.listdir(file_path)  #  get file list with device
                    if len(list_video_file) > 0:
                        print(f'The device contains {len(list_video_file)} files')
                        device_id = (list_video_file[0].split("_"))[0]  #  get id device
                        for file_name in list_video_file:
                            try:
                                new_file_name = get_new_file_name(file_name)
                                year = new_file_name.split("_")[1]
                                month = new_file_name.split("_")[2]
                                create_folder_date(path_to_storage, device_id, new_file_name)
                                copy_video(path_to_storage, file_path, file_name, device_id, new_file_name, year, month)

                            except Exception as ex:
                                print(ex)
                    else:
                        pass

                    print(f'Process {device} finished')
                
                
                else:
                    print(f'Device {device} is not bodycam')           

            except Exception as ex:
                print(ex)

    except Exception as ex:
        print(ex)       
    

if __name__ == '__main__':
    print(path_to_storage)
    

    """атрибут (all=False) указывает, что необходимо вернуть
    только физические устройства, а не виртуальные."""
    list_disk = disk_partitions(all=False)

    with Pool(4) as p:
        p.map(main, [disk for disk in list_disk]) # запускаем функцию main в паралельных процесса

    
    print(f'Підключенно відеореєстраторів: {len(body_cam_list)} шт')
    for item in body_cam_list:
        print(item)


    
            
        






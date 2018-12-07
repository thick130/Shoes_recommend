from PIL import Image
import os

#이미지 경로 지정
root_dir = 'C:/Users/KHJ/PycharmProjects/Shoes_tf/naver/'

#경로에 있는 이미지 폴더 저장 
folder_list = os.listdir(root_dir)
img_path_list = []
for folder_name in folder_list:
    img_path = root_dir + folder_name
    img_path_list.append(img_path)
    
#이미지폴더 주소와 폴더명 출력 
print(img_path_list)
print(folder_list)
"""
#원본이미지 크기변경 
for folder_name in img_path_list:
    file_list = os.listdir(folder_name)
    for image in file_list:
        img = Image.open(folder_name + '/' + image)
        resize_img = img.resize((299,299))
        resize_img.save(folder_name + '/' + image)
"""
#이미지 좌우반전 
for folder_name in img_path_list:
    file_list = os.listdir(folder_name)
    for image in file_list:
        img = Image.open(folder_name + '/' + image).convert('RGB')
        flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        flip_img.save(folder_name + '/' + 'flip_' + image)
"""
#이미지를 -20도~20도까지 5도간격으로 회전 
for folder_name in img_path_list:
    file_list = os.listdir(folder_name)
    for image in file_list:
        for ang in range(-90, 90, 15):
            if ang != 0:
                img = Image.open(folder_name + '/' + image)
                rot_img = img.rotate(ang)
                rot_img.save(folder_name + '/' + 'rot_' + str(ang) + '_' + image)
"""
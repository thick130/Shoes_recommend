from PIL import Image
import os
#이미지 경로 지정
root_dir = "./qwe/"
# 카테고리들을 리스트에 받아오기
folder_list = os.listdir(root_dir)
#카테고리별 경로를 리스트에 저장
img_path_list = []
for folder_name in folder_list:
    img_path = root_dir + folder_name
    img_path_list.append(img_path)
print(folder_list)      #카테고리 리스트 출력
print(img_path_list)    #이미지 경로 출력

#카테고리별 이미지를 반전시켜 저장
for folder_name in img_path_list:
    file_list = os.listdir(folder_name)
    for image in file_list:
        img = Image.open(folder_name + '/' + image).convert('L')
        img.save(folder_name + '/' + image)
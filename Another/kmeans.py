import cv2
import numpy as np
import os
global gray
root_dir = "./KNNTRAIN/"
folder_list = os.listdir(root_dir)
print(folder_list)
FN = []
train = []

img_path_list = []
for folder_name in folder_list:
    img_path = root_dir + folder_name
    img_path_list.append(img_path)
cat = 0
for folder_name in img_path_list:
    file_list = os.listdir(folder_name)
    for image in file_list:
        img = cv2.imread(folder_name + '/' + image, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("not img")
        x = np.array(gray)

        train.append(x[:, :].reshape(40000).astype(np.float32))
    cat = cat + 1
X_train = np.array(train)
npFN = np.array(FN)[:, np.newaxis]

from sklearn import cluster
import matplotlib.pyplot  as plt
from sklearn import decomposition

X_train = X_train / 255.
pca = decomposition.PCA(n_components=2, whiten=True).fit_transform(X_train)

X = np.array(pca).astype(np.float32)
print(X)
# create model and prediction
model = cluster.KMeans(init='k-means++', n_clusters=6, algorithm='auto')
model.fit(X)
predict = np.array(model.predict(X))[:, np.newaxis]


# concatenate labels to df as a new column
r = np.hstack([X,predict])

print(r)

centers = np.array(model.cluster_centers_)
print(centers)
print(len(npFN))
center_x = centers[:, 0]
center_y = centers[:, 1]
import mglearn
# scatter plot
plt.scatter(X[:,0],X[:,1],c=npFN[:,0],alpha=0.5)
plt.scatter(center_x,center_y,s=50,marker='D',c='r')
plt.show()
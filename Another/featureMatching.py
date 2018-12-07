import numpy as np
import cv2

def featureMatching():
    img1 = cv2.imread('C:/Users/KHJ/PycharmProjects/Shoes_tf/test/21.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('C:/Users/KHJ/PycharmProjects/Shoes_tf/test/k1.jpg', cv2.IMREAD_GRAYSCALE)
    res = None
    
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    
    matches = sorted(matches, key=lambda x:x.distance)
    res= cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], res, singlePointColor=(0,255,0), matchColor=(255,0,0), flags=2)
    
    cv2.imshow('Feature Matching', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
featureMatching()
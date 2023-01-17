#Import necessarry package 
import cv2


#Reading the low pass images and grayscalig the  low pass images
def imageset1(num):
    
    Image=[]
    for i in range(1,num+1):
        img = cv2.imread(f'image{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/255.0
        Image.append(img)
    return Image
#Reading the high pass images and grayscaling the highpass images
def imageset2(num):
    Images=[]
    for i in range(1,num+1):
        imgs = cv2.imread(f'images{i}.jpg')
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)/255.0
        Images.append(imgs)
    return Images
#applying filter to lowpass images
def lowpass(num, im):
    for i in range(num):
        im[i]=cv2.GaussianBlur(im[i],(55,55),0)
    return im
        
#applying filter to highpass images
def highpass(num, im):
    for i in range(num):
        im[i]=im[i]-cv2.GaussianBlur(im[i],(85,85),0)
    return im 

#Savinng the hybrid image to the persons folder
def saveimages(num, hybrid):
    for i in range(num):
        cv2.imwrite(f'hybrid{i}.jpg' ,hybrid[i]*255)

    pass
    
#Ask user for number of images he will be changing 
print("hello how many images would you like to create")
try:
    number=int(input())
except ValueError:
    print("Please input a number.")

img1= imageset1(number)
img2= imageset2(number)

#Changing the size of each image to make sure they're the same size
for i in range(number):
    width1,height1=img1[i].shape
    width2,height2=img2[i].shape
    area1=width1*height1
    area2=width2*height2
    if area1>area2:
        img1[i]=cv2.resize(img1[i], (height2,width2))
        
    elif area2>area1:
        img2[i]=cv2.resize(img2[i], (height1,width1))
        
    else:
        continue
low=lowpass(number, img1)
high=highpass(number, img2)
hybrid=[]
for i in range(number):
    hybrid.append(low[i]+high[i])

saveimages(number, hybrid)

print("Congrats your images were created check your file!!")
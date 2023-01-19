# Hybrid-Image-Generator
#### Instructions on progrm use 
-Specific file setup is required in order to use the hybrid picture generator. The methods to properly arrange your files so that the generator may run are listed below.

-STEP 1: Locate the photographs you want to use and confirm that they are JPEGs because the application only processes JPEGs.
Use the numbering pattern "Image1- Image2 -Image3....." in Step 2 to rename all the photos to the proper names for low pass filter images.

Use the numbering format "Images1- Images2- Images3....." for high pass filter images. THE NUMBER OF LOWPASS IMAGES MUST BE EQUAL TO THE NUMBER OF HIGHPASS IMAGES.

-Because of this piece of code, you must provide such names for the photographs.
```
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
```
This code processes the images by searching for files with the names "Image" for low pass and "images" for high pass, and it then searches for JPEGS because of the.JPG at the end, therefore the images must be JPEGS.

-Once a file is configured, open the terminal, CD into the path where your folder is configured, and then run the following code.

```
python Saeedfinal.py
```
-It will ask you how many hybrid images you want to create. Do not answer with more images then you have in your file but you may put less.

A video of your program running (1min or less, no voiceover)


#### Project overview
My program, a photo manipulator, alters photos using a filter to produce hybrid images. This software was developed by me to demonstrate the effects of high- and low-pass filtering on photos and how one's view point impacts how one perceives a picture.

#### Breakthrough moment 
In order to change the range of pixel intensities from 0-255 to 0-1 and effectively apply all the filters, I had to divide the grayscale image by 255.

```
imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)/255.0

```
I used imwrite to create the final hybrid image after finishing this, but they all came out black. The image appeared normal while using imshow in the Jupytar notebook, so I wasn't sure why this was happening. However, after researching what occurred, I learned that a different person had encountered a related problem.

Here is the source ![https://stackoverflow.com/questions/54165365/opencv2-imwrite-is-writing-a-black-image] This is the source I used to figure out what the cause of my issue was. The issue was that the imwrite function couldn't handle the 0-1 range for pixel intensity, so I had to convert it back to the 0-255 range by multiplying it by 255.

```
  cv2.imwrite(f'hybrid{i}.jpg' ,hybrid[i]*255)

```

#### Data Abstraction 
First, we used this function to save photos in a list.

```
def imageset1(num):
    
    Image=[]
    for i in range(1,num+1):
        img = cv2.imread(f'image{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/255.0
        Image.append(img)
    return Image
```
I implemented this so that the user could create as many hybrid images as they like. By utilizing a list, I was able to cycle through the list more quickly and effectively.

The other main data type I utilized was a tuple to get the picture width and height using Python's.shape() function, which returns a tuple result that represents the object's dimensions.

Bellow is an example code of how i did it.
```
  width1,height1=img1[i].shape
  width2,height2=img2[i].shape
```

I utilized the tupel to help me determine the image's width and height, which was helpful when I later needed to resize the image.


#### Procedural Abstraction 

```
def lowpass(num, im):
    for i in range(num):
        im[i]=cv2.GaussianBlur(im[i],(55,55),0)
    return im
        
```
I used this function to apply a low pass filter to all of the photographs and I used iteration to loop through the lists of images as an example of procedural abstraction. Instead of going through each image one by one, using the method that uses iteration to apply the blur to every image in the list makes it easier to construct.


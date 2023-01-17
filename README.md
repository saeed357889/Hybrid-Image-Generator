# Hybrid-Image-Generator

 A video of your program running (1min or less, no voiceover)


#### Project overview
My program, which is a photo manipulator, creates hybrid images by editing photos with a filter. I created this software to demostrate the impact of high - and low - pass filtering on photos and how a persons point of veiw affects how they see the image.

#### Breakthrough moment 
I had to divide the grayscale image by 255 in order to change the range of pixel intensities from 0-255 to 0-1 in to properly implement all the filters.
```
imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)/255.0

```
After completing this, I used imwrite to produce the final hybrid image, but all of them turned out to be black. I wasn't sure why this happened because using imshow in the Jupytar notebook made the image look normal. However, after looking up what happened, I found that someone else had experienced a similar issue.

Here is the source ![https://stackoverflow.com/questions/54165365/opencv2-imwrite-is-writing-a-black-image] Here is the source I used to find out what my problem was the problem was that imwrite canot handle the 0-1 range for pixel intensity so I had to convert iit back to the 0-255 range and I did that by multiplying imwrite function by 255.

```
  cv2.imwrite(f'hybrid{i}.jpg' ,hybrid[i]*255)

```






#### Data Abstraction 
First we stored images in a list using this function
```
def imageset1(num):
    
    Image=[]
    for i in range(1,num+1):
        img = cv2.imread(f'image{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/255.0
        Image.append(img)
    return Image
```
The reason I did this was so the user  can creat as many hybrid images as they wanted and using the list allowed me to loop through the list faster and more effeciently.

The other major data type that I used was a tuple to access the width and the height of the images using pythons .shape() feature which returns the tupel value which is the dimensions of the object that its called on.
Bellow is an example code of how i did it.
```
  width1,height1=img1[i].shape
  width2,height2=img2[i].shape
```

The tupel was used to help me find the width and the height of the image which was usefull later on to resize the image.


#### Procedural Abstraction 
```
def lowpass(num, im):
    for i in range(num):
        im[i]=cv2.GaussianBlur(im[i],(55,55),0)
    return im
        
```
This function is one example of procedual abstraction that I used this function impplemented a low pass filter on all the images and I used itiration by for looping through the lists of images. Using the function that uses itteration  to implement the blur on every image in the list made it simpler to implement instead of going through all the images 1 by 1.


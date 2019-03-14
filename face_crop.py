## This program first ensures if the face of a person exists in the given image or not then if it exists, it crops
## the image of the face and saves to the given directory.

## Importing Modules
import cv2
import os


#################################################################################

##Make changes to these lines for getting the desired results.

## DIRECTORY of the images
directory = "D:\\images"

## directory where the images to be saved:
f_directory = "D:\\images_new\\"
################################################################################
            
def facecrop(image,attr):
    ## Crops the face of a person from any image!

    ## OpenCV XML FILE for Frontal Facial Detection using HAAR CASCADES.
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    ## Reading the given Image with OpenCV
    img = cv2.imread(image)

    try:
        ## Some downloaded images are of unsupported type and should be ignored while raising Exception, so for that
        ## I'm using the try/except functions.
    
        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            sub_face = img[y:y+h, x:x+w]

            f_name = image.split('\\')
            f_name = f_name[-1]

            print(f_name)
            ## Change here the Desired directory.
            cv2.imwrite(f_directory + attr+"\\"+ f_name, sub_face)
            print ("Writing: " + image)

    except:
        pass
count=3
directory2=os.listdir(directory)
print(directory2)
if __name__ == '__main__':
    while(count>=0):
        images=os.listdir("D:\\images\\"+directory2[count])
        print(images)
        i = 0
        for img in images:
            file = "D:\\images\\"+directory2[count]+"\\" + img
            print(file)
            print (i)
            facecrop(file,directory2[count])
            i += 1
        count=count-1
        

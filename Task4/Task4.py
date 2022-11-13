import cv2
from matplotlib import pyplot as plt

#Read image file
image = cv2.imread("Pokemon-Go.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Blur image with Gaussian Blur
blur_image1 = cv2.GaussianBlur(image, (3,3), 0)
blur_image2 = cv2.GaussianBlur(image, (51,51), 0)

#Unsharp image
unsharp_image1 = cv2.addWeighted(image, 2, blur_image1, -1, 0) 
unsharp_image2 = cv2.addWeighted(image, 2, blur_image2, -1, 0) 

#Highboost filtering with k=4
k1 = 4
boost_image_4_1 = cv2.addWeighted(image, 1+k1, blur_image1, -k1, 0) 
boost_image_4_2 = cv2.addWeighted(image, 1+k1, blur_image2, -k1, 0) 

#Highboost filtering with k=8
k2 = 8
boost_image_8_1 = cv2.addWeighted(image, 1+k2, blur_image1, -k2, 0) 
boost_image_8_2 = cv2.addWeighted(image, 1+k2, blur_image2, -k2, 0) 

#Visualize image
fig = plt.figure(figsize=(20,15))
list_image = [image, blur_image1, blur_image2,
                unsharp_image1, boost_image_4_1, boost_image_4_2,
                unsharp_image2, boost_image_8_1, boost_image_8_2]

list_title = ["Original", "Blur(kernel=3x3)", "Blur(kernel=51x51)",
             "UnsharpMasking(blur kernel=3x3)", "HighboostFiltering k={} (blur kernel=3x3)".format(k1), "HighboostFiltering k={} (blur kernel=3x3)".format(k2),
             "UnsharpMasking(blur kernel=51x51)", "HighboostFiltering k={} (blur kernel=51x51)".format(k1), "HighboostFiltering k={} (blur kernel=51x51)".format(k2)]

for i in range(9):
    ax = fig.add_subplot(3, 3, i+1)
    ax.imshow(list_image[i])
    ax.axis('off')
    ax.axes.set_title(list_title[i])

plt.show()
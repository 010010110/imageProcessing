import numpy as np
import cv2
from matplotlib import pyplot as plt


def show_img_with_matplotlib(img, title, pos):
    # Convert BGR image to RGB
    img = img[:, :, ::-1]

    ax = plt.subplot(5, 6, pos)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    cv2.imwrite("img.jpg",img)



def show_hist_with_matplotlib_gray(hist, title, pos, color):
    ax = plt.subplot(5, 6, pos)
    # plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("number of pixels")
    plt.xlim([0, 256])
    plt.plot(hist, color=color)

# Create the dimensions of the figure and set title:
plt.figure(figsize=(18, 14))
plt.suptitle("Histogram, Equalization and Negative", fontsize=16, fontweight='bold')

# Load the image and convert it to grayscale:
image1 = cv2.imread('1.jpg')
image2 = cv2.imread('2.jpg')
image3 = cv2.imread('3.jpg')
image4 = cv2.imread('4.jpg')

#-------------------------------------------------------------------------------------------
# Gray image
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
gray_image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)


# Histogram from gray image
hist_gray = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])

# Equalize gray image and calculate histogram:
gray_image_eq = cv2.equalizeHist(gray_image1)
hist_gray_eq = cv2.calcHist([gray_image_eq], [0], None, [256], [0, 256])

# Negative image and calculate histogram
gray_image_negative = cv2.bitwise_not(gray_image1)
hist_negative_image = cv2.calcHist([gray_image_negative], [0], None, [256], [0, 256])
#-------------------------------------------------------------------------------------------

# Add 50 to every pixel the result will look lighter and calculate histogram:
M = np.ones(gray_image2.shape, dtype="uint8") * 50
added_image = cv2.add(gray_image2, M)
hist_added_image = cv2.calcHist([added_image], [0], None, [256], [0, 256])

# Equalize image and calculate histogram:
added_image_eq = cv2.equalizeHist(added_image)
hist_eq_added_image = cv2.calcHist([added_image_eq], [0], None, [256], [0, 256])

# Negative ligth image and calculate histogram
add_image_negative = cv2.bitwise_not(added_image)
hist_added_image_negative = cv2.calcHist([add_image_negative], [0], None, [256], [0, 256])
#-------------------------------------------------------------------------------------------

# Add 100 to every pixel the result will look lighter and calculate histogram:
M = np.ones(gray_image3.shape, dtype="uint8") * 100
added_100_image = cv2.add(gray_image3, M)
hist_100_added_image = cv2.calcHist([added_100_image], [0], None, [256], [0, 256])

# Equalize image and calculate histogram:
added_100_image_eq = cv2.equalizeHist(added_100_image)
hist_100_eq_added_image = cv2.calcHist([added_100_image_eq], [0], None, [256], [0, 256])

# Negative ligth image and calculate histogram
add_100_image_negative = cv2.bitwise_not(added_100_image)
hist_100_added_image_negative = cv2.calcHist([add_100_image_negative], [0], None, [256], [0, 256])
#-------------------------------------------------------------------------------------------

# Subtract 50 from every pixel the result will look darker and calculate histogram:
subtracted_image = cv2.subtract(gray_image4, M)
hist_subtracted_image = cv2.calcHist([subtracted_image], [0], None, [256], [0, 256])

# Equalize image and calculate histogram:
subtracted_image_eq = cv2.equalizeHist(subtracted_image)
hist_eq_subtracted_image = cv2.calcHist([subtracted_image_eq], [0], None, [256], [0, 256])

# Negative darker image and calculate histogram
subtracted_image_neg = cv2.bitwise_not(subtracted_image)
hist_neg_added_image = cv2.calcHist([subtracted_image_neg], [0], None, [256], [0, 256])
#-------------------------------------------------------------------------------------------

# Plot the images and the histograms (without equalization first):
show_img_with_matplotlib(cv2.cvtColor(gray_image1, cv2.COLOR_GRAY2BGR), "gray", 1)
show_hist_with_matplotlib_gray(hist_gray, "grayscale histogram", 2, 'm')
# show_img_with_matplotlib(cv2.cvtColor(added_image, cv2.COLOR_GRAY2BGR), "gray lighter +50", 7)
# show_hist_with_matplotlib_gray(hist_added_image, "grayscale histogram", 8, 'm')
# show_img_with_matplotlib(cv2.cvtColor(added_100_image, cv2.COLOR_GRAY2BGR), "gray lighter +100", 13)
# show_hist_with_matplotlib_gray(hist_100_added_image, "grayscale histogram", 14, 'm')
# show_img_with_matplotlib(cv2.cvtColor(subtracted_image, cv2.COLOR_GRAY2BGR), "gray darker -50", 19)
# show_hist_with_matplotlib_gray(hist_subtracted_image, "grayscale histogram", 20, 'm')

# # Plot the images and the histograms (with equalization):
# show_img_with_matplotlib(cv2.cvtColor(gray_image_eq, cv2.COLOR_GRAY2BGR), "grayscale equalized", 3)
# show_hist_with_matplotlib_gray(hist_gray_eq, "grayscale equalized histogram", 4, 'm')
# show_img_with_matplotlib(cv2.cvtColor(added_image_eq, cv2.COLOR_GRAY2BGR), "gray lighter +50 equalized", 9)
# show_hist_with_matplotlib_gray(hist_eq_added_image, "grayscale equalized histogram", 10, 'm')
# show_img_with_matplotlib(cv2.cvtColor(added_100_image_eq, cv2.COLOR_GRAY2BGR), "gray lighter +100 equalized", 15)
# show_hist_with_matplotlib_gray(hist_100_eq_added_image, "grayscale equalized histogram", 16, 'm')
# show_img_with_matplotlib(cv2.cvtColor(subtracted_image_eq, cv2.COLOR_GRAY2BGR), "gray darker -50 equalized", 21)
# show_hist_with_matplotlib_gray(hist_eq_subtracted_image, "grayscale equalized histogram", 22, 'm')

# # Plot the images and histogram (with negative)
# show_img_with_matplotlib(cv2.cvtColor(gray_image_negative, cv2.COLOR_GRAY2BGR), "grayscale negative", 5)
# show_hist_with_matplotlib_gray(hist_negative_image, "grayscale negative histogram", 6, 'm')
# show_img_with_matplotlib(cv2.cvtColor(add_image_negative, cv2.COLOR_GRAY2BGR), "gray lighter +50 negative", 11)
# show_hist_with_matplotlib_gray(hist_added_image_negative, "gray lighter negative histogram", 12, 'm')
# show_img_with_matplotlib(cv2.cvtColor(add_100_image_negative, cv2.COLOR_GRAY2BGR), "gray lighter +100 negative", 17)
# show_hist_with_matplotlib_gray(hist_100_added_image_negative, "gray lighter negative histogram", 18, 'm')
# show_img_with_matplotlib(cv2.cvtColor(subtracted_image_neg, cv2.COLOR_GRAY2BGR), "gray darker -50 negative", 23)
# show_hist_with_matplotlib_gray(hist_neg_added_image, "gray darker negative histogram", 24, 'm')

# Show the Figure:
plt.show()
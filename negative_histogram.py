# USAGE
# python grayscale_histogram.py --image beach.png

# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute a grayscale histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# equalize gray image and calc histogram
img_eq = cv2.bitwise_not(image)
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])



# matplotlib expects RGB images so convert and then display the image
# with matplotlib gray image
# plt.figure()
# plt.title("Grayscale original image")
# plt.axis("off")
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

# with matplotlib equalized image
plt.figure()
plt.title("Grayscale negative image")
plt.axis("off")
plt.imshow(cv2.cvtColor(img_eq, cv2.COLOR_GRAY2RGB))

# plot the histogram
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])

# plot the equalized histogram
plt.figure()
plt.title("Grayscale negative Histogram")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist_eq)
plt.xlim([0, 256])

plt.show()
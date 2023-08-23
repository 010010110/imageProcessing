# USAGE
# python color_histograms.py --image beach.png

# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

# split the image into its respective channels, then initialize the
# tuple of channel names along with our figure for plotting
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and plot it
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])

hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))
#-------------------------------------------------------
img_hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
img_hsv[:, :, 2]=cv2.equalizeHist(img_hsv[:, :, 2])
saida=cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
concat=cv2.hconcat((image,saida))

chans = cv2.split(saida)
colors = ("b", "g", "r")
plt.figure()
plt.title("Equalized Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# loop over the saida channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and plot it
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])

hist = cv2.calcHist([saida], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))
#------------------------------------------------------

# display the original input
plt.figure()
plt.axis("off")
plt.title("Original image")
plt.imshow(imutils.opencv2matplotlib(image))

# display the equalized input
plt.figure()
plt.axis("off")
plt.title("equalized image")
plt.imshow(imutils.opencv2matplotlib(saida))


# show our plots
plt.show()
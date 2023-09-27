import cv2 as cv

# READING IMAGE
img = cv.imread('./sampleInputImg.jpg')

# OUTPUT IMAGE DIMENSIONS
width = 256
height = 256

# RESZING IMAGE
resized_img = cv.resize(img, (width, height))

# DISPLAYING IMAGES
cv.imshow('Input Original image', img)
cv.imshow('Output Resized image', resized_img)

cv.waitKey(0)

# CLOSING ALL WINDOWS
cv.destroyAllWindows()

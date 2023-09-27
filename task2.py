import cv2 as cv

# READING IMAGE
img = cv.imread('./sampleInputImg.jpg')

# CONVERTING TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# DISPLAYING IMAGE
cv.imshow('input Original image', img)
cv.imshow('Output Grayscale image', gray)

cv.waitKey(0)

# CLOSING ALL WINDOWS
cv.destroyAllWindows()

import cv2 as cv

image = cv.imread('./sampleInputImg.jpg')

# Binary conversion
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
_,binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

#image display
cv.imshow('Original ', image)
cv.imshow('Binary', binary)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv

image = cv.imread('./sampleInputImg.jpg')
#BINARY CONVERSION
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
_,binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

#CONTOURS
contours, _ = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
marked = image.copy()

# FILTERING
min_contour_area = 1000
filtered_contours = [contour for contour in contours if cv.contourArea(contour) >= min_contour_area]

#MARKING THE IMAGE
for i,contour in enumerate(filtered_contours,0):
    cv.drawContours(marked, contours, -1, (255,0,0), 2)
    cv.putText(marked, str(i), tuple(contour[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

#show images
cv.imshow('Original ', image)
cv.imshow('Marked', marked)
cv.waitKey(0)
cv.destroyAllWindows()

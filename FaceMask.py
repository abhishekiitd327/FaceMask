import cv2
import numpy as np
import os
import stasm

"""
MOUTH_POINTS = list(range(59, 77))
RIGHT_BROW_POINTS = list(range(17, 22))
LEFT_BROW_POINTS = list(range(22, 27))
RIGHT_EYE_POINTS = list(range(30, 38))
LEFT_EYE_POINTS = list(range(39, 48))
NOSE_POINTS = list(range(49, 59))
BORDER_POINTS = list(range(0, 16))
"""


def get_face_mask(im, pts):

    #mask = np.zeros_like(img)
    if np.size(pts) > 76:
        vertices_mouth = np.array([pts[59:77]], dtype=np.int32)
        vertices_eye_right = np.array([pts[30:38]], dtype=np.int32)
        vertices_eye_left = np.array([pts[39:48]], dtype=np.int32)
        vertices_eyebrow_right = np.array([pts[17:22]], dtype=np.int32)
        vertices_eyebrow_left = np.array([pts[22:27]], dtype=np.int32)
        vertices_border = np.array([pts[0:16]], dtype=np.int32)

        mask = np.zeros_like(im)

        #cv2.fillPoly(mask, vertices[0:32], 255)

        cv2.fillConvexPoly(mask, cv2.convexHull(vertices_border), 255)

        #cv2.fillConvexPoly(mask, cv2.convexHull(vertices_mouth), 0)
        #cv2.fillConvexPoly(mask, cv2.convexHull(vertices_eye_right), 0)
        #cv2.fillConvexPoly(mask, cv2.convexHull(vertices_eye_left), 0)
        #cv2.fillConvexPoly(mask, cv2.convexHull(vertices_eyebrow_right), 0)
        #cv2.fillConvexPoly(mask, cv2.convexHull(vertices_eyebrow_left), 0)
        #cv2.fillConvexPoly(mask, cv2.convexHull(vertices[59:77]), 255)

    return mask


filepath = 'face1.jpeg'
img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
imgcol = cv2.imread(filepath)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
imgcol = cv2.resize(imgcol, (0,0), fx=0.5, fy=0.5)

landmarks = stasm.search_single(img)
#print(f"landmarks = {len(landmarks)}")
    
for pt in landmarks:
    cv2.circle(imgcol, (pt[0], pt[1]), 5, (0,0,255), -1)

face_mask = get_face_mask(img, landmarks)
#maskname = f'{images_dir}{filename}_mask{extension}'

#cv2.imwrite('sweaty_139_0.png', face_mask)
#cv2.imwrite(maskname, face_mask)
cv2.imshow("mask", face_mask)
cv2.imshow("imgcol", imgcol)

cv2.waitKey()
cv2.destroyAllWindows()

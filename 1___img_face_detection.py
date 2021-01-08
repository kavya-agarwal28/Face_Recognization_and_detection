import cv2
import face_recognition

image_to_detect = cv2.imread('images/pic4.jpg')

all_face_locations = face_recognition.face_locations(image_to_detect,model='hog')
# face_locations is now an array listing the co-ordinates of each face
print('There are {} number of faces'.format(len(all_face_locations)))

for index,current_face_location in enumerate(all_face_locations):
    top_pos,right_pos,bottom_pos,left_pos=current_face_location
    print('Four face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    #current_face_image = image_to_detect[top_pos:bottom_pos,left_pos:right_pos]
    #returns face cropped from image
    cv2.rectangle(image_to_detect,(left_pos,top_pos),(right_pos,bottom_pos),(0,0,255),-1)
cv2.imshow("Face no "+str(index+1),image_to_detect)
import cv2
import face_recognition

original_image = cv2.imread('images/pic.jpeg')

one_image = face_recognition.load_image_file('images/picc9.jpeg')
one_face_encodings = face_recognition.face_encodings(one_image)[0]

two_image = face_recognition.load_image_file('images/picc5.jpeg')
two_face_encodings = face_recognition.face_encodings(two_image)[0]

known_face_encoding = [one_face_encodings,two_face_encodings]
known_face_names = ["Kavya","Reena"]

image_to_recognize = face_recognition.load_image_file('images/pic.jpeg')
all_face_locations = face_recognition.face_locations(image_to_recognize,model='hog')
all_face_encodings = face_recognition.face_encodings(image_to_recognize,all_face_locations)
print(all_face_encodings)
for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):
    top_pos,right_pos,bottom_pos,left_pos=current_face_location
    all_matches = face_recognition.compare_faces(known_face_encoding, current_face_encoding)
    name_of_person = 'Unknown face'
    if True in all_matches:
        first_match_index = all_matches.index(True)
        name_of_person = known_face_names[first_match_index]
    cv2.rectangle(original_image ,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)
    
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(original_image ,name_of_person,(left_pos,bottom_pos),font,0.5,(255,255,255),1)
    
cv2.imshow("Face Identified",original_image)
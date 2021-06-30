
import cv2
import os,time,shutil

#images=os.listdir('chinese')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

direc=os.listdir()
#Remove unwanted files in the directory if any
for i in direc:
	if "image" not in i :
		direc.remove(i)
		print(i)
#direc.remove('haarcascade_frontalface_default.xml')
#direc.remove('haarcascade_eye.xml')
#direc.remove('singleface')
#direc.remove('na')
#print(direc)
for images in direc:
	#print(images)
	img = cv2.imread(images)
#print('chinese\\{}'.format(i))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	try:
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		eyes = eye_cascade.detectMultiScale(gray,1.3,5)

		if len(faces)==1 and len(eyes)==2:
			shutil.move(images, 'singleface')
		elif len(faces)>1:
			shutil.move(images, 'multiface')
		else:
			shutil.move(images , 'na')

	except:
		shutil.move(images, 'na')
print('finished')	
#for (x,y,w,h) in faces:
    #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #roi_gray = gray[y:y+h, x:x+w]
    #roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    #for (ex,ey,ew,eh) in eyes:
     #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

'''cv2.imshow('img',img)
cv2.waitKey(0)
time.sleep(2)
cv2.destroyAllWindows()
'''

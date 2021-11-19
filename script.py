import cv2  

# xml_hc = 'hc/haarcascade_frontalface_alt2.xml'
xml_hc = 'hc/haarcascade_eye_tree_eyeglasses.xml'

fc = cv2.CascadeClassifier(xml_hc)

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while not cv2.waitKey(20) & 0xFF == ord('q'):
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = fc.detectMultiScale(gray)

    for x, y , w, h in faces:
        cv2.rectangle(frame, (x, y), ( x + w, y + h), (0,0,255), 2)

    cv2.imshow('color', frame)
    cv2.imshow('gray', gray)

from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2

# Iniciar la captura de video
cap = cv2.VideoCapture(1)

def gen_frame():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            _, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def recognition_home_view(request):
    return render(request, 'WebSite/home.html')

def video(request):
    return StreamingHttpResponse(gen_frame(), content_type='multipart/x-mixed-replace; boundary=frame')

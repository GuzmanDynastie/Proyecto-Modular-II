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
            resized_frame = cv2.resize(frame, (1080, 720))
            
            _, encode = cv2.imencode('.jpg', resized_frame)
            frame = encode.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def product_scan(request):
    return render(request, 'WebSite/product_scan.html')

def video(request):
    return StreamingHttpResponse(gen_frame(), content_type='multipart/x-mixed-replace; boundary=frame')

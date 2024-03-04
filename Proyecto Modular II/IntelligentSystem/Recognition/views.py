from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_POST
import cv2
import threading

# Iniciar la captura de video
cap = cv2.VideoCapture(1)
stop_event = threading.Event()

def gen_frame():
    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break
        else:
            resized_frame = cv2.resize(frame, (1080, 720))
            
            _, encode = cv2.imencode('.jpg', resized_frame)
            frame_bytes = encode.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

    cap.release()  # Liberar el objeto cv2.VideoCapture al salir del bucle

def product_scan(request):
    return render(request, 'WebSite/product_scan.html')

def video(request):
    return StreamingHttpResponse(gen_frame(), content_type='multipart/x-mixed-replace; boundary=frame')

def stop_video(request):
    stop_event.set()
    return redirect("http://127.0.0.1:3000/home")
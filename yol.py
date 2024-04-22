from ultralytics import YOLO
import cv2 as cv
from time import sleep
from walk import run
from capture import WindowCapture
from threading import Thread

#https://docs.ultralytics.com/quickstart/#install-ultralytics

# CUDA Pytorch > https://pytorch.org/get-started/locally/ 
# CUDA Toolkit > https://developer.nvidia.com/cuda-downloads
    


#yolov8n-oiv7.pt / yolov8s-oiv7.pt
#model = YOLO('yolov8x-oiv7.onnx')

#trained on Open Image V7, which include 600 pre-trained classes
model = YOLO('yolov8x-oiv7.pt')

#Export to ONNX or OpenVINO for up to 3x CPU speedup.
#model.export(format='onnx')

wincap = WindowCapture('window_name')

def obb():
    while 1:

        img = wincap.get_screenshot()

        results = model.predict(img, device=0)

        annotated_frame = results[0].plot()
        cv.imshow("YOLOv8 Inference", annotated_frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

#https://www.pythontutorial.net/python-concurrency/python-threading/

t1 = Thread(target=obb)

t2 = Thread(target=run)

if __name__ == "__main__":
    t1.start()
    sleep(10)
    t2.start()
    t1.join()
    t2.join()
    

import numpy.core.multiarray
import cv2 as cv

from pathlib import Path

THRESHOLD = 0.45
NMS = 0.2

classNames = []
objects = []
base = Path(__file__).parent
classFile = str((base /"Object_Detection_Files/coco.names").resolve())

with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = str((base/"Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt").resolve())
weightsPath = str((base/"Object_Detection_Files/frozen_inference_graph.pb").resolve())


net = cv.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def processImage(imagePath):
    img = cv.imread(imagePath)

    classIds, confs, bbox = net.detect(img, confThreshold=THRESHOLD, nmsThreshold=NMS)

    data =[]
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if confidence > 0.50 and className in ('cat', 'dog'): 
                data.append({'className':className, 'confidence': confidence})
            else:
                continue

    return data


# testing - show all classifications
# def testing(imagePath):
#     img = cv.imread(imagePath)

#     classIds, confs, bbox = net.detect(img, confThreshold=THRESHOLD, nmsThreshold=NMS)

#     data =[]
#     if len(classIds) != 0:
#         for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
#             className = classNames[classId - 1]
#             data.append({'className':className, 'confidence': confidence})
#             # cv.rectangle(img,box,color=(0,0,0),thickness=2)
#             # cv.putText(img,classNames[classId-1],(box[0], box[1]),
#             # cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
#             # cv.putText(img,str(round(confidence*100,2)),(box[0], box[1]),
#             # cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
    
#     print(data)
#     # cv.imshow("Output",img)
#     # cv.waitKey(0)

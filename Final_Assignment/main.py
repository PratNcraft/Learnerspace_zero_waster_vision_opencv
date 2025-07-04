from ultralytics import YOLO

# Load a pretrained model (nano version is very fast)
model = YOLO("yolov8n.pt")

# train on images
model.train(data= "config.yaml", epochs=30)


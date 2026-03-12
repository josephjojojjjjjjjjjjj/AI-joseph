[app]
title = JosephApp
package.name = josephapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pt
version = 0.1

# Ensure these requirements match your code
requirements = python3, kivy==2.3.0, opencv-python, numpy, ultralytics, torch, torchvision, tqdm, PyYAML, scipy, pandas, requests, seaborn, matplotlib

orientation = portrait
fullscreen = 0
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE

# (list) Predicted YOLO model file to include
# If your model is 'yolov8n.pt', ensure it's in the repo root
source.include_patterns = yolov8n.pt

[buildozer]
log_level = 2
warn_on_root = 1

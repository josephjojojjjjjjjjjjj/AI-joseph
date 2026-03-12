[app]
# (str) Title of your application
title = JosephApp

# (str) Package name
package.name = josephapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (IMPORTANT: Added 'pt' for YOLO model)
source.include_exts = py, png, jpg, kv, atlas, pt

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Added 'opencv-python', 'numpy', and 'ultralytics' (for YOLO)
requirements = python3, kivy==2.3.0, opencv-python, numpy, ultralytics, pillow

# (list) Permissions
# REQUIRED: Camera for ball tracking, Internet for downloading YOLO weights (first run)
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API (API 33 is standard for 2026)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android logcat filters to help you debug
android.logcat_filters = *:S python:D

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Supported orientation (landscape or portrait)
orientation = portrait

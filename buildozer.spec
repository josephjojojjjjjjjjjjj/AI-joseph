[app]

# (str) Title of your application
title = JosephApp

# (str) Package name
package.name = josephapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Application versioning (method 1)
# --- FIX STARTS HERE ---
version = 0.1
# Make sure the line below is COMMENTED OUT with a #
# version.regex = __version__ = ['"](.*)['"]
# --- FIX ENDS HERE ---

# (list) Application requirements
# Since you are building a Cricket AI, ensure these are here:
requirements = python3,kivy,opencv-python,numpy

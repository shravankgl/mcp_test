#!/usr/bin/env python3
import subprocess
import time
import os

# Set the DISPLAY environment variable for the main display
os.environ['DISPLAY'] = ':1'

# Open Pinta
print("Opening Pinta on main display...")
pinta_process = subprocess.Popen(['pinta'])
print(f"Pinta process started with PID: {pinta_process.pid}")

# Wait a bit to ensure it opens
time.sleep(2)

# Check if process is still running
if pinta_process.poll() is None:
    print("Pinta is running successfully")
else:
    print(f"Pinta exited with code: {pinta_process.returncode}")

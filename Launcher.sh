#!/bin/sh
echo "Loading..."
sleep 5
echo "Changing Directory"
cd /home/mass/Desktop/Obj-Detect-and-Depth/object-detect #Replace it with your actual path.
echo "Setting XDG_RUNTIME_DIR"
export XDG_RUNTIME_DIR=/run/user/$(id -u)
echo "Setting actual permissions for runtime directory"
sudo chmod 0700 /run/user/1000
echo "Running Python script"
python3 IASDriver.py
cd

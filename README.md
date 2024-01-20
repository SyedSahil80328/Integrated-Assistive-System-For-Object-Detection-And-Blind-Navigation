<h1>Integrated Assistive System For Object Detection And Blind Navigation</h1>
<p>Embark on a transformative journey towards enhanced accessibility and independence with our innovative repository, 'Integrated Assistive System for Object Detection and Blind Navigation.' This comprehensive solution seamlessly combines cutting-edge object detection capabilities and intelligent blind navigation technologies. Empower individuals with visual impairments to navigate their surroundings confidently, fostering a more inclusive and connected world.</p>
<h1>Basic Hardware Requirements</h1>
<ol>
<li>Raspberry PI Computer.<sup><i>1</i></sup></li>
<li>Micro SD Card.<sup><i>2</i></sup></li>
<li>Raspberry PI adapter or battery.</li>
<li>Raspberry PI Fan.</li>
<li>Any type of light weight cap.</li>
<li>Speaker or Headphones.<sup><i>3</i></sup></li>
<li>PI Camera or USB Webcam.</li>
<li>Raspberry PI Case.</li>
<li>Raspberry PI Heatsink.</li>
</ol>
<i>
<sup>1</sup>Version 4 or Higher with Main memory of 8 Gigabytes.<br>
<sup>2</sup>32 Gigabytes is sufficient, but 64 is recommended for development purpose and avoiding storage shortage.<br>
<sup>3</sup>Wired is recommended, as wireless connection requires desktop setting for initiating or manipulating connection.
</i>

<h1>Basic Installation</h1>
<p>Refer <a href="https://www.raspberrypi.com/documentation/computers/getting-started.html">here</a> for learning complete setup of your Raspberry PI.</p>
<p>Install the Raspberry PI imager by clicking <a href="https://www.raspberrypi.com/software/">this link.</a></p>
<p>Note: You can also install it with NOOBS <i>(New Out Of Box Software)</i> by clicking <a href="https://www.raspberrypi.com/news/introducing-noobs/">this link.</a></p>
<p>After installing, your Raspberry PI interface will be looking as shown in Figure 1</p>
<img src="https://www.raspberrypi.com/documentation/computers/images/recommended-software.png">
<p align="center"><i>Figure 1: Raspberry PI Interactive OS</i></p>

<h1>Setup Environment</h1>
<p>We can have laboratory environment both wired(just like desktop computer) or wireless(through SSH or VNC).</p>
<p>For Wired setup, we require</p>
<ol>
<li>Monitor which supports HDMI port.<sup><i>1</i></sup></li>
<li>Mouse.</li>
<li>Keyboard.</li>
<li>HDMI to micro HDMI cable or adapter.</li>
</ol>
<p><i><sup>1</sup>If you have only VGA port in your monitor and doesn't support audio, a VGA to HDMI adapter with an audio device is needed.</i></p>
<p>For wireless usage, you should enable SSH as in Figure 2 when imager has been installed for downloading the Operating System for Raspberry PI. Then issue the command.</p>
<p float="left">
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/pi-imager.png" width="45%">
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/SSH-Save.png" width="45%">
</p>
<p align="center"><i>Figure 2: Enabling SSH by clicking Ctrl+Shift+X on Image 1 to open Image 2</i></p>

```
ssh pi@192.168.29.165 #Replace it with actual username of PI and IP address of your device.
```

<p>Then provide your password to get connected (Give yes for the message after encountering a message if you are logging in for first time).</p>
<p>You'll be logged in as shown in figure 3</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/login-SSH.png">
<p align="center"><i>Figure 3: Login through SSH</i></p>

<p><i>
<b>Note:</b> Both PI and operating device must be in same Wi-Fi network.<br>
<b>Tips:</b> After connecting the operating device to a Wi-Fi, you can find IP address through the application <a href="https://www.fing.com/products/fing-desktop">fing</a>.
</i></p>

<b><p>To have seamless experience, we recommend using wired method as it is easy and doesn't require internet (except for installation and upgrading required modules).</p></b>

<h1>Usage through VNC</h1>
<p>Working through SSH terminal the entire time could be tedious. Also, our program requires GUI for showing the output. In that case, SSH fails to execute our program. So, to interactively work with Raspberry PI headlessly, we can use VNC which is a best alternative to SSH. VNC lets you to work with PI on GUI. To enable it, turn on your Raspberry PI and connect via your device through SSH. Then issue the command.</p>

```
sudo raspi-config
```

<p>Then select interface option by hitting enter button on <code>Interface Options</code> (Control through up/down arrow buttons) as shown in Figure 4.</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/raspi-config.png">
<p align="center"><i>Figure 4: Raspi Config Interface</i></p>

<p>Then select VNC (Figure 5).</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/config-interface.png">
<p align="center"><i>Figure 5: Selection of VNC</i></p>

<p>Then select <code>Yes</code> (control by left/right arrow and hit enter) shown in Figure 6.</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/interface-VNC.png">
<p align="center"><i>Figure 6: Enabling VNC</i></p>

<p>After clicking yes, you'll see a couple of output as shown in Figure 7a and 7b.</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-success-console.png">
<p align="center"><i>Figure 7a: Output of activation on console</i></p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-success.png">
<p align="center"><i>Figure 7b: Output of activation on raspi-config</i></p>

<p>Select <code>OK</code> and hit finish</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/raspi-config-finish.png">
<p align="center"><i>Figure 8: Exiting the raspi-config</i></p>

<p>Cool! We have now enabled VNC for working with Raspberry PI headlessly along with GUI. Next, head over to RealVNC viewer.<br><a href="https://www.realvnc.com/en/connect/download/viewer/">Download RealVNC viewer.</a></p>
<p>After opening the viewer, create a new connection as shown in figure 9.</p>
<p align="center"><img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-new.png" width="75%"></p>
<p align="center"><i>Figure 9: Creation of new connection</i></p>

<p>Then provide the same IP address that has been used during SSH login and any friendly name as indicated in figure 10.</p>
<p align="center"><img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-credentials.png" width="75%"></p>
<p align="center"><i>Figure 10: Providing neccessary details</i></p>

<p>Then, a computer icon as shown in Figure 11 is created. You can rename it by pressing F2. You need to click that icon and enter username and password as indicated in figure 12.</p>
<p align="center"><img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-new.png" width="75%"></p>
<p align="center"><i>Figure 11: New device creation</i></p>

<p float="left">
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-first-time.png" width="45%">
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-login.png" width="45%">
</p>
<p align="center"><i>Figure 12: Login through VNC</i></p>

<p>After clicking OK button, it'll take a couple of seconds to show an interface as in Figure 13.</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-success-output.png">
<p align="center"><i>Figure 13: Raspberry PI desktop through VNC</i></p>

<p>That's it, now we can rock and roll by using either wired or wireless method.</p>

<h1>Upgrading the PI</h1>
<p>First, you need to make some upgrades on your PI via terminal.</p>

```
sudo apt-get update -y
sudo apt-get upgrade -y
```

<p>This will take about minutes or an hour to complete upgrading process.</p>
<p>After upgrading, reboot the PI by </p>

```
sudo reboot
```

<h1>Enabling Camera Option</h1>
<p>After rebooting, we need to enable the camera option for suuccessful object detection. To do this, open the terminal and type</p>

```
sudo raspi-config
```
<p>After issuing this command, you will be looking something as shown in figure 14</p>
<img src="https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/raspi-config.png">
<p align="center"><i>Figure 14: Raspi Config Interface</i></p>

<p>It'll be controlled by arrows. Go to Interface options and enable Camera or Legacy Camera. If you don't have that option, don't worry, we faced the same thing implying that camera is automatically in active state.</p>
<p>It requires rebooting, so issue the command given for rebooting</p>

<h1>Installing neccessary modules</h1>
<p>Here, we are going to install all required modules from pip and sudo. Issue the commands given below</p>

```
# Install Python development tools and package manager
sudo apt-get install python3-dev python3-pip

# TensorFlow is a machine learning library that can be used for object detection
# We upgrade it to ensure that we have the latest version with potential bug fixes and improvements
sudo pip3 install --upgrade tensorflow

# OpenCV (Open Source Computer Vision) is essential for computer vision tasks, including image processing and object detection
sudo apt-get install python3-opencv

# NumPy is a powerful library for numerical operations, commonly used in scientific computing and image processing
sudo apt-get install python3-numpy

# Matplotlib is a plotting library that can be useful for visualizing data and results
sudo apt-get install python3-matplotlib

# SciPy is a library for scientific computing and can complement NumPy for advanced functionality
sudo apt-get install python3-scipy

# pyttsx3 is a Python library that provides text-to-speech conversion
sudo pip3 install pyttsx3

# espeak is a compact software speech synthesizer that can be used by pyttsx3 for text-to-speech
# The -y flag automatically confirms the installation without requiring user input
sudo apt-get install -y espeak

# imutils is a collection of convenience functions for OpenCV, making it easier to work with image and video processing tasks
pip3 install imutils
```

<p>Simply copy and paste it, things followed by # (the description of a particular module being installed) are treated as comments by shell interpreter (Linux terminal in this case)</p>
<p>If you are facing the externally managed environment due to installing modules using pip, then simply remove the <code>EXTERNALLY-MANAGED</code> file by</p>

```
cd /usr/lib/python3.11 #Replace with your actual python version
sudo rm EXTERNALLY-MANAGED
```
<h1>Cloning this Rep</h1>
<p>You can clone this repository for implementing our project. Issue the command on Desktop for easy access.</p>

```
cd Desktop
git clone https://github.com/syed-sahil-100/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation.git
mv Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation.git blindhelper
```
<p>We are shrinking the path name, as remembering such a big name is tedious. You can give your own name. But recommended to keep the name as it is.</p>

<h1>Running the code</h1>
<p>Running the script creates a popup showing capture from your camera with detected objects with distance away from the camera. If an object or person is near to the blind (camera in this case), pyttsx3 module conveys the message in voice format like Move away. It can be run by</p>

```
python3 /home/pi/Desktop/blindhelper/objectdetector.py
```



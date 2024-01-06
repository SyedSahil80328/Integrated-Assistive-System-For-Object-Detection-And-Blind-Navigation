<h1>Integrated Assistive System For Object Detection And Blind Navigation</h1>
<p>Embark on a transformative journey towards enhanced accessibility and independence with our innovative repository, 'Integrated Assistive System for Object Detection and Blind Navigation.' This comprehensive solution seamlessly combines cutting-edge object detection capabilities and intelligent blind navigation technologies. Empower individuals with visual impairments to navigate their surroundings confidently, fostering a more inclusive and connected world.</p>
<h1>Basic Hardware Requirements</h1>
<ol>
<li>Raspberry PI 4 or higher (8GB Memory)</li>
<li>Micro SD Card (32GB or higher)</li>
<li>Raspberry PI adapter or battery</li>
<li>Raspberry PI cooler (Fan)</li>
<li>Audio device (Speaker or Headphones)</li>
<li>PI Camera or USB Webcam</li>
</ol>
<h1>Basic Installation</h1>
<p>Refer <a href="https://www.raspberrypi.com/documentation/computers/getting-started.html">here</a> for learning complete setup of your Raspberry PI.</p>
<p>Install the Raspberry PI imager by clicking <a href="https://www.raspberrypi.com/software/">this link.</a></p>
<p>Note: You can also install it with NOOBS <i>(New Out Of Box Software)</i> by clicking <a href="https://www.raspberrypi.com/news/introducing-noobs/">this link.</a></p>
<p>After installing, your Raspberry PI interface will look like this:</p>
<img src="https://www.raspberrypi.com/documentation/computers/images/recommended-software.png">
<h1>Upgrading the PI</h1>
<p>First, you'll need to make some upgrades on your PI via terminal</p>

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
After issuing this command, you will be looking something like this

```
Raspberry Pi 4 Model B Rev 1.5

┌─────────┤ Raspberry Pi Software Configuration Tool (raspi-config) ├──────────┐
│                                                                              │
│       1 System Options       Configure system settings                       │
│       2 Display Options      Configure display settings                      │
│       3 Interface Options    Configure connections to peripherals            │
│       4 Performance Options  Configure performance settings                  │
│       5 Localisation Options Configure language and regional settings        │
│       6 Advanced Options     Configure advanced settings                     │
│       8 Update               Update this tool to the latest version          │
│       9 About raspi-config   Information about this configuration tool       │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                     <Select>                     <Finish>                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```
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

<p>If you are facing the externally managed environment due to installing modules using pip, then simply remove the <code>EXTERNALLY-MANAGED</code> file by</p>

```
cd /usr/lib/python3.11 #Replace with your actual python version
sudo rm EXTERNALLY-MANAGED
```
<h1>Cloning this Rep</h1>
<p>You can clone this repository for implementing our project. Issue the command on Desktop for easy access.</p>

```
cd Desktop
git clone https://github.com/syed-sahil-100/Integrated-Assis
```

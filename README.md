# Integrated Assistive System For Object Detection And Blind Navigation

Embark on a transformative journey towards enhanced accessibility and independence with our innovative repository, **Integrated Assistive System for Object Detection and Blind Navigation.** This comprehensive solution seamlessly combines cutting-edge object detection capabilities and intelligent blind navigation technologies. Empower individuals with visual impairments to navigate their surroundings confidently, fostering a more inclusive and connected world.

*Note: Use Ctrl/Cmd+Click or Click scroll button on hyperlinks to retain our markdown file.*

# Basic Hardware Requirements
1. Raspberry PI Computer.<sup>*1*</sup>
1. Micro SD Card.<sup>*2*</sup>
1. Raspberry PI adapter or battery.
1. Raspberry PI Fan.
1. Any type of light weight cap.
1. Speaker or Headphones.<sup>*3*</sup>
1. PI Camera or USB Webcam.
1. Raspberry PI Case.
1. Raspberry PI Heatsink.

*<sup>1</sup>Version 4 or Higher with Main memory of 8 Gigabytes.*\
*<sup>2</sup>32 Gigabytes is sufficient, but 64 is recommended for development purpose and avoiding storage shortage.*\
*<sup>3</sup>Wired is recommended, as wireless connection requires desktop setting for initiating or manipulating connection.*

# Skipper Part

We request the absolute beginners to skip this skipper part and go to [What is Raspberry PI](https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation#what-is-raspberry-pi).

This markdown file is created with intention to provide clarified explanations for absolute beginners. So, it'll contain the steps for the one who are getting started with Raspberry PI Computer. If you are well aware of Raspberry PI and already using it through desktop mode or remote mode (SSH or VNC or both), we don't want you to waste time by scrolling down all the upcoming images. You can directly go to the steps for running the program for object detection with vocal assistance.

[Steps for running our project.](https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation#installing-neccessary-modules)

Note: If you haven't enabled the camera option (without enabling it makes our program to fail) though you have [upgraded the PI](https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation#upgrading-the-pi) (Click if you haven't upgraded it yet) please [don't skip it](https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation#enabling-camera-option).

# What is Raspberry PI?

Raspberry Pi is a series of small, affordable, single-board computers developed by the Raspberry Pi Foundation, a UK-based charity organization. The primary goal of the Raspberry Pi project is to promote computer science education and enable people of all ages to learn about programming and computing in a hands-on and cost-effective way.

Key features and aspects of Raspberry Pi include:

1. **Affordability:** Raspberry Pi boards are priced reasonably, making them accessible to a wide audience, including students, hobbyists, and professionals.
2. **Versatility:** Despite their small size, Raspberry Pi computers are versatile and can be used for various purposes, including desktop computing, programming, DIY projects, home automation, robotics, and more.
3. **Hardware:** Raspberry Pi boards typically include various ports for peripherals, GPIO (General Purpose Input/Output) pins for hardware interfacing, HDMI for video output, USB ports, and networking capabilities.
4. **Community and Support:** The Raspberry Pi community is large and active, with a wealth of online resources, forums, and tutorials. This strong community support contributes to the ease of learning and troubleshooting.
5. **Educational Value:** Raspberry Pi is widely used in schools and educational institutions to teach programming and computer science. Its low cost allows for widespread adoption in educational settings.
6. **DIY Projects:** Raspberry Pi is popular for DIY (Do It Yourself) projects, allowing enthusiasts to create custom solutions for various applications, such as media centers, home servers, retro gaming consoles, and more.
7. **Open Source:** The Raspberry Pi operating system, Raspbian (now called Raspberry Pi OS), is based on Linux and is open source. This encourages a culture of sharing and collaboration.
8. **Low Power Consumption:** Raspberry Pi boards are energy-efficient and have low power requirements, making them suitable for projects where power consumption is a concern.
9. **Continuous Development:** The Raspberry Pi Foundation regularly releases new models with improved hardware specifications, ensuring that the platform stays relevant and up-to-date.

The importance of Raspberry Pi lies in its role in democratizing access to computing and providing a platform for learning, experimentation, and innovation. It has become a valuable tool for introducing individuals, especially students, to the world of programming and electronics, fostering creativity and problem-solving skills. Additionally, its affordability and versatility make it an excellent choice for a wide range of practical applications in various fields.

# Basic Installation

Refer [here](https://www.raspberrypi.com/documentation/computers/getting-started.html) for learning the complete setup of your Raspberry PI.

[Download Raspberry PI Imager.](https://www.raspberrypi.com/software/)  
[Go through the installation of OS via NOOBS (*New Out Of Box Software*).](https://www.raspberrypi.com/news/introducing-noobs/)  
[Install NOOBS from the official GitHub repository of Raspberry PI.](https://github.com/raspberrypi/noobs)

However, the NOOBS is now obsolete and is not updated regularly. For getting a regularly updated Operating System, we recommend installing it with Raspberry PI Imager.

After installing, your Raspberry PI interface will look as shown in Figure 1.

![Raspberry PI Interactive OS](https://www.raspberrypi.com/documentation/computers/images/recommended-software.png)
<p align="center"><i>Figure 1: Raspberry PI Interactive OS</i></p>

# Setup Environment

We can have a laboratory environment both wired (just like a desktop computer) or wireless (through SSH or VNC).

For Wired setup, we require:

1. Monitor which supports HDMI port.<sup><i>1</i></sup>
2. Mouse.
3. Keyboard.
4. HDMI to micro HDMI cable or adapter.

<sup><i>1</i></sup>*If you have only VGA port in your monitor and it doesn't support audio, a VGA to HDMI adapter with an audio device is needed.*

For wireless usage, you should enable SSH as in Figure 2 when the imager has been installed for downloading the Operating System for Raspberry PI. Then issue the command.

```
ssh mass@192.168.xxx.xxx #Replace "mass" with your actual username and "192.168.xxx.xxx" with the actual detected IP address of your device.
```

<p float="left">
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/pi-imager.png" width="45%">
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/SSH-Save.png" width="45%">
</p>
<p align="center"><i>Figure 2: Enabling SSH by clicking Ctrl+Shift+X on Image 1 to open Image 2</i></p>

Then provide your password to get connected (give "yes" for the message after encountering a message if you are logging in for the first time).

You'll be logged in as shown in Figure 3.

![Login through SSH](https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/login-SSH.png)

<p align="center"><i>Figure 3: Login through SSH</i></p>

**Note:** Both PI and operating device must be on the same Wi-Fi network.  
**Tips:** After connecting the operating device to Wi-Fi, you can find the IP address through the application [Fing](https://www.fing.com/products/fing-desktop).

**To have a seamless experience, we recommend using the wired method as it is easy and doesn't require internet (except for installation and upgrading required modules).**

# Usage through VNC

Working through the SSH terminal the entire time could be tedious. Also, our program requires a GUI for showing the output. In that case, SSH fails to execute our program. So, to interactively work with Raspberry PI headlessly, we can use VNC which is a better alternative to SSH. VNC lets you work with PI on a GUI. To enable it, turn on your Raspberry PI and connect via your device through SSH. Then issue the command.

```
sudo raspi-config
```

Then select interface option by hitting enter button on <code>Interface Options</code> (Control through up/down arrow buttons) as shown in Figure 4.

![Figure 4: Raspi Config Interface](https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/raspi-config.png)
<p align="center"><i>Figure 4: Raspi Config Interface</i></p>

Then select VNC (Figure 5).

<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/config-interface.png">
<p align="center"><i>Figure 5: Selection of VNC</i></p>

Then select <code>Yes</code> (control by left/right arrow and hit enter) shown in Figure 6.

<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/interface-VNC.png">
<p align="center"><i>Figure 6: Enabling VNC</i></p>

After clicking yes, you'll see a couple of output as shown in Figure 7a and 7b.

<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-success-console.png">
<p align="center"><i>Figure 7a: Output of activation on console</i></p>
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-success.png">
<p align="center"><i>Figure 7b: Output of activation on raspi-config</i></p>

Select <code>OK</code> and hit finish.

<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/raspi-config-finish.png">
<p align="center"><i>Figure 8: Exiting the raspi-config</i></p>

Cool! We have now enabled VNC for working with Raspberry PI headlessly along with GUI. Next, head over to RealVNC viewer.<br><a href="https://www.realvnc.com/en/connect/download/viewer/">Download RealVNC viewer.</a>

After opening the viewer, create a new connection as shown in figure 9.

<p align="center"><img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-new.png" width="75%"></p>
<p align="center"><i>Figure 9: Creation of new connection</i></p>

<p>Then provide the same IP address that has been used during SSH login and any friendly name as indicated in figure 10.</p>
<p align="center"><img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-credentials.png" width="75%"></p>
<p align="center"><i>Figure 10: Providing neccessary details</i></p>

<p>Then, a computer icon as shown in Figure 11 is created. You can rename it by pressing F2. You need to click that icon and enter username and password as indicated in figure 12.</p>
<p align="center"><img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-new-user.png" width="75%"></p>
<p align="center"><i>Figure 11: New device creation</i></p>

<p float="left">
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-first-time.png" width="45%">
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-login.png" width="45%">
</p>
<p align="center"><i>Figure 12: Login through VNC</i></p>

<p>After clicking OK button, it'll take a couple of seconds to show an interface as in Figure 13.</p>
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/VNC-success-output.png">
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
<p>After issuing this command, you will be looking something as shown in figure 14.</p>
<img src="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation/blob/main/Manual%20Pictures/raspi-config.png">
<p align="center"><i>Figure 14: Raspi Config Interface</i></p>

<p>It'll be controlled by arrows. Go to Interface options and enable Camera or Legacy Camera. If you don't have that option, don't worry, we faced the same thing implying that camera is automatically in active state.</p>
<p>It requires rebooting, so issue the command given for <a href="https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation?tab=readme-ov-file#upgrading-the-pi" >rebooting</a>.</p>

<h1>Installing neccessary modules</h1>
<p>Here, we are going to install all required modules from pip and sudo. Issue the commands given below.</p>

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

<p>Simply copy and paste it, things followed by # (the description of a particular module being installed) are treated as comments by shell interpreter (Linux terminal in this case).</p>
<p>If you are facing the externally managed environment due to installing modules using pip, then simply remove the <code>EXTERNALLY-MANAGED</code> file by</p>

```
cd /usr/lib/python3.11 #Replace "3.11" with your actual python version
sudo rm EXTERNALLY-MANAGED
```
<h1>Cloning this Rep</h1>
<p>You can clone this repository for implementing our project. Issue the command on Desktop for easy access.</p>

```
cd Desktop
git clone https://github.com/SyedSahil80328/Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation.git
mv Integrated-Assistive-System-For-Object-Detection-And-Blind-Navigation.git blindhelper
```
<p>We are shrinking the path name, as remembering such a big name is tedious. You can give your own name. But recommended to keep the name as it is.</p>

<h1>Adjusting Terminal's Default Directory</h1>
<p>Amazingly, we can change the default directory that the terminal will open. To do this, we can edit the <code>.bashrc</code> file by running the command given below.</p>

```
nano ~/.bashrc
```

<p>Append the line given below at the end of the file.</p>

```
cd /home/mass/Desktop/blindhelper #Replace "mass" with your actual username
```

<p>Save it and close. On restarting it, the terminal should open with the specified location.</p>

<h1>Program Split Up</h1>
<p>It consists of three python codes with functionalities listed below:</p>
<ol>
<li><code>IASDriver.py</code>: The Main Object detection program.</li>
<li><code>ObjectDetectionConstants.py</code>: Contains required Constants for running the main script.</li>
<li><code>ObjectDetectionMethods.py</code>: Contains utility methods for running the main script.</li>
</ol>

<h1>Running the code</h1>
<p>Running the script creates a popup showing capture from your camera with detected objects with distance away from the camera. If an object or person is near to the blind (camera in this case), pyttsx3 module conveys the message in voice format like Move away. It can be run by</p>

```
python3 /home/mass/Desktop/blindhelper/IASDriver.py #Replace "mass" with your actual username
```

<p>You will see the output with video streaming. To quit, press q.</p>

<h1>Launching the code automatically</h1>
<p>If you want to demonstrate it as a software only project, then we optionally require to self start our script. Since we are doing it as a portable hardware product, we cannot rely everytime on SSH or VNC for manually starting it from our laptop. Raspberry PI offers you with a service file called crontab which accepts the shell commands and make the PI react accordingly in an automated manner. To do this, we have created a launcher script file which is present on the renamed folder (blindhelper in our case) which is the same folder as our python script presents. You are required to issue the command to open the crontab file.</p>

```
sudo crontab -e
```

<p><i>Note: For first time users of crontab, it'll show you a list of editors to be opened. Simply click the number which opens nano editor.</i></p>
<p>Now, we have opened our crontab file. Next, copy the below text and paste it at the end of file.</p>

```
@reboot Xvfb :1 -screen 0 1920x1080x24 & export DISPLAY=:1 && /home/mass/Desktop/blindhelper/launcher.sh > /home/mass/Desktop/blindhelper/cronlog 2>&1
```

<p>Save it and close. To make this command to work, you need to install a Virtual Framebuffer called Xvfb which is a tool that enables you to run graphical applications headlessly in the background without a monitor. Issue the command below.</p>

```
sudo apt-get install xvfb
```

<p>You can check it by running the command given below.</p>

```
chmod +x launcher.sh #Make it executable
xvfb-run -a ./launcher.sh
```

<p>After checking with your video streaming, simply reboot the Raspberry PI to make the edited crontab file to run at startup. After seeing with the desktop, you should be able to see the output with voice navigation automatically.</p>

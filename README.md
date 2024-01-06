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


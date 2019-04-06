# Arethru Twitch Notifier

-----

## Description

This is a program for windows that is intended to run in the background, and give notifications when a followed stream goes live on twitch.tv

This has been a long running project, and something that I built almost exclusively for own use in the beginning. Ignoring a few rough edges here and there, this is certainly a very usable program these days, with a wide array of features and customization options. More on this further down.

### Installation

To get started, head on over to the github download page and get the installer.

##### [Download Page](https://github.com/MartinHartmannJensen/TwitchNotifier/releases)

Once installed, click the "authorize" button under settings and complete the login. That's it. The program should now restart and function as you would expect. 

Check out the overview section here, to get an in-depth explanation of the program and what the different options do. There's also some features that aren't yet accessible with the user interface. More on this in the Features section.

------

## Overview

### Notification Window

This is the popup that occurs when someone new has gone live. When minimized, the program runs as a background app, and will show this window when appropriate. Clicking on a stream/name in this window, will launch the twitch.tv page in your default browser. If you want to use another browser, or something else entirely that you'd rather want to watch the streams with, then there's an option to configure that too. Check the section "Customizing Opening of Stream Links"

### Settings

Under the settings tab, you will find some options like changing the how long the window stays up, or whether or not the program should start with windows. If there is a setting that seems confusing; hover over it. This should show a tooltip describing what it does.

Settings for the program is stored in a text file under "ArethruNotifier" in documents. This is the central place for customizable stuff and settings the program use. This folder won't be removed per default when uninstalling (but it's always safe to get rid of).

### Follows

Although not strictly having something to do with displaying live notifications, this just exists as an overview of followed streams.

### How it Works

#### Privacy and Security

If feel it is important to mention that nothing is saved anywhere besides on the local machine, and that no clutter or remnants will be left behind on an uninstall. The config folder "ArethruNotifier" under documents should be safe to delete always, and will be generated on program startup.

Regarding your twitch account. This program of course uses the twitch API. This means that all account info is handled on their side and all the program uses, is its own identifier and a users unique identifying token that is saved after authorization.

#### Tech

The general concept is simple: Contact the twitch servers to ask for updates after a set interval time. The NewtonSoft JSON package is used to receive twitch responses. Early on I decided to use a homebrewed config system, created with inspiration from existing C# config systems. This can be found as another featured project on this site.

Also, I should mention how authorization is handled since that can look a bit confusing from the code side of things. So just a quick word on the login flow:

When sending a request to authorize a user, the user is given a login portal hosted on twitch's side. On a successful auth. the users browser is redirected to an address on the localhost. This is where the program can seem a bit weird, because it's essentially turned into a listening server, waiting to grab info from a browser pinging the local address.

------

## Features

There exists some handy features that has not yet gotten a proper interface in the program. Adding this is not a high priority, but something that can be done eventually. As of now these features are used by editing xml files, writing own batch scripts or manually writing to the config file.

### Favorites System

You can have custom sounds play for specified streams. If you know xml, this should be fairly straight forward to configure. If you don't, then let me explain.

In the same folder that you can find the config file, there's also a file called "favorites.xml". This file can be used to define streams that belong to certain groups with some unique attributes. The structure of the file looks like this:

```
<favorites>
	<group name="some unique name" priority="100" soundfile="coolSound.wav" poptime="3000">
      	<stream>A livestream channel name</stream>
  	</group>
</favorites>
```

The favorites tag can contain any number of group tags. The same is true for the group tag and stream tag. The stream tag should contain a type sensitive name of a twitch streamer. 
The group tag also has a few attributes that needs to be assigned, these are:

- **Name**: This just has to be unique from other group names 
- **Priority**: The higher number gets priority, if streamers from different groups go live at the same time (during the same notification) 
- **Soundfile**: This is the name of a ".wav" soundfile located in the folder "group sounds", that can be found alongside "favorites.xml"
- **Poptime**: How many seconds the notification window should be displayed.

### Customizing Opening of Stream Links

This is done with the file "StreamStart.cmd", by right clicking and choosing to edit it. In the settings tab, you can choose between launching the stream in your system default browser, or running this file. Found at "documents/ArethruNotifier/StreamStart.cmd".

Why not just make an option to choose your preferred browser, instead of having to edit this file? 

The reason for this is that some people like to watch streams with other software, and the use of windows command prompt allows for creative application. The clicked streams' name will be passed as a launch parameter (stored in variable %1) to StreamStart.cmd, and with twitch's url structure, that's all you should need to launch streams in any software with the command prompt.

An example of this could be launching google chrome in "app mode".

```
@echo off
START "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -app=https://twitch.tv/%1
```



### Color Scheme!

This is easily configured and can be essential if the whole dark/nightly theme isn't something you're a fan of. The whole program is designed to use 5 central colors for everything, and these can be set in the configuration file by editing it with your text editor of choice. Find the lines starting with "Color" to get started.


```
Color_Mainpanel=0
```

In this case 0 means "not set", and the program will use the default main panel color.

To change the color, use a hex color code.


```
;Color_Mainpanel=0    this line is out commented
Color_Mainpanel=#510022
```

To see changes take effect, restart the program. Using the semicolon can be handy for saving different color schemes. Any line starting with this symbol, will not be considered a setting by the program.
+++
title = "Tap User Manual"
description = "The user manual for 7III Tap, a MIDI controller for iPhone"
date = 2024-03-15
updated = 2024-04-12
[extra]
share = true
featured_image = "7III Tap Ableton Live Controller Device Center.jpg"
featured_image_alt = "7III Tap, a MIDI controller for Ableton Live"
+++
>This is the user manual for the MIDI controller app [7III Tap](/tap) for iPhone.


## Set Up
To run as an Ableton Live controller you will need to [add the Tap MIDI Remote Script](#add-the-tap-midi-remote-script) first. If you are only going to use the [Encoders](#encoders-view), then you can directly jump to [Connect your iPhone](#connect-your-iphone).

### Add the Tap MIDI Remote Script
<ol>
<li>On your computer, download the MIDI Remote Script at <a href="/tap/Tap.zip" download>project7iii.com/tap/Tap.zip</a>.</li>
<li>Manually create a folder called <code>Remote Scripts</code> within your User Library if it does not already exist. The default User Library location are:
 <blockquote class="list_block">
 <strong>Windows</strong><br><code>\Users\[username]\Documents\Ableton\User Library</code>
 <br>
 <br><strong>Mac</strong><br><code>Macintosh HD/Users/[username]/Music/Ableton/User Library</code>
 </blockquote>
 </li>
<li>Place the remote script folder called <code>Tap</code> into the <code>Remote Scripts</code> folder you just created.</li>
</ol>


### Connect your iPhone
<ol>
<li>Connect your iPhone to your computer using a USB cable.</li>
<li>Enable Connection:</li>
<blockquote class="list_block">
<strong>Windows</strong>
<ol>
<li>Try to use <a href="https://www.tobias-erichsen.de/software/rtpmidi.html">rtpMIDI</a> to connect your iPhone with your PC.<br>
If it works by simply connecting or an ad-hoc Wi-Fi network, please let us know and we will include it in this guide!<br>
You might also need some iOS drivers, as described <a href="https://www.copytrans.net/support/install-iphone-ipod-touch-and-ipad-drivers-without-installing-itunes/">here</a>.</li>
<li>???</li>
<li>Profit!</li>
</ol>
<br>
<strong>Mac</strong>
<ol>
<li>Open the app <strong>Audio MIDI Setup</strong>.</li>
<li>Open the <em>Audio Devices</em> window.<br>
If it is not already visible, select the <em>Window -&gt; Audio Devices</em> menu to display it.</li>
<li>Find your iOS device in the sidebar and click the <code>Enable</code> button.</li>
</ol>
</blockquote>
<li>Launch Live.</li>
<li>Open Live&#39;s Preferences and navigate to the <strong>MIDI</strong> tab.</li>
<li>Select the script <code>Tap</code> using the dropdown menu in the Control Surface column.</li>
<li>Assign your iPhone as input and output ports.</li>
</ol>

{{ image_sets(path="content/tap/manual/midi-settings-7iii-tap.png", format="auto", op="fit_width", quality=75, alt="7III MIDI setting in Ableton Live", caption='The right settings for Tap.') }}

## User Interface
There are 5 Views in Tap.  
The first is called [Options](#options) - here you can get infos and choose your options.  
The main Tap interfaces are the known views of Ableton Live: [Device View](#device-view), [Clip View](#clip-view) and [Mixer View](#mixer-view).  
Tap also has one extra view which are customizable encoder pages to control about anything that accepts MIDI CC: [Encoders](#encoders-view).

### Options
Tap `Connected to Ableton Live` and then `Play Tap` to play Tap.  
Tap `Test Tap without connection` to explore Tap without connection.  
Tap `Encoders` to get to the stand-alone encoders interface.  
You can change the order of view switching and set the default quantize settings.

### Main Views
Each view of the main Ableton Live controller engine has some of the same elements described below.

#### Tracks Bar
The top bar showing the tracks of your Live project.  
Navigate between tracks by swiping. To select a track, tap on it. Long-press opens the tracks context menu where you can delete tracks, add tracks, go to the [Options](#options) or [Encoders](#encoders-view).

#### Footer Bar
A deep dive into the buttons of the footer bar. Left to right. The footer bar is present in all the pages except the Options View.

##### Side Panel/Encoders
The side panel opens the options for the midi grid. Long-press opens the encoders view.  
In the mixer view the button shows up as the encoder button. You get to the encoders view by pressing it.

##### Navigation Buttons
Navigate the 3 main views via the arrow buttons. In the [Encoders](#encoders-view) this will mover forwards and backward in the encoder pages if you have more than one.  
Long-press on the left pointing arrow to undo, long-press on the other to redo.

##### Duplicate/Stop
In device view: Duplicates the selected clip. Long press shows a context menu.  
In the other views: Stops all the clips.

##### Quantize
Quantizes the notes of the clip selected.  
Long-press will show detailed quantize options.

##### Capture/Options
Capture in clips, captures the midi just played in the grid.  
In all other views this will get you back to the options view.

##### Record
Activates or deactivates the session record button.

##### Play/Stop
Starts or stops the playback.

### Device View
#### Devices Bar
The devices are shown here, you can navigate by swiping left or right. Select a device by tapping on it.  
Tap on the `+` to add a new random device. You can choose between adding a random sound, synth, drums (if you are in a MIDI track) or effect.

#### Banks Bar
Navigate and select banks of the chosen device here.

#### Encoders Section
The 8 encoders of the current bank.  
You can swipe from in between the encoders to get to adjacent banks directly.

<div>Activate an encoder by touching it<br>
<ul>
<li>Adjust the encoder value by moving your finger up or down.</li>
<li>Fine-tune the value by moving your finger left or right.</li>
</ul></div>

Double tap an encoder to reset to 0 (or center for Panning), triple tap to reset to center (63).

#### MIDI Grid
Play notes with the MIDI grid. You have the option of choosing from different scales, velocity modes, mood wheel, grids etc. via the side panel button in the [Footer Bar](#footer-bar).

### Clip View
Show the clips. Use the [Tracks Bar](#tracks-bar) to navigate horizontally, use the clips for navigating vertically. Start and stop clips by tapping on a clip. If you tap on an empty clip slot Tap will take you to the [Device View](#device-view). Long-press on any clip slot to bring up a context menu.

### Mixer View
Show the mixer section. Use the [Tracks Bar](#tracks-bar) to navigate.

### Encoders View
Shows custom encoder layouts. You can create a custom encoder layout, or load a previously created layout by tapping the button in the top right-hand corner and choose your adventure. Encoder layouts can have more than one page and you can choose the MIDI channel and CC for each encoder. Navigation of the pages is done through the [Footer Bar](#footer-bar) arrows.  
For encoder functionality check the [Encoders Section](#encoders-section).

<div class="footnote-definition"><p>Ableton Live is a trademark of Ableton AG, registered in the United States and other countries.
<br>iPhone is a trademark of Apple Inc., registered in the United States and other countries.</p></div>
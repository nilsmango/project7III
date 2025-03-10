+++
title = "Tap User Manual"
description = "The user manual for 7III Tap, a MIDI controller for iPhone & iPad"
[extra]
date = 2024-03-15
updated = 2025-03-10
share = true
featured_image = "7III Tap Ableton Live Controller Device Center.jpg"
featured_image_alt = "7III Tap, a MIDI controller for Ableton Live"
+++
>This is the user manual for the MIDI controller app [7III Tap](/tap) for iPhone and iPad.

## Quick Start
Below is a video to help you get started. It follows the Mac version of this manual, but most steps are similar for other systems. You can start by following along with the [Set Up](#set-up) section.

{{ youtube(id="CBXZ1DxyzfE", start="0") }}

## Set Up
Note: If you are only going to use the [Encoders](#encoders-view), then you can directly jump to [2. Connect your iPhone or iPad](#2-connect-your-iphone-or-ipad).

### 1. Add the Tap MIDI Remote Script
<ol>
<li>On your computer, download the MIDI Remote Script at <a href="/tap/Tap.zip" download>project7iii.com/tap/Tap.zip</a>.</li>
<li>Manually create a folder called <code>Remote Scripts</code> within your User Library if it does not already exist. The default User Library locations are:
 <blockquote class="list_block">
 <strong>Windows</strong><br><code>\Users\[username]\Documents\Ableton\User Library</code>
 <br>
 <br><strong>Mac</strong><br><code>Macintosh HD/Users/[username]/Music/Ableton/User Library</code>
 </blockquote>
 </li>
<li>Place the unzipped remote script folder called <code>Tap</code> into the <code>Remote Scripts</code> folder you just created.</li>
</ol>

### 2. Connect your iPhone or iPad
Note: If you have a Mac, MIDI over USB is the best way to connect your iPhone or iPad to Live. If you are never using MIDI over WiFi, you can disable `MIDI over WiFi enabled` in options.

#### Over USB (Mac Only)
<ol>
<li>Connect your device to your Mac using a USB cable.</li>
<li>Open the app <strong>Audio MIDI Setup</strong>.</li>
<li>Open the <code>Audio Devices</code> window.<br>
→ If it is not already visible, select the <code>Window</code> → <code>Audio Devices</code> menu to display it.</li>
<li>Find your iOS device in the sidebar and click the <code>Enable</code> button.</li>
</ol>

#### Over WiFi
<ol>
<li>Connect your device to the same WiFi as your computer (best would be an ad hoc WiFi network).</li>
<li>Configure RTP-MIDI:</li>
<blockquote class="list_block">
<strong>Windows</strong>
<ol>
<li>Download <a href="https://www.tobias-erichsen.de/wp-content/uploads/2020/01/rtpMIDISetup_1_1_14_247.zip">rtpMIDI</a>.</li>
<li>Follow this <a href="https://www.tobias-erichsen.de/software/rtpmidi/rtpmidi-tutorial.html" target="_blank">guide</a> to install rtpMIDI and connect your device (no <strong>Advanced Configuration</strong> necessary).</li>
</ol>
<br>
<strong>Mac</strong>
<ol>
<li>Simply follow this <a href="https://support.apple.com/en-ca/guide/audio-midi-setup/ams1012/mac" target="_blank">guide</a> (no need to do <strong>Step 9</strong>).</li>
</ol>
</blockquote>
</ol>

### 3. Set Up Live
<ol>
<li>Launch Live.</li>
<li>Open Live&#39;s Preferences and navigate to the <strong>MIDI</strong> tab.</li>
<li>Select the script <code>Tap</code> using the dropdown menu in the Control Surface column.</li>
<li>Assign your device or Network Session as input and output ports.</li>
<li>Activate <code>Track</code> and <code>Remote</code> for your active MIDI Ports.</li>
</ol>

{{ image_sets(path="content/tap/manual/midi-settings-7iii-tap.png", format="auto", op="fit_width", quality=75, alt="7III MIDI setting in Ableton Live", caption='The right settings for Tap.') }}

## User Interface
There are 5 views in Tap.  
The main Tap interfaces are the known views of Ableton Live: [Device View](#device-view), [Clip View](#clip-view) and [Mixer View](#mixer-view).  
Tap also has one extra view which are customizable encoder pages to control about anything that accepts MIDI CC: [Encoders](#encoders-view).

### Home
Select `Try to connect to Ableton Live` and then `Play Tap` to play Tap.  
Tap `Test Tap without Connection` to explore Tap without connection.  
Tap `Start Encoders` to get to the stand-alone encoders interface.  
Get `Help` and dive into `Settings`.

### Main Views
The main Ableton Live controller views share some common elements, described below.

#### Tracks Bar
The top bar showing the tracks of your Live project.  
Navigate between tracks by swiping left or right. To select a track, tap on it. A long-press opens the track’s context menu where you can delete tracks, add tracks, go to [Home](#home) or [Encoders](#encoders-view).

#### Footer Bar
Here's a detailed look at the buttons in the footer bar, from left to right: 

##### Side Panel/Encoders
The side panel opens the options for the midi grid. Long-press opens the encoders view.  
In the mixer view, the button shows up as the encoders button. You get to the encoders view by pressing it.

##### Navigation Buttons
Navigate the three main views via the arrow buttons. In the [Encoders](#encoders-view) this will move forward and backward in the encoder pages if you have more than one page.  
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
Starts or stops the playback. Long press shows a context menu for stopping and starting clips.

### Device View
#### Devices Bar
The devices are shown here, you can navigate by swiping left or right. Select a device by tapping on it.  
Tap on the `+` to add a new random device. You can choose between adding a random sound, synth, drums (if you are in a MIDI track) or effect.

#### Banks Bar
Navigate and select banks of the chosen device here.

#### Encoders Section
The 8 encoders of the current bank.  
You can swipe from in between the encoders to get to adjacent banks directly.

<div>Activate an encoder by touching it, then:<br>
<ul>
<li>Adjust the encoder value by moving your finger up or down.</li>
<li>Fine-tune the value by moving your finger left or right.</li>
</ul></div>

Double tap an encoder to reset to 0 (or center for Panning), triple tap to reset to center (63).

#### MIDI Grid
Play notes with the MIDI grid. You have the option of choosing from different scales, velocity modes, mood wheel, grids etc. via the side panel button in the [Footer Bar](#footer-bar).

#### Step Sequencer
Add notes by tapping and move them by dragging. Dragging slowly enables non-quantized fine movement. Change octaves using the side panel. Use the green rectangle at the top of the step sequencer to move the loop and perform other useful actions. Drag horizontally to navigate through the pages of the step sequencer. Drag the small rectangle at the end of a note to adjust its length.

### Clip View
Show the clips. Use the [Tracks Bar](#tracks-bar) to navigate horizontally, use the clips for navigating vertically. Start and stop clips by tapping on a clip. If you tap on an empty clip slot Tap will take you to the [Device View](#device-view). Long-press on any clip slot to bring up a context menu.

### Mixer View
Show the mixer section. Use the [Tracks Bar](#tracks-bar) to navigate.

### Encoders View
Shows custom encoder layouts. You can create a custom encoder layout, or load a previously created layout by tapping the button in the top right-hand corner and choose your adventure. Encoder layouts can include multiple pages. You can adjust the MIDI channel and CC for each encoder. The navigation of the pages is done through the [Footer Bar](#footer-bar) arrows.  
For encoder functionality check the [Encoders Section](#encoders-section).




<div class="footnote-definition"><p>Ableton Live is a trademark of Ableton AG, registered in the United States and other countries.
<br>iPhone and iPad are trademarks of Apple Inc., registered in the United States and other countries.</p></div>
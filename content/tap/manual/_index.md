+++
title = "Tap User Manual"
description = "The user manual for 7III Tap, a MIDI controller for iPhone & iPad"
[extra]
date = 2024-03-15
updated = 2025-05-15
share = true
featured_image = "mixer.jpg"
featured_image_alt = "7III Tap, a MIDI controller for Ableton Live"
+++

<a href="/tap" class="btn" id="yellowButton">← 7III Tap</a> <a href="/tap/videos" class="btn" id="yellowButton">Videos</a> <a href="/tap/support" class="btn" id="yellowButton">Support</a>

>Last Update: **{{ date_updated() }}**  
>If you find any mistakes or notice anything missing in this User Manual, please reach out and let us know!

<!-- toc -->

## 1. Quick Start
Below is a video to help you get started. It follows the Mac version of this manual, but most steps are similar for other systems. You can start by following along with the [Set Up](#2-set-up) section.

{{ youtube(id="CBXZ1DxyzfE", start="0") }}

## 2. Set Up
Note: If you are only going to use the [Encoders](#3-6-encoders-view), then you can directly jump to [Connect your iPhone or iPad](#2-2-connect-your-iphone-or-ipad).

### 2.1 Add the Tap MIDI Remote Script
<ol>
<li>On your computer, download the MIDI Remote Script at <a href="/tap/Tap.zip" download>project7iii.com/tap/Tap.zip</a>.</li>
<li>Manually create a folder called <code>Remote Scripts</code> within your User Library if it does not already exist. The default User Library locations are:
 <blockquote class="list_block">
 <strong>Windows</strong><br><code>\Users\[username]\Documents\Ableton\User Library</code>
 <br>
 <br><strong>Mac</strong><br><code>Macintosh HD/Users/[username]/Music/Ableton/User Library</code>
 </blockquote>
 </li>
<li>Place the unzipped remote script folder called <strong>Tap</strong> into the <strong>Remote Scripts</strong> folder you just created.</li>
</ol>

### 2.2 Connect your iPhone or iPad
Note: If you have a Mac, MIDI over USB is the best way to connect your iPhone or iPad to Live. If you are never using MIDI over WiFi, you can disable **MIDI over WiFi enabled** in Settings.

#### 2.2.1 Over USB (Mac Only)
<ol>
<li>Connect your device to your Mac using a USB cable.</li>
<li>Open the app <strong>Audio MIDI Setup</strong>.</li>
<li>Open the <strong>Audio Devices</strong> window.<br>
→ If it is not already visible, select the <strong>Window</strong> → <strong>Audio Devices</strong> menu to display it.</li>
<li>Find your iOS device in the sidebar and click the <strong>Enable</strong> button.</li>
</ol>

#### 2.2.2 Over WiFi
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

### 2.3 Set Up Live
<ol>
<li>Launch Live.</li>
<li>Open Live&#39;s Preferences and navigate to the <strong>MIDI</strong> tab.</li>
<li>Select the script <strong>Tap</strong> using the dropdown menu in the Control Surface column.</li>
<li>Assign your device or Network Session as input and output ports.</li>
<li>Activate <strong>Track</strong> and <strong>Remote</strong> for your active MIDI ports.</li>
</ol>

{{ image_sets(path="content/tap/manual/midi-settings-7iii-tap.png", format="auto", op="fit_width", quality=75, alt="7III Tap MIDI setting in Ableton Live", caption='The correct settings for Tap. Set Takeover Mode to "None" for the best experience.' imgset_class="imgset-twothird") }}

## 3. User Interface
There are 5 views in Tap.  
The main Tap interfaces are the familiar views of Ableton Live: [Device View](#3-3-device-view), [Clips View](#3-4-clips-view), and [Mixer View](#3-5-mixer-view).  
Tap also has one extra view, which are customizable encoder pages to control just about anything that accepts MIDI CC: [Encoders](#3-6-encoders-view).

### 3.1 Home View
Select **Try to connect to Ableton Live** and then **Play Tap** to play Tap.  
Tap **Test Tap without Connection** to explore Tap without connection.  
Tap **Start Encoders** to go straight to the standalone [Encoders View](#3-6-encoders-view).  
Also available in the Home View: **Help** and **Settings**.

### 3.2 Main Views
The main Ableton Live controller views share some common elements, described below.

#### 3.2.1 Tracks Bar
The top bar showing the tracks of your Live project. A little half circle at the start or end indicates that there are more tracks to be found in that direction. 
{{ image_sets(path="content/tap/manual/Tracks Bar.jpeg", format="auto", op="fit_width", quality=75, alt="7III Tap Tracks Bar", caption='The Tracks Bar.') }}
Navigate between tracks by swiping left or right. To select a track, tap on it. The currently selected track is displayed in bold font.   
When you tap on a track that is already selected, you switch the main view!
A long-press opens the track’s context menu where you can add tracks, delete tracks, configure the standard note length for the step sequencers, go [Home](#3-1-home-view), or go to [Encoders](#3-6-encoders-view).

{{ image_sets(path="content/tap/manual/Tap_tracks_context_menu.jpg", format="auto", op="fit_width", quality=75, alt="Tracks Bar Context Menu", caption='The Tracks Bar context menu.' imgset_class="imgset-twothird") }}

#### 3.2.2 Footer Bar
Here's a detailed look at the buttons in the footer bar:

{{ image_sets(path="content/tap/manual/Footer_Bar.jpg", format="auto", op="fit_width", quality=75, alt="Tap Footer Bar", caption='The Footer Bar buttons.' imgset_class="imgset-twothird") }}

1. Side Panel/Encoders Button  
The side panel opens the options side panel in the [Device View](#3-3-device-view), where you will find layout, velocity, pitch-bend/modwheel, scale, root, and octave/drums page.  
In the Clips and Mixer Views, this button activates the Scene Launch buttons.
Long-press opens the [Encoders View](#3-6-encoders-view). 

2. Navigation Buttons  
Navigate the three main views via the arrow buttons. In the [Encoders View](#3-6-encoders-view), this will move forward and backward through the encoder pages if you have more than one page.  
Long-press on the left-pointing arrow to undo; long-press on the other to redo.  
In the [Home View](#3-1-home-view) Settings, you can disable navigation with these buttons to undo and redo with a single tap. With this setting enabled, you will need to use the [Tracks Bar](3-2-1-tracks-bar) for navigation instead.

3. Duplicate/Stop
In Device View: Duplicates the selected clip. Long-press shows a context menu where you can duplicate the selected scene.  
In the other views: Stops all the clips.

4. Quantize  
Quantizes the notes of the selected clip.  
Long-press will show detailed quantize options.

5. Capture/Double Loop/Home  
In [Device View](#3-3-device-view), with a keyboard or pads active, this captures the MIDI just played.  
If you are in the step sequencer layout, this will double the selected loop.  
In all other views, this will get you back to the [Home View](#3-1-home-view).

6. Record  
Activates or deactivates the session record button.

7. Play/Stop  
Starts or stops the playback. Long-press shows a context menu for stopping and starting clips.

### 3.3 Device View
#### 3.3.1 Devices Bar
The devices are shown here; you can navigate by swiping left or right. Select a device by tapping on it.  
Tap the ⊕ symbol to add a new random device. You can choose between adding a random sound, synth, drums (if you are in a MIDI track), or effect.
{{ image_sets(path="content/tap/manual/Devices Bar.jpeg", format="auto", op="fit_width", quality=75, alt="7III Tap Devices Bar", caption='The Devices Bar.') }}

#### 3.3.2 Banks Bar
Navigate and select banks of the chosen device here.

#### 3.3.3 Encoders Section
The 8 encoders of the current bank.  
You can swipe from in between the encoders to directly get to adjacent banks.

{{ image_sets(path="content/tap/manual/Encoders Section.jpeg", format="auto", op="fit_width", quality=75, alt="7III Tap Encoders Section", caption='The Encoders Section with the Banks Bar above.') }}

Activate an encoder by touching it, then:
- Adjust the encoder value by moving your finger up or down.
- Fine-tune the value by moving your finger left or right.


Double-tap an encoder to reset to 0 (or center for Panning); triple-tap to reset to center (63).

#### 3.3.4 MIDI Grid
Play notes with the MIDI grid. The pads show names if you are in a drum rack. Many keyboard and pad layouts are available. Root notes are in a different color than the rest of the pads.  
You have the option of choosing different scales, velocity modes, mod wheel, pitch wheel, layouts, and more via the side panel button in the [Footer Bar](#3-2-2-footer-bar).

{{ image_sets(path="content/tap/manual/MIDI pads.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap MIDI grid", caption='One of the many MIDI grid pads layouts.') }}

#### 3.3.5 Step Sequencer
Add notes by tapping, and move them by dragging. Dragging slowly enables non-quantized fine movement.  
Each note you add will have the velocity set in the side panel (see button one in the [Footer Bar](#3-2-2-footer-bar))
Drag horizontally to navigate through the pages of the step sequencer. 

Let's dive into the Tap step sequencer in detail:
{{ image_sets(path="content/tap/manual/Step_Sequencer.jpg", format="auto", op="fit_width", quality=75, alt="Tap Step Sequencer", caption='The Step Sequencer.' imgset_class="imgset-twothird") }}

1. The Start and Stop are marked with dark triangles.
2. The looped section is indicated by the band on top of the step sequencer and two lines at the start and end of the loop all in the color of the track.
3. Octave starts are marked with a horizontal line in the background.
4. Notes are indicated as rectangles in the track color.
5. Each note has an end rectangle. Drag the small rectangle at the end of a note to adjust its length. On iPhone, this might be a bit tricky to do; that is why we have added a context menu to the [Tracks Bar](#3-2-1-tracks-bar), where you can adjust the standard length.
6. The third track-colored line indicates the playing position.
7. These numbers show current page followed by total number of pages for this clip.
8. Shows clip playback status: solid play symbol (▶) means this clip is playing. An outline (▷) means a different clip on the same track is playing. A play symbol with a dash means no clip on this track is playing.
9. The Lil Green Helper rectangle. You can move the green rectangle by dragging it. Tap on it to open the menu. In the menu, you can move the loop and perform other useful actions like changing the drums page or octave. You can also change octaves/pages by using the side panel.  

When you tap the Lil Green Helper rectangle, you will see the following menu:

{{ image_sets(path="content/tap/manual/Step Seq Context Menu.jpg", format="auto", op="fit_width", quality=75, alt="Tap Step Sequencer Context Menu", caption='The Lil Green Helper menu.', imgset_class="imgset-half") }}

1. Move helper buttons: Use these if you don't want to drag the Lil Green Helper by hand. Moves the green rectangle to the start or end of the sequencer window.
2. Move buttons: Move up and down the octave in instruments, and up and down the drums page for drums.
3. See 2.
4. Page to Clip Start/End: Moves the sequencer page to the start/end of the clip.
5. Page to Loop Start/End: Moves the sequencer page to the start/end of the loop.
6. Crop Clip: Crops the clip to the loop length.
7. Move Loop Start/End & Loop: Moves the start/end of the loop and the whole loop (this means no change in loop length) to where the Lil Green Helper rectangle sits.
8. Move Loop Start/End: Only moves the start/end of the loop to where the Lil Green Helper rectangle sits. This will change the length of the loop.
9. See 7.
10. See 8.
12. Stop playing Clip: Will stop the playing clip.
13. To playing Clip: Will move the selection (and the step sequencer) to the playing clip.
14. New empty Clip: Will create a new empty clip and select it.
15. & 16. Start/End Marker: Moves the start/end marker to the Lil Green Helper rectangle.


### 3.4 Clips View
Shows the clips. Use the [Tracks Bar](#3-2-1-tracks-bar) to navigate horizontally; drag in the Clips View for navigating vertically.  
Start and stop clips by tapping on a clip. If you tap on an empty clip slot, Tap will take you to the [Device View](#3-3-device-view). Long-press on any clip slot to bring up a context menu.  
Pressing the Side Panel button in the [Footer Bar](#3-2-2-footer-bar) activates the Scene Launch buttons to launch scenes.  
The selected device's Banks Bar and Encoders Section are displayed above the clip view, exactly like in the Device View.

{{ image_sets(path="content/tap/manual/clips.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Clips View", caption='The Clips View.') }}

### 3.5 Mixer View
Shows the mixer section. Use the [Tracks Bar](#3-2-1-tracks-bar) to navigate. Double-tap the volume fader to set the volume to zero. Use sends, panning, mute, and solo at your discretion.  
Below the mixer section, there is a compact Clips View that allows you to interact with clips.  
Pressing the Side Panel button in the [Footer Bar](#3-2-2-footer-bar) activates the Scene Launch buttons to launch scenes.

{{ image_sets(path="content/tap/manual/mixer.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Mixer View", caption='The Mixer View.') }}

### 3.6 Encoders View
Shows custom encoder layouts. You can create a custom encoder layout, or load a previously created layout by tapping the button in the top right-hand corner and choosing your adventure. Encoder layouts can include multiple pages. You can adjust the name, MIDI channel, and CC for each encoder. The navigation of the pages is done through the [Footer Bar](#3-2-2-footer-bar) arrows.  
For encoder functionality, check the [Encoders Section](#3-3-3-encoders-section).




<div class="footnote-definition"><p>Ableton Live is a trademark of Ableton AG, registered in the United States and other countries.
<br>iPhone and iPad are trademarks of Apple Inc., registered in the United States and other countries.</p></div>
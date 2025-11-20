+++
title = "Tap User Manual"
description = "The user manual for 7III Tap, a MIDI controller for iPhone & iPad"
[extra]
date = 2024-03-15
updated = 2025-11-20
share = true
featured_image = "mixer.jpg"
featured_image_alt = "7III Tap, a MIDI controller for Ableton Live"
+++

<a href="/tap" class="btn" id="yellowButton">← 7III Tap</a> <a href="/tap/videos" class="btn" id="yellowButton">Videos</a> <a href="/tap/support" class="btn" id="yellowButton">Support</a> <a href="/tap/history" class="btn" id="yellowButton">Version History</a>

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
This is where every adventure starts.
- Select **Try to connect to Ableton Live** and then **Play Tap** to play Tap.  
- Tap **Test Tap without Connection** to explore Tap without connection.  
- Tap **Start Encoders** to go straight to the standalone [Encoders View](#3-6-encoders-view).  
- Also available in the Home View: **Help** and [Settings](#3-1-1-settings).

### 3.1.1 Settings
In Settings you can configure very useful things, like the connection or touch indicators (great for tutorials etc.).
- You will also find a button to enable/disable all **Performance Features**.

### 3.2 Main Views
The main Ableton Live controller views share some common elements, described below.

#### 3.2.1 Tracks Bar
The top bar showing the tracks of your Live project.
{{ image_sets(path="content/tap/manual/Tracks Bar.jpeg", format="auto", op="fit_width", quality=75, alt="7III Tap Tracks Bar", caption='The Tracks Bar.') }}
- A little half circle at the start or end indicates that there are more tracks to be found in that direction. 
- Navigate between tracks by swiping left or right. To select a track, tap on it. The currently selected track is displayed in bold font.   
- When you tap on a track that is already selected, you switch the main view!
- A long-press opens the track's context menu where you can:
  - add track
  - delete track
  - toggle arm of the track (if audio track)
  - activate "select a drum pad without playing it" (only with active drum pad layout)
  - configure the standard note length (only with active step sequencer)
  - go [Home](#3-1-home-view)
  - go to [Encoders](#3-6-encoders-view)

{{ image_sets(path="content/tap/manual/Tap_tracks_context_menu.jpg", format="auto", op="fit_width", quality=75, alt="Tracks Bar Context Menu", caption='The Tracks Bar context menu.' imgset_class="imgset-twothird") }}

#### 3.2.2 Footer Bar
Here's a detailed look at the buttons in the Footer Bar in vertical mode:

{{ image_sets(path="content/tap/manual/Footer_Bar.jpg", format="auto", op="fit_width", quality=75, alt="Tap Footer Bar", caption='The Footer Bar buttons in the step sequencers.' imgset_class="imgset-twothird") }}

Here is the Footer Bar in horizontal mode in the [Device View](#3-3-device-view), in all other views it looks like the one above, simply turned 90 degrees:
{{ image_sets(path="content/tap/manual/Footer_Bar_Horizontal.jpg", format="auto", op="fit_width", quality=75, alt="Tap Footer Bar in horizontal mode", caption='The horizontal Footer Bar in the step sequencers.' imgset_class="imgset-twothird") }}

1. Side Panel/Encoders Button  
The side panel opens the options side panel in the [Device View](#3-3-device-view), where you will find layout, velocity, pitch-bend/modwheel, scale, root, and octave/drums page.  
In the Clips and Mixer Views, this button activates the Scene Launch buttons.
Long-press opens the [Encoders View](#3-6-encoders-view). 

2. Navigation Buttons  
In Device view you can use these buttons to move up and down through the octaves/drums pages and going forward and backwards through the [Step Sequencer](#3-3-5-step-sequencer) pages. To change the mode, you simply swipe left or right over the navigation buttons. 
Long-press on the left-pointing arrow to undo; long-press on the other to redo. 
In the rest of the views, the buttons will simply be undo and redo (arrows in circle means undo redo).  
If you deactivate the **Performance Features** in [Settings](#3-1-1-settings) you can navigate the three main views via the arrow buttons. In the [Encoders View](#3-6-encoders-view), this will move forward and backward through the encoder pages if you have more than one page.  
 

3. Duplicate/Stop
In Device View: Duplicates the selected clip. Long-press will duplicate the selected scene.  
In the other views: Stops all the clips.

4. Quantize  
Quantizes the notes of the selected clip.  
Long-press will show detailed quantize options.

5. Capture/Double Loop/Home  
In [Device View](#3-3-device-view), with a keyboard or pads active, this captures the MIDI just played.  
If you are in the [Step Sequencer](#3-3-5-step-sequencer) layout, this will double the selected loop.  
In all other views, this will get you back to the [Home View](#3-1-home-view).

6. Record  
Activates or deactivates the session record button.

7. Play/Stop/Play Menu/Tempo
In the step sequencer with **Performance Features**: Single Tap opens that menu. Long-press opens the Tempo Overlay (see below).  
In all other layouts and views: Starts or stops the playback. Long-press opens the tempo overlay.  
In the [Step Sequencer](#3-3-5-step-sequencer) without **Performance Features**: Long-press shows a context menu for stopping, starting, adding, going to clips + tempo.  

Extra buttons in the horizontal Footer Bar of the Device View:  

8. Switch from Pads to Sequencer and vice versa.

9. Go to start of loop (only in Sequencer), stop all clips (in Pads)
  
Tempo Overlay
{{ image_sets(path="content/tap/manual/Tempo_Overlay.jpg", format="auto", op="fit_width", quality=75, alt="Tap Tempo Overlay", caption='The Tempo Overlay' imgset_class="imgset-twothird") }}
Tapping the plus and minus buttons will adjust the tempo by the amount indicated in the center.  
Tapping on the BPM digits lets you type in the exact tempo you want.


### 3.3 Device View
#### 3.3.1 Devices Bar
The devices are shown here.
- You can navigate by swiping left or right. 
- Select a device by tapping on it. The selected device has a bold font. 
- Tap the ⊕ symbol to add a new random device. You can choose between adding a random sound, synth, drums (if you are in a MIDI track), or effect.
- < (open) and > (closed) symbols indicate rack mothers. You can open and close racks by tapping on a selected rack mother. Chain start and ends are indicated by corner brackets. The chain number is indicated with cirlces below the first member of the chain (for more than one chain per rack mother).

{{ image_sets(path="content/tap/manual/Devices Bar.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Devices Bar", caption='The Devices Bar.') }}

#### 3.3.2 Banks Bar
Navigate and select banks of the chosen device here.

{{ image_sets(path="content/tap/manual/Encoders Section.jpeg", format="auto", op="fit_width", quality=75, alt="7III Tap Encoders Section", caption='The Banks Bar with the Encoders Section below.') }}

#### 3.3.3 Encoders Section
The 8 encoders of the current bank.  
- You can swipe from in between the encoders to directly get to adjacent banks.
- Activate an encoder by touching it, then:
  - Adjust the encoder value by moving your finger up or down.
  - Fine-tune the value by moving your finger left or right.
- Double-tap an encoder to reset to 0 (or center for Panning); triple-tap to reset to center (63).
- Encoders with active automation have a small circle in the top left corner, in the color of the track. If the circle is gray, it means the automation is not active.

{{ image_sets(path="content/tap/manual/encoder.jpg", format="auto", op="fit_width", quality=75, alt="Tap Encoder", caption='An Encoder with active automation' imgset_class="imgset-twothird") }}

#### 3.3.4 MIDI Grid
The MIDI grid is for playing notes (huge surprise!).  
- The pads show names if you are in a drum rack, the note names if in a MIDI track.  
- Root notes are in a different color than the rest of the pads. If you are in a drum rack, the selected drum pad is in the channel color.  
- You have the option of choosing different scales, velocity modes, mod wheel, pitch wheel, layouts, and more via the Side Panel button in the [Footer Bar](#3-2-2-footer-bar).  
- Many keyboard and pad layouts are available. The layouts **Keys** and **7 Pads** are velocity-sensitive - the higher up you hit a pad, the greater the velocity. You can invert or fix the velocity in the Side Panel.
- Notes played by the playing clip are lit up.

{{ image_sets(path="content/tap/manual/MIDI pads.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap MIDI grid", caption='One of the many MIDI grid pads layouts.') }}

#### 3.3.5 Step Sequencer
Step sequence away!
- Add notes by tapping, and move them by dragging. Dragging slowly enables non-quantized fine movement.  
- Drag up or down in the little rectangle at the end of a note to change the velocity of that note.  
- Drag left or right in the little rectangle at the end of a note to change the length of that note.  
- Each note you add will have the velocity set in the Side Panel (see button 1 in the [Footer Bar](#3-2-2-footer-bar)).
- Without **Performance Features**: Drag horizontally on the background to navigate through the pages of the Step Sequencer. With **Performance Features** you only change pages with the Footer Bar arrows.
- Without **Performance Features**: Drag vertically first on the background to activate [Selection Mode](#3-3-5-1-selection-mode). With **Performance Features** enabled you can simply drag on the background to activate Selection Mode.
- Long press on a note to also enter Selection Mode (or if already in Selection Mode, this will add/remove the note from the selection).
- Change the drums page or octave using the Side Panel, or the up/down buttons in the Footer Bar - available in landscape mode or when **Performance Features** are enabled (see [Footer Bar](#3-2-2-footer-bar) button 2).
- To select a drum pad, long press on an empty step in the Step Sequencer.

Let's dive into the Tap Step Sequencer in detail:
{{ image_sets(path="content/tap/manual/Step_Sequencer.jpg", format="auto", op="fit_width", quality=75, alt="Tap Step Sequencer", caption='The Step Sequencer.' imgset_class="imgset-twothird") }}

1. The Start and Stop are marked with dark triangles.
2. The looped section is indicated by the band on top of the step sequencer and two lines at the start and end of the loop all in the color of the track.
3. Octave starts are marked with a horizontal line in the background. For drums, it is the selected drum pad that is marked.
4. Notes are indicated as rectangles in the track color.
5. Each note has an end rectangle. Drag the small rectangle at the end of a note to adjust its length. On iPhone, this might be a bit tricky to do; that is why we have added a context menu to the [Tracks Bar](#3-2-1-tracks-bar), where you can adjust the standard length.
6. The third track-colored line indicates the playing position.
7. These numbers show current page followed by total number of pages for this clip.
8. Shows clip playback status: solid play symbol (▶) means this clip is playing. An outline (▷) means a different clip on the same track is playing. A play symbol with a dash means no clip on this track is playing.
9. The Lil Green Helper rectangle. You can move the green rectangle by dragging it. Tap on it to open the menu. In the menu, you can move the loop and perform other useful actions like changing the drums page or octave. You can also change octaves/pages by using the side panel.  

When you tap the Lil Green Helper rectangle, you will see the following menu:

{{ image_sets(path="content/tap/manual/Step Seq Context Menu.jpg", format="auto", op="fit_width", quality=75, alt="Tap Lil Green Helper menu", caption='The Lil Green Helper menu.', imgset_class="imgset-half") }}

1. Move helper to End/Start: Use these if you don't want to drag the Lil Green Helper by hand. Moves the green rectangle to the start or end of the sequencer window.
2. Page to Clip Start/End: Moves the sequencer page to the start/end of the clip.
3. Page to Loop Start/End: Moves the sequencer page to the start/end of the loop.
4. Crop Clip: Crops the clip to the loop length.
5. Move Loop Start/End & Loop: Moves the start/end of the loop and the whole loop (this means no change in loop length) to where the Lil Green Helper rectangle sits.
6. Move Loop Start/End: Only moves the start/end of the loop to where the Lil Green Helper rectangle sits. This will change the length of the loop.
7. Start/End Marker: Moves the start/end marker to the Lil Green Helper rectangle.

##### 3.3.5.1 Selection Mode
Enter Selection Mode by either selecting notes or long-pressing on a note. Selected notes and range are highlighted in light-blue.
Selections work the same way as in Ableton Live. You can add or subtract from a selection by dragging the selection square accordingly. You can also long-press on a selected note to deselect it. You can also add and subtract from the range of the selection, without selecting additional notes. This is important for duplication and copy pasting.  
You can move around selected notes by dragging one of them. You can also adjust the velocity and the length of all the selected notes by simply editing one of them. As this can be finicky, especially when playing live, we have added an edit overlay for easy and quick editing (see below).
Info: You can't undo and redo selections.

{{ image_sets(path="content/tap/manual/Footer_Bar_Selection_mode.jpg", format="auto", op="fit_width", quality=75, alt="Tap Footer Bar in Selection Mode", caption='The Footer Bar buttons in Selection Mode.' imgset_class="imgset-twothird") }}

Once in Selection Mode, there are several new [Footer Bar](#3-2-2-footer-bar) buttons available, here are the new ones:
1. Trash: Deletes the selected notes.
4. Edit Overlay: Opens and closes the edit overlay.
6. Modulation Menu: Opens and closes the modulation menu.
7. Selection Menu: Opens and closes the selection menu.

**Edit Overlay**  
{{ image_sets(path="content/tap/manual/Edit_Overlay.jpg", format="auto", op="fit_width", quality=75, alt="Tap MIDI Notes Edit Overlay", caption='The notes Edit Overlay.' imgset_class="imgset-twothird") }}
1. Velocities of the selected notes. Drag to increase and decrease. Takes effect on letting go.
2. Probabilities of the selected notes. Drag to increase and decrease. Takes effect on letting go.
3. Copy button. Copies the selected range and notes into the copy buffer. To paste either press the Paste button (pastes buffer at start of selected range) or tap any grid cell. You can also paste in other clips etc.
4. Lengthen/shorten button. Lengthens or shortens the selected notes by one grid cell. On long-press, prolongs or shortens by one beat. On swipe you can change to x2 and /2 buttons. These multiply or divide the duration of the selected notes by 2.
5. Cut button. Cuts the selected range and notes into the copy buffer. To paste, see "3. Copy button".
6. Duplicate button. Duplicates the selected range and notes to the end of the selected range.
7. Page indicator. Tap it or swipe on it to change the elongate/shorten buttons to x2 and /2 buttons.
8. Move buttons. Left and right moves the selected range and notes by one grid. Long-press moves the selected range and notes by one beat. Up and down moves the selected range and notes by one scale step. Long-press moves the selected notes by one octave.

**Modulation Menu**  
{{ image_sets(path="content/tap/manual/Modulation_Menu.jpg", format="auto", op="fit_width", quality=75, alt="Tap MIDI notes modulation menu", caption='The Modulation Menu.' imgset_class="imgset-twothird") }}
There are four modulation categories:  
- Timing
  - Random will get you random timings inside the selected range.
  - Vary will vary the timing of the selected notes by up to 4 grid cells
  - Reverse reverses the timing of the selected notes inside the selected range.
  - Falling person will humanize the timing.
- Pitch
  - Shuffle will shuffle the pitches of the selected notes.
  - Vary will vary the pitches of the selected notes by up to 4 semitones.
  - Invert will invert the pitches of the selected notes.
- Velocity
  - Random will randomize the velocities of the selected notes.
  - Vary will vary the velocities of the selected notes by up to 30% or so.
- Probability
  - Random will randomize the probabilities of the selected notes.
  - Vary will vary the probabilities of the selected notes by up to 30% or so.

**Selection Menu**  
You can: 
- select all notes
- invert the selection
- randomize the selection

### 3.4 Clips View
{{ image_sets(path="content/tap/manual/clips.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Clips View", caption='The Clips View.') }}

Shows the clips. 
- Use the [Tracks Bar](#3-2-1-tracks-bar) to navigate horizontally; drag in the Clips View for navigating vertically.  
- Start and stop clips by tapping on a clip. If you tap on an empty clip slot in a MIDI Track, Tap will take you to the [Device View](#3-3-device-view). If you tap an empty clip in an armed audio track (arm by long-press in the Tracks Bar, then tap "Toggle Arm"), the recording will start. Tap it again to stop the recording.
- Long-press on any clip slot to bring up a context menu (see below).  
- Pressing the Side Panel button in the [Footer Bar](#3-2-2-footer-bar) activates the Scene Launch buttons to launch scenes.  
- The selected device's Banks Bar and Encoders Section are displayed above the clip view, exactly like in the Device View.

**Clip Slot Context Menu**
{{ image_sets(path="content/tap/manual/Clip_Slot_Menu.jpg", format="auto", op="fit_width", quality=75, alt="Tap Clip Slot menu", caption='The Clip Slot Menu.' imgset_class="imgset-twothird") }}

Inside the context menu, you can:
- Select the clip/clip slot
- Duplicate the scene
- if a clip is on the slot:
  - Duplicate the loop of the clip
  - Stop the clip
  - Append the clip to another clip
    - Simply tap on the clip you want to append to. The original clip will get added to the end of the tapped clip. The original clip will get removed.
  - Copy the clip 
    - To paste simply tap on an empty clip slot
  - Duplicate the clip
  - Delete the clip


### 3.5 Mixer View
Shows the mixer section. 
- Use the [Tracks Bar](#3-2-1-tracks-bar) to navigate. 
- Double-tap the volume fader to set the volume to zero. Use sends, panning, mute, and solo at your discretion.  
- Below the mixer section, there is a compact Clips View that allows you to interact with clips.  
- Pressing the Side Panel button in the [Footer Bar](#3-2-2-footer-bar) activates the Scene Launch buttons to launch scenes.

{{ image_sets(path="content/tap/manual/mixer.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Mixer View", caption='The Mixer View.') }}

### 3.6 Encoders View
Shows custom encoder layouts. 
- You can create a custom encoder layout, or load a previously created layout by tapping the button in the top right-hand corner and choosing your adventure. 
- Encoder layouts can include multiple pages. 
- You can adjust the name, MIDI channel, and CC for each encoder. 
- The navigation of the pages is done through the [Footer Bar](#3-2-2-footer-bar) arrows.  
- For encoder functionality, check the [Encoders Section](#3-3-3-encoders-section).

## 4. Tips and Tricks

### 4.1 Performance Features
These settings turn Tap into a powerhose, but this might be overwhelming. To change this, practise or disable them:
1. Go to **Settings**.
2. Scroll down to **Performance Features**, then tap on the button "Deactivate all".

This will deactivate all the performance features:
1. **Header View Switching** → while playing Tap, you can now switch views by tapping the already active channel. This frees the navigation buttons for other uses.
2. **Undo & Redo instead of Navigation** and **Octave Up & Down in Device View** → With these enabled, you'll have octave up/down buttons in the Device View, while long-pressing still triggers undo/redo. In other views, the buttons continue to perform undo/redo as usual.  
If you're on iPad in landscape mode, you'll always see the octave buttons in the Device View, regardless of these settings, as there's more space available for buttons.
3. **Sequencer Page Changing in Footer Bar Only** -> This makes it so you can page through the Sequencer pages with arrow buttons, you can swipe over the Octave buttons to get to the page buttons in vertical mode. In horizontal mode you will always see the page move buttons. This makes it faster to select MIDI notes (and turn pages) as there is no more swipe action for page changing in the grid.
4. **Play Button Menu** -> Turns the play button into a menu in the Sequencer (instead of a context menu).


### 4.2 Velocity
When using the MIDI pads or the step sequencer, you can tap the **Side Panel** button in the [Footer Bar](#3-2-2-footer-bar) and navigate to the **Velocity** section. From there, you can directly adjust the velocity of notes you play on the pads or add in the step sequencer.

<div class="footnote-definition"><p>Ableton Live is a trademark of Ableton AG, registered in the United States and other countries.
<br>iPhone and iPad are trademarks of Apple Inc., registered in the United States and other countries.</p></div>
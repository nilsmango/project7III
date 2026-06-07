+++
title = "Tap User Manual"
description = "The user manual for 7III Tap, an Ableton Live controller for iPhone & iPad"
[extra]
date = 2024-03-15
updated = 2026-05-30
share = true
featured_image = "mixer.jpg"
featured_image_alt = "Mixing an Ableton Live set with 7III Tap on iPad"
+++

<a href="/tap" class="btn" id="greenButton">← 7III Tap</a> <a href="/tap/videos" class="btn" id="greenButton">Videos</a> <a href="/tap/support" class="btn" id="greenButton">Support</a> <a href="/tap/history" class="btn" id="greenButton">Version History</a> <a href="/tap/best-ableton-live-controller" class="btn" id="greenButton">Controllers for Ableton Live</a>

This is the user manual for 7III Tap, an [Ableton Live controller for iPad & iPhone](/tap), with customizable MIDI CC encoders.  

>Last Update: **{{ date_updated() }}**  
>If you find any mistakes or notice anything missing in this user manual, please reach out and let us know!


<!-- toc -->

## 1. Quick Start
Below is a video to help you get started. It follows the Mac version of this manual, but most steps are similar on other systems. You can begin by following along with the [Set Up](#2-set-up) section. After the **Set Up** steps the video shows an older version of Tap without the new **Performance Features**. For the current navigation, refer to the [Performance Features](#4-1-performance-features) section, which includes a short updated video. 

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
<li>Your directory should now look like this:</li>
</ol>

```
Ableton/
└── User Library/
    └── Remote Scripts/
        └── Tap/
            ├── __init__.py
            ├── Tap.py
            └── README.md (optional, can be removed)
```

>**Important:** Make sure the User Library is stored locally on your computer and matches the exact path described above. If it is cloud-based or even slightly misnamed, Ableton Live may fail to recognize the script.

### 2.2 Connect your iPhone or iPad
Note: If you have a Mac, **MIDI over USB is the best way to connect your iPhone or iPad to Live**. If you are never using MIDI over WiFi, you can disable `MIDI over WiFi enabled in Settings.

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
<li>Connect your device to the same WiFi as your computer (preferably on an ad hoc WiFi network).</li>
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
- You will also find a button to enable/disable all [Performance Features](#4-1-performance-features).
- **Default MIDI Layout** sets which note layout Tap should use when you arrive in the MIDI pads of a MIDI track. You can choose the compact pad layouts, the larger pad layout, or the keyboard layout. On iPad the default "pad" choice is the 8 Pads layout; on iPhone it is the 4ths layout.

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
  - fold or unfold a Group Track, if the track is a group or belongs to one
  - toggle arm of the track (if audio track)
  - re-enable automation, either for the whole Live Set or for the next touched parameter
  - remove automation from the next touched parameter
  - activate "select a drum pad without playing it" (only with active drum pad layout)
  - configure the standard note length (only with active step sequencer)
  - go [Home](#3-1-home-view)
  - go to [Encoders](#3-6-encoders-view)

Group tracks show a group indicator in the Tracks Bar. When a group is folded in Live, Tap hides the tracks inside that group as well, so the Tracks Bar behaves like Live's Session View: fold the group to make room, unfold it when you want access to the child tracks again.

{{ image_sets(path="content/tap/manual/Tap_tracks_context_menu.jpg", format="auto", op="fit_width", quality=75, alt="Tracks Bar Context Menu", caption='The Tracks Bar context menu.' imgset_class="imgset-twothird") }}

#### 3.2.2 Footer Bar
Here's a detailed look at the buttons in the Footer Bar in vertical mode:

{{ image_sets(path="content/tap/manual/Footer_Bar.jpg", format="auto", op="fit_width", quality=75, alt="Tap Footer Bar", caption='The Footer Bar buttons in the step sequencers.') }}

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
If you deactivate the [Performance Features](#4-1-performance-features) in Settings you can navigate the three main views via the arrow buttons. In the [Encoders View](#3-6-encoders-view), this will move forward and backward through the encoder pages if you have more than one page.  

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
In the step sequencer with [Performance Features](#4-1-performance-features): Single Tap opens that menu. Long-press opens the [Tempo Overlay](#tempo-overlay).  
In all other layouts and views: Starts or stops the playback. Long-press opens the tempo overlay.  
In the [Step Sequencer](#3-3-5-step-sequencer) without **Performance Features**: Long-press shows a context menu for stopping, starting, adding, going to different clips, and the **Tempo Overlay**.  

Extra buttons in the horizontal Footer Bar of the Device View:  

8. Switch from Pads to Sequencer and vice versa.

9. Go to start of loop (only in Sequencer), stop all clips (in Pads)
  
##### Tempo Overlay
{{ image_sets(path="content/tap/manual/Tempo_Overlay.jpg", format="auto", op="fit_width", quality=75, alt="Tap Tempo Overlay", caption='The Tempo Overlay' imgset_class="imgset-half") }}

Tapping the plus and minus buttons will adjust the tempo by the amount indicated in the center.  
Tapping on the BPM digits lets you type in the exact tempo you want.
The Tempo Overlay also has a **Tap Tempo** pad and a **Metronome** button. Tap Tempo sends Live's tap-tempo command, so several taps set the song tempo from your rhythm. The Metronome button mirrors Live's metronome state and toggles it on or off.


### 3.3 Device View
#### 3.3.1 Devices Bar
The devices are shown here.
- You can navigate by swiping left or right. 
- Select a device by tapping on it. The selected device has a bold font. 
- Tap the `⊕` symbol to open the [Browser](#browser) or add a new random device. You can choose between adding a random sound, synth, drums (if you are in a MIDI track), or effect.
- `<` (open) and `>` (closed) symbols indicate rack mothers. You can open and close racks by tapping on a selected rack mother. Chain start and ends are indicated by corner brackets. The chain number is indicated with circles below the first member of the chain (for more than one chain per rack mother).

{{ image_sets(path="content/tap/manual/Devices Bar.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Devices Bar", caption='The Devices Bar.') }}

##### Browser
Browse away!
- Select a category by tapping on it. 
- Some instruments, drums, effects have children, indicated by a `>` symbol, to show the children tap the `>`. 
- To load a device or effect simply tap on it. 
- You can navigate through the browser levels by tapping on the level in the path display on top. 
- To go back and forth through the browser pages, tap the left or right arrow or swipe left or right. 
- Tap the `x` symbol to close the browser. 

#### 3.3.2 Banks Bar
Navigate and select banks of the chosen device here.

{{ image_sets(path="content/tap/manual/Encoders Section.jpeg", format="auto", op="fit_width", quality=75, alt="7III Tap Encoders Section", caption='The Banks Bar with the Encoders Section below.') }}

#### 3.3.3 Encoders Section
The 8 encoders of the current bank.  
- There are three types: dials, selectors (current selection with a slider underneath), on/off buttons
- All encoders show their approximate display value from Ableton Live (still work-in-progress, let us know if you find a big gap between what you see and what Ableton Live shows)
- All encoders with active automation have a small circle in the top left corner, in the color of the track. If the circle is gray, it means the automation is not active.

Dials:
- Activate a dial by touching it, then:
  - Move up or down for normal, broad value changes.
  - Move left or right for fine value changes.
  - Tap watches the beginning of your gesture and locks to the first clear direction it understands. After the dial has locked to vertical or horizontal movement, diagonal wobble is ignored, which makes live parameter moves much less jumpy.
- Double-tap a dial to reset to the default value; triple-tap to reset to center (63).

Selectors:
- Activate a selector by touching it, then:
- Adjust the value of a selector by:
  - moving your finger horizontal or vertical. The first direction will let you move from value to value
  - tapping it once, this will go through the values one by one
  - Double-tap a selector to reset it to the default value. No triple-tap.

On/Off Buttons:
- Simply tap a button to switch the value.

{{ image_sets(path="content/tap/manual/encoder.jpg", format="auto", op="fit_width", quality=75, alt="Tap Encoder", caption='An Encoder with active automation' imgset_class="imgset-quarter") }}

##### Parameter Automation from the Encoders
The small automation dot on an encoder tells you what Live reports for that parameter:
- A track-coloured dot means the parameter has active automation.
- A grey dot means automation exists, but it is currently overridden because the parameter was moved away from the automated value.

Automation actions appear in the Banks Bar menu and in the track context menu when they are useful:
- **Global Automation** re-enables automation for the whole Live Set. This is the same kind of action as pressing Live's "Re-enable Automation" button.
- **Local Automation** arms Tap for one touch. After choosing it, touch the encoder whose automation you want to re-enable. This is useful when one grey-dot parameter should return to automation without restoring the whole song.
- **Remove Automation** also arms Tap for one touch. After choosing it, touch the encoder whose automation should be removed. Tap clears that parameter's automation envelope from the playing clip on the selected track and leaves the parameter at its current value.

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
- Without [Performance Features](#4-1-performance-features): Drag horizontally on the background to navigate through the pages of the Step Sequencer. With **Performance Features** you only change pages with the Footer Bar arrows.
- Without **Performance Features**: Drag vertically first on the background to activate [Selection Mode](#3-3-5-1-selection-mode). With **Performance Features** enabled you can simply drag on the background to activate Selection Mode.
- Long press on a note to also enter Selection Mode (or if already in Selection Mode, this will add/remove the note from the selection).
- Change the drums page or octave using the Side Panel, or the up/down buttons in the Footer Bar - available in landscape mode or when **Performance Features** are enabled (see [Footer Bar](#3-2-2-footer-bar) button 2).
- To select a drum pad, long press on an empty step in the Step Sequencer.
- Pinch in the sequencer to change the grid size. Pinch open for a finer grid, down to 1/32. Pinch closed for a wider overview, up to whole-note pages. The same gesture works while editing automation.
- You can page further than the current clip length. This lets you move into empty space beyond the clip end, add notes or edit longer automation, and then extend the musical idea instead of being trapped at the old end marker.

Let's dive into the Tap Step Sequencer in detail:
{{ image_sets(path="content/tap/manual/Step_Sequencer.jpg", format="auto", op="fit_width", quality=75, alt="Tap Step Sequencer", caption='The Step Sequencer.') }}

1. The Start and Stop are marked with dark triangles.
2. The looped section is indicated by the band on top of the step sequencer and two lines at the start and end of the loop all in the color of the track.
3. Octave starts are marked with a horizontal line in the background. For drums, it is the selected drum pad that is marked.
4. Notes are shown as rectangles in the track’s colour. Each note also has a slightly darker background rectangle behind it for visual contrast.  
Velocity is represented by how much of the note is filled from the bottom up: a fully filled bar corresponds to velocity 127, while a barely filled bar represents velocity 1.  
Probability is represented by colour saturation: the more saturated the note’s colour, the higher the chance it will be played. Fully saturated means 100% probability.
5. Each note has an end rectangle. Drag the small rectangle at the end of a note horizontally to adjust its length, or vertically to adjust its velocity. This gesture can be a bit tricky, which is why we added an [Edit Overlay](#edit-overlay). When you [select](#3-3-5-1-selection-mode) one or more notes, the Edit Overlay becomes available. There, you can edit length, velocity, probability, and more.
6. The third track-colored line indicates the playing position.
7. These numbers show current page followed by total number of pages for this clip.
8. Shows clip playback status: solid play symbol `▶` means this clip is playing. An outline `▷` means a different clip on the same track is playing. A play symbol with a dash means no clip on this track is playing.
9. The Lil Green Helper rectangle. You can move the green rectangle by dragging it. Tap on it to open the menu. In the menu, you can move the loop and perform other useful actions like changing the drums page or octave. You can also change octaves/pages by using the side panel.  

When you tap the Lil Green Helper rectangle, you will see the following menu:

{{ image_sets(path="content/tap/manual/Step Seq Context Menu.jpg", format="auto", op="fit_width", quality=75, alt="Tap Lil Green Helper menu", caption='The Lil Green Helper menu.', imgset_class="imgset-half") }}

1. Move helper to End/Start: Use these if you don't want to drag the Lil Green Helper manually. Moves the green rectangle to the start or end of the sequencer window.
2. Page to Clip Start/End: Moves the sequencer page to the start/end of the clip.
3. Page to Loop Start/End: Moves the sequencer page to the start/end of the loop.
4. Crop Clip: Crops the clip to the loop length.
5. Move Loop Start/End & Loop: Moves the start/end of the loop and the whole loop (this means no change in loop length) to where the Lil Green Helper rectangle sits.
6. Move Loop Start/End: Only moves the start/end of the loop to where the Lil Green Helper rectangle sits. This will change the length of the loop.
7. Start/End Marker: Moves the start/end marker to the Lil Green Helper rectangle.

The Lil Green Helper menu also gives access to [Automation Editing](#3-3-5-2-automation-editing), the [Companion](#3-3-5-3-companion), and the [Rhythm Generator](#3-3-5-4-rhythm-generator), depending on the selected clip and track.

##### 3.3.5.1 Selection Mode
Enter Selection Mode by either selecting notes or long-pressing on a note. Selected notes and range are highlighted in light-blue.
Selections work the same way as in Ableton Live. You can add or subtract from a selection by dragging the selection square accordingly. You can also long-press on a selected note to deselect it. You can also add and subtract from the range of the selection, without selecting additional notes. This is important for duplication and copy-pasting.  
You can move around selected notes by dragging one of them. You can also adjust the velocity and the length of all the selected notes by simply editing one of them. As this can be finicky, especially when playing live, we have added an **Edit Overlay** for easy and quick editing (see below).
Info: You can't undo and redo selections.

{{ image_sets(path="content/tap/manual/Footer_Bar_Selection_mode.jpg", format="auto", op="fit_width", quality=75, alt="Tap Footer Bar in Selection Mode", caption='The Footer Bar buttons in Selection Mode.') }}

Once in Selection Mode, there are several new [Footer Bar](#3-2-2-footer-bar) buttons available, here are the new ones:
<ol>
  <li value="1">Trash: Deletes the selected notes.</li>
  <li value="4"><a href="#edit-overlay">Edit Overlay</a>: Opens and closes the edit overlay.</li>
  <li value="6"><a href="#modulation-menu">Modulation Menu</a>: Opens and closes the modulation menu.</li>
  <li value="7"><a href="#selection-menu">Selection Menu</a>: Opens and closes the selection menu.</li>
</ol>
  

###### Edit Overlay 
{{ image_sets(path="content/tap/manual/Edit_Overlay.jpg", format="auto", op="fit_width", quality=75, alt="Tap MIDI Notes Edit Overlay", caption='The notes Edit Overlay.' imgset_class="imgset-twothird") }}
1. Velocities of the selected notes. Drag to increase and decrease. Takes effect on letting go.
2. Probabilities of the selected notes. Drag to increase and decrease. Takes effect on letting go.
3. Copy button. Copies the selected range and notes into the copy buffer. To paste either press the Paste button (pastes buffer at start of selected range) or tap any grid cell. You can also paste in other clips etc. Once copy is active button 5 turns into a deactive **Selection Mode** button. When you press it, you will be able to use the **Play Menu** in the [Footer Bar](#3-2-2-footer-bar) to move to other clips in the track and paste the notes there!
4. Lengthen/shorten button. Lengthens or shortens the selected notes by one grid cell. On long-press, prolongs or shortens by one beat. On swipe you can change to `x2` and `/2` buttons. These multiply or divide the duration of the selected notes by 2.
5. Cut button. Cuts the selected range and notes into the copy buffer and deactivates **Selection Mode**. To paste, see "3. Copy button".
6. Duplicate button. Duplicates the selected range and notes to the end of the selected range.
7. Page indicator. Tap it or swipe on it to change the elongate/shorten buttons to `x2` and `/2` buttons.
8. Move buttons. Left and right moves the selected range and notes by one grid. Long-press moves the selection by one eighth of the grid. Keep pressing to repeat. Up and down moves the selected range and notes by one scale step. Long-press moves the selected notes by one octave.
  

###### Modulation Menu
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
  
###### Selection Menu
The notes Selection Menu is simple but powerful in combination with the Modulation Menu.  
You can: 
- select all notes
- invert the selection
- randomize the selection

##### 3.3.5.2 Automation Editing
Tap can edit the selected device parameter's clip automation directly in the Step Sequencer. Tap the Lil Green Helper and choose **Show Automation**. Tap will pick an automated parameter if it can find one; otherwise it uses the first available parameter in the current bank. To edit a different parameter, press **Choose Parameter** in the Footer Bar, then touch the encoder you want to edit.

The automation line is drawn over the sequencer:
- A solid line with dots means the clip has automation for the selected parameter.
- A dashed horizontal line means there is no envelope yet; the line shows the current parameter value.
- The selected parameter is marked with corner brackets around its encoder.

Editing works directly on the line:
- Tap the dashed line, a line segment, or the visible automation curve to add a point.
- Drag a point to move it in time and value. Time snaps to the current sequencer grid.
- Drag a line segment to bend the curve between two points.
- Tap a point when no automation points are selected to remove it.
- Drag on the background to select automation points. Selected points get a light-blue ring.
- Drag one selected point to move all selected automation points together.
- Tap the background to clear the selection.
- Turn on the pencil in the Footer Bar to draw automation continuously.

When automation points are selected, the Footer Bar changes:
- **Trash** deletes the selected automation points.
- **Duplicate** copies the selected automation span to the end of that span. The destination range is overwritten, and the first copied point lands exactly where the original selection ended, so repeating ramps and shapes continue cleanly.

The helper menu has a few important automation commands:
- **Automation End** sets a separate end point for the selected parameter's automation. This creates decoupled automation: the notes can loop at one length while the automation runs at another length.
- **Clear Automation** removes the selected parameter's automation envelope from the clip.
- **Clear All Automation** removes automation for the parameters in the current device bank.
- **Unfold Clip** commits a decoupled automation clip into a normal longer clip. The hidden repeated note copies become real clip content, and Tap removes the special folding metadata.

Decoupled automation is useful for slow filter movements, long macro sweeps, and polymetric automation. For example, you can keep a 1-bar drum loop while a filter automation takes 8 bars to return home. Tap shows the note loop and the automation loop separately; an `A` in the loop length indicator means you are looking at an automation length.

##### 3.3.5.3 Companion
The **Companion** turns the visible source loop into a longer musical structure. Tap calls this "mutator" in some older code, but in the app and the manual it is the Companion.

Open the Lil Green Helper menu and choose **Companion**. Tap uses the current loop as the source section, called `A`, then writes generated sections after it. The source loop stays the musical identity. Other sections are variations, bridges, hooks, fills, breaks, or returns based on the selected pattern and algorithm.

Companion clips are still editable. While a clip is in Companion mode, the generated structure is stored with the clip. You can:
- **Start** to create the Companion structure.
- **Apply** after changing settings that are waiting to be written.
- **Regenerate** to make a fresh version with the same settings.
- **Commit** to turn the generated structure into a normal MIDI clip.
- **Exit** to remove the generated sections and return to the original source loop.

The main controls are:
- **Melody / Rhythm** switches whether the Companion mutates melodic material or drum/rhythm material. In Rhythm mode, choose the target drum lanes or note rows first.
- **Pattern** chooses the song shape, such as `AABA`, `AABB`, `ABCD`, or longer forms.
- **Depth / Variation** sets how far Tap is allowed to move away from the source.
- **Regeneration** controls whether the Companion stays static or evolves while the clip plays: Static, every pass, every 2nd pass, every 4th pass, or probability-based 10%, 25%, 50%, or 75% evolution.
- The toggles decide which musical operations are allowed: fills, simplification, rhythmic shifts, additions, removals, velocity, gate, octave shifts, and pitch shifts.

Pattern roles:
- `A` is the original source loop. It is either unchanged or only very lightly touched.
- `A'` and `A''` are close variations. They keep the identity but add small note, timing, velocity, or repetition changes.
- `A'''` is a stronger variation with bigger rhythm and register movement.
- `AB` is a transition section, often end-weighted with pickups, fills, or a short break.
- `B` is contrast. It may be sparser, denser, inverted, displaced, or register-shifted.
- `B'` is a variation of `B`.
- `C` is the hook or refrain. It tries to feel more stable and memorable.
- `D`, `E`, and `F` are chained mutations, each generated from the previous letter rather than always from `A`.
- `C2` is a special second mutation of `C`.
- `Fill` leads clearly into the next section.
- `Break` reduces density and energy.
- `Drop` brings the energy back with stronger timing and velocity.

Pattern presets:
- `AB` gives one original pass and one contrast pass.
- `AABA` makes a compact question-and-return phrase.
- `AABB` repeats both the original and the contrast.
- `AAAA BBBB` creates a clear block of source material followed by a clear block of contrast.
- `AAAA AB AB BB` is the default. It develops the idea without an abrupt jump.
- `ABCD`, `AABCDE`, `AAAABCDE`, and `AABBCCDD` are chained mutations.
- `A B A B C B` alternates source and contrast before a hook-like section.
- `A A' A'' B C A` develops the source, visits a bridge and hook, then returns home.
- `A B C D C C2 B A` travels away from the source and then walks back.
- `A A A' A' B Fill A' A` builds tension and snaps back.
- `A A A' A' B Fill C C A' A` gives a verse, bridge, refrain, and return shape.
- `A A' A'' Fill B B' Break C Drop A` is a longer tension and release form.
- `A A A A' A' B Fill C C B Fill C C A' A` is built for longer live-performance phrases.

Melody algorithms:
- **Companion** is the general-purpose mutator. It starts from the source notes and applies the enabled operations according to the pattern role.
- **Verse Weaver** expands a motif gently, repeating nearby scale movements so the result feels like a verse variation rather than a new part.
- **Motif Ladder** moves the motif up and down the scale in a ladder shape. It is good for arpeggios, hooks, and patterns that should climb without losing their original rhythm.
- **Sparse Echo** keeps more space, removes some density, and adds short echo-like replies. It is useful when the source is too busy or when you want a delayed answer to the phrase.
- **Chorus Lift** raises the energy with upward scale movement, velocity lift, and occasional octave reinforcement. It aims for the "same idea, bigger" feeling.
- **Middle Eight** creates contrast with more timing displacement and longer note lengths. It is useful for a section that should feel like it left the main loop for a moment.
- **Tension Break** pushes notes upward, shortens or tightens timing, and adds energy before a return.
- **Skylight Hook** creates a bright, stepwise melodic hook with a slight upward bias.
- **Glass Steps** is crisp and sequenced, with more repeated upward step movement and a little extra velocity.
- **Nocturne Line** keeps the line lower and more restrained, with smaller downward movements.
- **Modal Drift** turns source notes into scale-aware chord movement. A single-note source can become triads that drift through the selected scale.
- **Circle Resolve** is another chord generator, but with a stronger feeling of movement and return. It may add an extra chord tone for more colour in stronger sections.

Rhythm algorithms:
- **Backbeat Engine** builds a solid kick/snare/hat pattern from the selected target lanes.
- **Broken Garage** makes a syncopated, off-grid-feeling drum pattern with garage-style kick placement.
- **Four Floor Bloom** makes a four-on-the-floor base with backbeat snare and offbeat hats; if you select an open-hat lane, it can use that for the offbeats.

##### 3.3.5.4 Rhythm Generator
The **Rhythm Generator** writes a rhythm into one note lane. In a drum track, it targets the selected drum pad. In a melodic MIDI track, it targets the selected note row; while the overlay is open, tap a row in the sequencer to choose a different target.

Open it from the Lil Green Helper menu. The overlay shows the target lane at the top. With **Auto** off, adjust the controls and press **Generate**. With **Auto** on, Tap updates the lane automatically as you change settings.

The controls:
- **Step Size** chooses whether the pattern is built from 1/4, 1/8, 1/16, or 1/32 steps.
- **Steps** chooses the number of slots in the pattern, up to 16.
- **Density** chooses how many of those slots contain notes.
- **Pattern** chooses one exact rhythm from all possible rhythms for the current Steps and Density. You can use the plus/minus buttons, long-press to move faster, or tap the number field and type the pattern number directly.
- **Shift** rotates the rhythm forward or backward.
- **Velocity** sets the base velocity.
- **Accent** sets how much louder accented notes are.
- **Accent Count** chooses how many hits are accented.
- **Accent Pattern** chooses which of the hits receive the accent.

Tap calculates the full set of possible hit patterns for the current Steps and Density. For example, 16 steps with 4 hits produces many possible placements. Tap sorts them musically by favouring even spacing, avoiding long runs of consecutive hits, and preferring patterns that begin on the downbeat. Accent patterns are calculated separately from the hit pattern, so you can keep the same rhythm and move only the accents.

Generating replaces the notes on the target lane inside the current loop. Other note lanes are left alone.

### 3.4 Clips View
{{ image_sets(path="content/tap/manual/clips.jpg", format="auto", op="fit_width", quality=75, alt="7III Tap Clips View", caption='The Clips View.') }}

Shows the clips. 
- Use the [Tracks Bar](#3-2-1-tracks-bar) to navigate horizontally; drag in the Clips View for navigating vertically.  
- Start and stop clips by tapping on a clip. If you tap on an empty clip slot in a MIDI Track, Tap will take you to the [Device View](#3-3-device-view). If you tap an empty clip in an armed audio track (arm by long-press in the Tracks Bar, then tap "Toggle Arm"), the recording will start. Tap it again to stop the recording.
- Long-press on any clip slot to bring up a context menu (see below).  
- Pressing the Side Panel button in the [Footer Bar](#3-2-2-footer-bar) activates the Scene Launch buttons to launch scenes.  
- The selected device's Banks Bar and Encoders Section are displayed above the clip view, exactly like in the Device View.

#### 3.4.1 Clip Slot Context Menu
{{ image_sets(path="content/tap/manual/Clip_Slot_Menu.jpg", format="auto", op="fit_width", quality=75, alt="Tap Clip Slot menu", caption='The Clip Slot Menu.' imgset_class="imgset-half") }}

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
- Double-tap the volume fader to set the volume to -inf dB. Use sends, panning, mute, and solo at your discretion.  
- 0 dB is indicated by the horizontal line, any volume that crosses 0 dB will turn the volume meter red.
  - Peak values (2-second hold) are indicated by little horizontal lines in the meter.
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
These settings turn Tap into a powerhouse. If this feels overwhelming, you can practise more… or just turn them off:  
Go to **Settings** → **Performance Features** → **Deactivate all**.

This will deactivate all the performance features:
1. **Header View Switching** → while playing Tap, you can now switch views by tapping the already active channel. This frees the navigation buttons for other uses.
2. **Undo & Redo instead of Navigation** and **Octave Up & Down in Device View** → With these enabled, you'll have octave up/down buttons in the Device View, while long-pressing still triggers undo/redo. In other views, the buttons continue to perform undo/redo as usual.  
If you're on iPad in landscape mode, you'll always see the octave buttons in the Device View, regardless of these settings, as there's more space available for buttons.
3. **Sequencer Page Changing in Footer Bar Only** -> This allows you to page through the Sequencer pages with arrow buttons. You can swipe over the Octave buttons to access the page buttons in vertical mode. In horizontal mode you will always see the page move buttons. This makes it faster to select MIDI notes (and turn pages) as there is no more swipe action for page changing in the grid.
4. **Play Button Menu** -> Turns the play button into a menu in the Sequencer (instead of a context menu).

Here's a basic instruction video to get you started with the **Performance Features** in Tap:
{{ youtube(id="Yfxzsf9OlC4", start="0") }}

### 4.2 Velocity
When using the MIDI pads or the step sequencer, you can tap the **Side Panel** button in the [Footer Bar](#3-2-2-footer-bar) and navigate to the **Velocity** section. From there, you can directly adjust the velocity of notes you play on the pads or add in the step sequencer.

<div class="footnote-definition"><p>Ableton Live is a trademark of Ableton AG, registered in the United States and other countries.
<br>iPhone and iPad are trademarks of Apple Inc., registered in the United States and other countries.</p></div>

# Beta_to_Greek
This GUI lets you get Greek characters by giving it ASCII characters in a scheme called Beta Code.

# Background
Not everyone likes the Windows Greek keyboard for writing extensive ammounts of Greek text.  And
internet isn't always a guarantee.  Thus, I decided to create this compiler so that students and
academics alike could write in Greek text for assigments, articles, commentaries, etc.

# Current Status
This is the final Python version of this project; I plan to phase it out with a Tauri (TypeScript + Rust)
version by next year.  WxPython cannot bind keystrokes as easily as Tkinter, so keyboard shortcuts are not
enabled.  But unlike Tkinter, WxPython does allow screen narrators to read the text inside buttons, which is
why WxPython was chosen over the standard library.  The GUI is currently available in English and Spanish.
God willing, we should get more language support later on.

# Credits
Jesus Castelan

# Lisence
This is available under the GNU license 3.0 

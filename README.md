# python_speech_assistant
A personal speech assistant that uses Python and Google's text-to-speech API.

Idea is from Brad Traversy's [YouTube tutorial]. Uploading my own copy, as it proved to be a great exercise in TTS recognition, virtual environments, and troubleshooting-related patience.

My version seems to work when it wants to at the moment; however, if interested, please visit Brad Traversy's [GitHub page] where he has uploaded (and updated) a nicer speech assistant.


### Dependencies
```
pip install speechrecognition
pip install gTTS
pip install pyaudio
pip install playsound
pip install PyObjC
```
```
pip install PyAudio
```
### Current Voice Commands
- What is your name? / Who are you?
- Search
- Exit

### Apple Mac OS X (Homebrew & PyAudio)
Use Homebrew to install the prerequisite portaudio library, then install PyAudio using pip:

`brew install portaudio`
`pip install pyaudio`

Notes:

If not already installed, download Homebrew.
pip will download the PyAudio source and build it for your version of Python.
Homebrew and building PyAudio also require installing the Command Line Tools for Xcode (more information).

https://people.csail.mit.edu/hubert/pyaudio/



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
  
   [youtube tutorial]: <https://www.youtube.com/watch?v=x8xjj6cR9Nc>
   [github page]: <https://github.com/bradtraversy/alexis_speech_assistant>





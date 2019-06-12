# I rule my data. I, my self and only I.

## Tools to generate web ready versions of media files

*Tool 1* checks naming of files according to a convention, and generates a JSON
with info about all files in dir.   
*Tool 2* renders media files for web usage to a `dist/` dir.

The tools do not depend on each other, you can check names, and you can render files. The files don't have to be named
after the spec.

### Specification

#### File naming schema
A simple schema defined for use in an actual archive project:
```
Scheme:  YYYY-MM-DD_HH-MM-SS_title.extension
Example: 2019-05-27_20-44-16_Sonnenuntergang in Petershausen.jpg

Time is optional...
Scheme:  YYYY-MM-DD_title.extension
Example: 2019-05-27_Sonnenuntergang in Petershausen.jpg
``` 

#### Media file conversion
- all files will be wiped of some uncomfortable meta information...
- creative commons meta tags will be written (you have to adapt that to your needs!)

##### jpg
- a lo res image for preload
- a lot of different sizes for use in responsive lazyloading (400w, 600w, 800w, 1000w, 1500w, 2000w, 2500w)  
  Notice: Even if the resolution of the source image is small, all sizes will be generated. No magic here...  
  ToDo: WebP

##### mp3
If we don't have a hi res audio file to use or want to preserve ID3 Tags or images inside,
but want to share it anyways.
- a copy via ffmpeg (nevertheless some data is cleaned...)

##### wav
- a best quality VBR mp3
- a best quality VBR vorbis ogg
- a flac

##### mp4
All files preserve resolution, but are transcoded for playback in a browser.
- a lo res preload image
- a webm
- an ogg
- an mp4

##### txt
- a JSON containing a HTML version, that preserves larger whitespaces (by some &amp;nbsp;)  

### Installation
Be sure to have the latest versions installed:
- FFmpeg (libmp3lame, libvorbis)
- ImageMagick (convert)
- GNU Make
- Python 3 (using 3.7.3 at the time of writing)

`media/` is the input dir for the hi resolution files  
`dist/` is the output dir for renders

###
```
# Be sure to have set up Python 3 (pyenv is great!) or type `$ python3` 
$ python --version
Python 3.7.3

# Setup virtual environment
$ python -m venv venv
$ source venv/bin/activate
# When the prompt starts with (venv) you're good to move on

# Install required python packages
pip install -r requirements.txt
```

#### Usage Tool 1 (Test file names against naming scheme)
`cd src && python main.py`  
Yes, that's it. It will check all file names in `media/` and writes a nice JSON that
contains all data to render a frontend. I use vue.js, but that's my personal choice. 

#### Usage Tool 2 (Render files)

##### Render all files
```
cd media

# make can't handle whitespaces
make nospaces

make

# sanitize files for web usage
make yesspaces
make chmod
```
 
##### Render specific file types
You can render `jpg`, `mp4`, `mp3`, `wav`, `txt` and `pdf`
```
make nospaces
make jpg
make yesspaces
```

##### Start fresh to render
If a given source file is rendered, a *.done file will be generated.
This way you can see inside of media, what is done and what needs to be done.
For example a render failed somehow - just delete that specific *.done file
and restart make.  
```
make clean
```

##### Wipe
If you want to delete all files in `dist/` (Attention, video and audio render
could take hours to days!) you have to type
```
make wipe
```
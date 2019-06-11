# I rule my data. I, my self and only I.

## Tools to generate web ready versions of media files

### Specification
- all files will be wiped of some uncomfortable meta information...
- creative commons meta tags will be written (you have to adapt that to your needs!)

#### jpg
- a lo res image for preload
- a lot of different sizes for use in responsive lazyloading (400w, 600w, 800w, 1000w, 1500w, 2000w, 2500w)  
  Notice: Even if the resolution of the source image is small, all sizes will be generated. No magic here...  
  ToDo: WebP

#### mp3
Thats here, if we don't have a hi res audio file but want to share it anyways.
- a copy (via ffmpeg) to preserve ID3 Tags (nevertheless some data is cleaned...)

#### wav
- a best quality VBR mp3
- a best quality ogg
- a reasonably good compressed flac

#### mp4
All files preserve resolution, but are transcoded for playing in a browser.
- a lo res preload image
- a webm
- an ogg
- an mp4

#### txt
- a JSON containing a HTML version, that preserves larger whitespaces (with &nbsp;)  

### Installation
Be sure to have the latest versions installed:
- FFmpeg (libmp3lame, libvorbis)
- ImageMagick (convert)
- GNU Make
- Python 3 (using 3.7.3 at the time of writing)

### Usage
`media/` is the input dir for the hi resolution files  
`dist/` is the output dir for renders

#### Render all files
```
cd media
make nospaces # make can't handle whitespaces
make
make yesspaces
make chmod # sanitize files for web usage
```
 
#### Render specific file types
You can render `jpg`, `mp4`, `mp3`, `txt` and `wav`
```
make nospaces
make jpg
make yesspaces
```

#### Start fresh to render
If a given source file is rendered, a *.done file will be generated.
This way you can see inside of media, what is done and what needs to be done.
For example a render failed somehow - just delete that specific *.done file
and restart make.  
```
make clean
```

#### Wipe
If you want to delete all files in `dist/` (Attention, video and audio render
could take hours to days!) you have to type
```
make wipe
```
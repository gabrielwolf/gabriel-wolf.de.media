DEST = ../dist
VENV_DIR = ../venv/bin/activate
CONVERT_TXT_TO_HTML_TO_JSON = ../src/convert_txt_to_html_to_json.py

%.done : %.jpg
	convert -strip -geometry 400x -blur 0x20 -interlace JPEG -sampling-factor 4:2:0 -quality 5 $< $(DEST)/$(subst .jpg,,$<)-preload.jpg
	convert -strip -geometry 400x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 95 $< $(DEST)/$(subst .jpg,,$<)-400w.jpg
	convert -strip -geometry 600x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-600w.jpg
	convert -strip -geometry 800x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-800w.jpg
	convert -strip -geometry 1000x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-1000w.jpg
	convert -strip -geometry 1500x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-1500w.jpg
	convert -strip -geometry 2000x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-2000w.jpg
	convert -strip -geometry 2500x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-2500w.jpg
	find $(DEST) -name "$(subst .jpg,,$<)*.jpg" -not -name "*©*" -exec exiftool -P -overwrite_original_in_place -OwnerName='Gabriel Wolf' -IFD0:Artist='Gabriel Wolf' -IPTC:By-line='Gabriel Wolf' -XMP-dc:Creator='Gabriel Wolf' -IPTC:By-lineTitle='Photographer' -IPTC:Contact='email: info@gabriel-wolf.de; website: https://gabriel-wolf.de' -XMP-iptcCore:CreatorWorkURL='https://gabriel-wolf.de' -d %Y -IFD0:Copyright='Creative Commons CC-BY 4.0' -d %Y -IPTC:CopyrightNotice='https://creativecommons.org/licenses/by/4.0/deed.de' -d %Y -XMP-dc:Rights='Creative Commons CC-BY 4.0' {} \;
	touch $@

%.done : %.mp3
	ffmpeg -i $< -metadata originator= -metadata encoded_by= -metadata encoder_settings= -c:v copy -c:a copy $(DEST)/$<
	touch $@

%.done : %.wav
	ffmpeg -i $< -metadata originator= -metadata encoded_by= -metadata encoder_settings= -codec:a libmp3lame -qscale:a 2 $(DEST)/$(subst .wav,.mp3,$<)
	ffmpeg -i $< -metadata originator= -metadata encoded_by= -metadata encoder_settings= -codec:a libvorbis -q:a 9 $(DEST)/$(subst .wav,.ogg,$<)
	ffmpeg -i $< -metadata originator= -metadata encoded_by= -metadata encoder_settings= -compression_level 8 $(DEST)/$(subst .wav,.flac,$<)
	touch $@

%.done : %.mp4
	# Preload Image
	ffmpeg -y -i $< -ss 00:00:05.000 -vframes 1 $(DEST)/$(subst .mp4,,$<).jpg
	convert -strip -geometry 800x -blur 0x20 -quality 5 $(DEST)/$(subst .mp4,,$<).jpg $(DEST)/$(subst .mp4,,$<)-preload.jpg
	rm -f $(DEST)/$(subst .mp4,,$<).jpg
	# Make actual video conversion
	ffmpeg -y -i $< -vcodec libvpx -b:v 5120k -c:a libvorbis -ac 2 -b:a 192k -ar 44100 $(DEST)/$(subst .mp4,.webm,$<)
	ffmpeg -y -i $< -c:v libtheora -c:a libvorbis -b:v 5120k -b:a 192k -ar 44100 $(DEST)/$(subst .mp4,.ogg,$<)
	ffmpeg -y -i $< -vcodec h264 -vb 5120k -acodec aac -ab 192k -pix_fmt yuv420p $(DEST)/$(subst .mp4,.mp4,$<)
	touch $@

%.done : %.txt
	( \
	source $(VENV_DIR); \
	$(CONVERT_TXT_TO_HTML_TO_JSON) $< $(DEST)/$(subst .txt,.json,$<); \
	)
	touch $@

%.done : %.pdf
	gs -r300x300 -sDEVICE=png16m -dFirstPage=1 -dLastPage=1 -o $(DEST)/$(subst .pdf,.png,$<) $<
	gm convert -geometry 300x +dither -depth 8 -colors 50 $(DEST)/$(subst .pdf,.png,$<) $(DEST)/$(subst .pdf,.png,$<)
	cp -fv $< $(DEST)/$<
	find $(DEST) -name "$<" -not -name "*©*" -exec exiftool -P -overwrite_original_in_place -Producer= -OwnerName='Gabriel Wolf' -IFD0:Artist='Gabriel Wolf' -IPTC:By-line='Gabriel Wolf' -XMP-dc:Creator='Gabriel Wolf' -IPTC:By-lineTitle='Composer' -IPTC:Contact='email: info@gabriel-wolf.de; website: https://gabriel-wolf.de' -XMP-iptcCore:CreatorWorkURL='https://gabriel-wolf.de' -d %Y -IFD0:Copyright='Creative Commons CC-BY 4.0' -d %Y -IPTC:CopyrightNotice='https://creativecommons.org/licenses/by/4.0/deed.de' -d %Y -XMP-dc:Rights='Creative Commons CC-BY 4.0' {} \;
	touch $@

jpg = $(shell ls *.jpg)
jpgdone = $(subst .jpg,.done,$(jpg))

mp3 = $(shell ls *.mp3)
mp3done = $(subst .mp3,.done,$(mp3))

wav = $(shell ls *.wav)
wavdone = $(subst .wav,.done,$(wav))

mp4 = $(shell ls *.mp4)
mp4done = $(subst .mp4,.done,$(mp4))

txt = $(shell ls *.txt)
txtdone = $(subst .txt,.done,$(txt))

pdf = $(shell ls *.pdf)
pdfdone = $(subst .pdf,.done,$(pdf))

donefiles = $(jpgdone) $(mp3done) $(wavdone) $(mp4done) $(txtdone) $(pdfdone)

all: $(donefiles)

jpg: $(jpgdone)
mp3: $(mp3done)
wav: $(wavdone)
mp4: $(mp4done)
txt: $(txtdone)
pdf: $(pdfdone)

# Make cannot handle spaces in filenames, so temporarily rename them
.PHONY: nospaces
nospaces:
	rename -v 's/ /XX/g' *\ * &
	rename -v 's/ /XX/g' $(DEST)/*\ * &

# After Make is done, rename files back to having spaces
.PHONY: yesspaces
yesspaces:
	rename -v 's/XX/ /g' * &
	rename -v 's/XX/ /g' $(DEST)/* &

.PHONY: chmod
chmod:
	find $(DEST) -type f -exec chmod 0644 {} \;


.PHONY: wipe
wipe:
	rm -f $(DEST)/*

clean:
	rm -f *.done

DEST = ../dist

%.done : %.jpg
	convert -strip -geometry 400x -blur 0x20 -interlace JPEG -sampling-factor 4:2:0 -quality 1 $< $(DEST)/$(subst .jpg,,$<)-preload.jpg
	convert -strip -geometry 400x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 95 $< $(DEST)/$(subst .jpg,,$<)-400w.jpg
	convert -strip -geometry 600x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-600w.jpg
	convert -strip -geometry 800x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-800w.jpg
	convert -strip -geometry 1000x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-1000w.jpg
	convert -strip -geometry 1500x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-1500w.jpg
	convert -strip -geometry 2000x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-2000w.jpg
	convert -strip -geometry 2500x -sharpen 0x0.5 -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -quality 90 $< $(DEST)/$(subst .jpg,,$<)-2500w.jpg
	exiftool -P -overwrite_original_in_place -OwnerName='Gabriel Wolf' -IFD0:Artist='Gabriel Wolf' -IPTC:By-line='Gabriel Wolf' -XMP-dc:Creator='Gabriel Wolf' -IPTC:By-lineTitle='Photographer' -IPTC:Contact='email: info@gabriel-wolf.de; website: https://gabriel-wolf.de' -XMP-iptcCore:CreatorWorkURL='https://gabriel-wolf.de' -d %Y -IFD0:Copyright='Creative Commons CC-BY 4.0' -d %Y -IPTC:CopyrightNotice='https://creativecommons.org/licenses/by/4.0/deed.de' -d %Y -XMP-dc:Rights='Creative Commons CC-BY 4.0' $(DEST)/*.jpg
	touch $@

%.done : %.mp3
	cp -v $< $(DEST)/$<
	touch $@

jpg = $(shell ls *.jpg)
jpgdone = $(subst .jpg,.done,$(jpg))

mp3 = $(shell ls *.mp3)
mp3done = $(subst .mp3,.done,$(mp3))

donefiles = $(jpgdone) $(mp3done) $(wavdone)

all: $(donefiles)

jpg: $(jpgdone)
mp3: $(mp3done)

clean:
	rm -f *.done

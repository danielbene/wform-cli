# wform-cli
Python based cli application for generating simple waveform images from audio files. Generation time is about 6-7 seconds for a 30 minute audio (more than half of that is actually saving the image - this is caused by the high resolutions).

For detailed options and usage examples please see the included manual, that you can access with the `--help` cli option.

You can use the `Waveform` class as a python module if you want the functionality in your project.

---
## Examples
With default settings, transparent background, and optimized image width:
![transparent_wform](https://raw.githubusercontent.com/danielbene/project-media/master/wform-cli/wave.png)

Same audio with incresed width (more sampling -> more detail), and manually set colors:
![high_res_wform](https://raw.githubusercontent.com/danielbene/project-media/master/wform-cli/wave_high.png)

Lowered quality (faster generation, lower image size):
![low_res_colored_wform](https://raw.githubusercontent.com/danielbene/project-media/master/wform-cli/wave_low.png)

---
## Manual
```
Generating simple waveform image based on the given audio file.
project home: https://github.com/danielbene/wform-cli

usage examples:
    - wform-cli-win.exe c:\\path\\to\\audio.wav c:\\path\\to\\image.png
    - wform-cli-win.exe -bg '#FFFFFF' -c '#494949' c:\\audio.wav c:\\image.png
    - wform-cli-linux /home/user/Music/audio.wav /home/user/image.png
    - wform-cli-linux -manw 75000 /path/to/audio.wav image.png
    - wform-cli-linux -minw 20000 -maxw 200000 -c '#494949' /path/to/audio.wav image.png

limitations:
    - audio files fully loaded into memory during generation
    - basic wav files supported out of the box,
        but everything else (mp3, ogg, etc) needs ffmpeg on the system
        (eg.: signed-integer wav encoding is ok, but a-law is not)
    - only png output is supported now (but it allows transparency)
```

---
Parts of the Waveform class, and the idea is based on this script: https://gist.github.com/mixxorz/abb8a2f22adbdb6d387f

# wform-cli
Python based cli application for generating simple waveform images from audio files. Generation time is about 6-7 seconds for a 30 minute audio (more than half of that is actually saving the image - this is caused by the high resolutions). Binary builds are automatic (for Windows, and Linux) and the latest tag follows the state of the main branch.

For detailed options and usage examples please see the included manual, that you can access with the `--help` cli option.

You can simply use the `Waveform` class as a python module too if you want the functionality in your project.

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

Options:
    -bg, --background_color TEXT    Set the background color.
                                    Transparent by default. (eg.: '#FFFFFF')
    -c, --color TEXT                Set the spike color with hexadecimal value.
                                    [default: #65909A]
    -g, --gap INTEGER               Size of the gap between the image border
                                    and highest spikes. Value is in pixels.
                                    [default: 100]
    -h, --height INTEGER            Set the output image height in pixels.
                                    [default: 1000]
    -v, --version                   Print application version.
    -manw, --manual_width INTEGER   Skip optimal image width calculation and set
                                    the given value.
    -maxw, --maximum_width INTEGER  Image maximum width in pixels.  [default:
                                    150000]
    -minw, --minimum_width INTEGER  Image minimum width in pixels.  [default:
                                    10000]
    --help                          Show this message and exit.
```

---
Parts of the Waveform class, and the idea is based on this script: https://gist.github.com/mixxorz/abb8a2f22adbdb6d387f

import click

from waveform import Waveform


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 0.1')
    ctx.exit()


@click.command()
@click.option('-bg', '--background_color',
              help='Set the background color. \
                    Transparent by default. (eg.: \'#FFFFFF\')')
@click.option('-c', '--color', default='#65909A',
              show_default=True,
              help='Set the spike color with hexadecimal value.')
@click.option('-h', '--height', default=1000,
              show_default=True,
              help='Set the output image height in pixels.')
@click.option('-v', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True,
              help='Print application version.')
@click.option('-manw', '--manual_width', type=int,
              help='Skip optimal image width calculation and set \
                    the given value.')
@click.option('-maxw', '--maximum_width', default=150000,
              show_default=True,
              help='Image maximum width in pixels.')
@click.option('-minw', '--minimum_width', default=10000,
              show_default=True,
              help='Image minimum width in pixels.')
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path(exists=False))
def generate(background_color, color, height, manual_width, maximum_width,
             minimum_width, input_path, output_path):
    """
    \b
    Generating simple waveform image based on the given audio file.
    project home: https://github.com/danielbene/wform-cli

    \b
    usage examples:
        - wform-cli-win.exe c:\\path\\to\\audio.wav c:\\path\\to\\image.png
        - wform-cli-win.exe -bg '#FFFFFF' -c '#494949' c:\\audio.wav c:\\image.png
        - wform-cli-linux /home/user/Music/audio.wav /home/user/image.png
        - wform-cli-linux -manw 75000 /path/to/audio.wav image.png
        - wform-cli-linux -minw 20000 -maxw 200000 -c '#494949' /path/to/audio.wav image.png

    \b
    limitations:
        - audio files fully loaded into memory during generation
        - basic wav files supported out of the box,
            but everything else (mp3, ogg, etc) needs ffmpeg on the system
            (eg.: signed-integer wav encoding is ok, but a-law is not)
        - only png output is supported now (but it allows transparency)
    """
    waveform = Waveform(input_path, height, manual_width, maximum_width,
                        minimum_width)
    waveform.save(output_path, background_color, color)


if __name__ == '__main__':
    generate()

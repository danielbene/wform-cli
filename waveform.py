import sys

from pydub import AudioSegment
from PIL import Image, ImageColor


class Waveform(object):

    PEEK_DETAIL_POINT_SECS = 3600

    def __init__(self, filename, gap, img_height, img_manual_width,
                 img_max_width, img_min_width):
        try:
            audio_file = AudioSegment.from_file(filename,
                                                filename.split('.')[-1])
        except FileNotFoundError:
            # input file not found is handled by Click, so this is ok
            print('\n-----------------------------------------------------\n' +
                  'Error: this audio type requires ffmpeg for processing, ' +
                  'but couldn\'t find it. Please make sure it\'s installed ' +
                  'and/or reachable through system PATH. (Only basic wav ' +
                  'files (with popular encoding) can be processed without ' +
                  'external codec.)' +
                  '\n-----------------------------------------------------\n')
            sys.exit(1)

        self.img_height = img_height
        self.audio_length_ms = len(audio_file)
        self.img_width = self._calculate_width(img_manual_width, img_max_width,
                                               img_min_width)
        self.peaks = self._calculate_peaks(audio_file, gap)

    def generate_waveform_image(self, bg_color, color):
        dimensions = (self.img_width, self.img_height)
        if bg_color is not None:
            rgb = ImageColor.getcolor(bg_color, "RGB")
            im = Image.new('RGB', dimensions, rgb)
        else:
            im = Image.new('RGBA', dimensions, (255, 0, 0, 0))

        for index, value in enumerate(self.peaks, start=0):
            upper_endpoint = int(self.img_height / 2) - value

            im.paste(Image.new('RGBA', (4, value * 2), color),
                     (index, upper_endpoint))

        return im

    # NOTE: saving/writing out the image files takes more than
    # half of the total generation time
    def save(self, img_path, wform_image):
        with open(img_path, 'wb') as imfile:
            wform_image.save(imfile, 'PNG')

    # list of audio level peaks
    def _calculate_peaks(self, audio_file, gap):
        chunk_length = self.audio_length_ms / self.img_width

        loudness_of_chunks = [
            audio_file[i * chunk_length: (i + 1) * chunk_length].rms
            for i in range(self.img_width)]

        max_rms = max(loudness_of_chunks) * 1.00
        db_ceiling = (self.img_height - gap) / 2

        return [int((loudness / max_rms) * db_ceiling)
                for loudness in loudness_of_chunks]

    """
        This is experimental. Calculating optimal image width based on
        the max/min width, and a "peek detail point". If the audio
        length exceeds the peek point (1 hour at the moment), than the
        width is fixated at max (therefore longer audios produces less
        detailed maps, while still containing the whole length). If the
        length is less then that, than increment the width linearly from
        the minimum by a scale based on the length.
    """
    def _calculate_width(self, img_manual_width, img_max_width, img_min_width):
        if img_manual_width is not None:
            return img_manual_width

        media_length_in_sec = int(self.audio_length_ms / 1000)

        if img_min_width > img_max_width:
            img_max_width = img_min_width

        base = img_max_width - img_min_width
        scale = media_length_in_sec / self.PEEK_DETAIL_POINT_SECS

        if scale > 1:
            scale = 1

        return img_min_width + int(base * scale)

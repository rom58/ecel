import os
import subprocess

from engine.parser import Parser


class ManualScreenShotParser(Parser):
    type = "parsers.ManualScreenShot"

    def __init__(self, plugin):
        super(ManualScreenShotParser, self).__init__(plugin)
        if os.name == 'nt':
            self.script_file = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "manualscreen_parser.bat")
        else:
            self.script_file = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "manualscreen_parser.sh")
        self.click_dir = os.path.join(self.file_or_dir, "")

    def parse(self):
        subprocess.Popen([self.script_file, self.click_dir, self.parsed_folder],shell=False)
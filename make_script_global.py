#!/usr/bin/env python3

import os
import sys
import subprocess


class ScriptManger():
    def __init__(self, file_name):
        self.golbal_dir = '/usr/local/bin'
        self.file_name = file_name

    def make_script_executable(self):
        os.chmod(self.file_name, 0o755)

    def make_script_normal(self):
        os.chmod(self.file_name, 0o664)

    def start(self):
        self.path = os.path.join(self.golbal_dir, self.file_name)

        if os.path.exists(self.path):
            option = input(
                "File Already exists did you wont to overwrite: 'y' or 'n' ")

            if option.lower() == "y":
                self.copy_script_to_global()

            else:
                sys.exit(1)
        else:
            self.copy_script_to_global()

    def copy_script_to_global(self):
        try:
            self.make_script_executable()
            subprocess.run(['sudo', 'cp', self.file_name, self.path])
            self.make_script_normal()
            print('File copy successful')

        except subprocess.CalledProcessError as e:
            print(f'Something went wrong {e}')


def main():
    if len(sys.argv) < 2:
        print('Need file name')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('File does not exist')
        sys.exit(1)

    file_path = os.path.basename(sys.argv[1])

    scriptManger = ScriptManger(file_path)
    scriptManger.start()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3


import os
from sys import argv, exit


class FlutterScreen():

    def __init__(self, folder_name: str, router_name: str):
        self.folder_name = folder_name
        self.router_name = router_name
        self.screen_structure = {
            "data": [
                {
                    "folder": "models",
                    "file_name": f"{self.folder_name}_model.dart",
                    "content": "",
                },
                {
                    "folder": "providers",
                    "file_name": f"{self.folder_name}_provider.dart",
                    "content": "",
                },
            ],
            "widgets": [],
            "views": [
                {
                    "file_name": f"{self.folder_name}_screen.dart",
                    "content": self.create_screen_file(self.folder_name, self.router_name)
                },
            ],
        }

    def create_screen(self):
        try:
            path = os.path.join(self.folder_name)

            os.mkdir(path)

            for sub_folder in self.screen_structure:
                sub_folder_current_path = os.path.join(path, sub_folder)

                os.mkdir(sub_folder_current_path)

                for item in self.screen_structure[sub_folder]:
                    sub__folder_current_path = sub_folder_current_path

                    if item.get('folder') is not None:
                        sub__folder_current_path = os.path.join(
                            sub__folder_current_path, item.get('folder'))
                        os.mkdir(sub__folder_current_path)

                    if item.get('file_name') is not None and item.get('file_name'):
                        with open(os.path.join(sub__folder_current_path, item.get('file_name')), 'w') as file:
                            file.write(item.get('content'))

        except OSError:
            print('file already exists')

    def create_screen_file(self, folder_name: str, router_name: str) -> str:
        return f"""
    import 'package:flutter/material.dart';

    class {folder_name.capitalize()}Screen extends StatelessWidget {{
    const {folder_name.capitalize()}Screen({{super.key}});

    static const String routerName = '/{router_name}';
    
    @override
    Widget build(BuildContext context) {{
        return const Scaffold(
        body: Text(
            '{folder_name.capitalize()} Screen',
            textAlign: TextAlign.center,
        ),
        );
    }}
    }}

    """


def main():

    if len(argv) < 2:
        print('Need Screen Name and Router Name ')
        exit(1)

    folder_name = argv[1]

    if len(argv) > 1:
        router_name = folder_name.lower()

    flutterScreen = FlutterScreen(folder_name, router_name)
    flutterScreen.create_screen()


if __name__ == '__main__':
    main()

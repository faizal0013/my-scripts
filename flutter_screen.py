#!/usr/bin/env python3


import os


def create_screen_file(folder_name: str, router_name: str) -> str:
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


folder_name = input("Enter a Screen Name: ")

router_name = input("Enter a Router Name: ")

if folder_name == "" or router_name == "":
    exit(1)

screen_structure = {
    "data": [
        {
            "folder": "models",
            "file_name": f"{folder_name}_model.dart",
            "content": "",
        },
        {
            "folder": "providers",
            "file_name": f"{folder_name}_provider.dart",
            "content": "",
        },
    ],
    "widgets": [],
    "views": [
        {
            "file_name": f"{folder_name}_screen.dart",
            "content": f"{create_screen_file(folder_name, router_name)}"
        },
    ],
}


def main():
    try:
        path = os.path.join(folder_name)

        os.mkdir(path)

        for sub_folder in screen_structure:
            sub_folder_current_path = os.path.join(path, sub_folder)

            os.mkdir(sub_folder_current_path)

            for item in screen_structure[sub_folder]:

                sub__folder_current_path = sub_folder_current_path

                if item.get('folder') is not None :
                    sub__folder_current_path = os.path.join(sub__folder_current_path, item.get('folder'))
                    os.mkdir(sub__folder_current_path)

                if item.get('file_name') is not None and item.get('file_name'):
                    with open(os.path.join(sub__folder_current_path, item.get('file_name')), 'w') as file:
                        file.write(item.get('content'))

    except OSError:
        print('file already exists')

if __name__ == '__main__':
    main()

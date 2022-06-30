# SPDX-FileCopyrightText: 2022 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

while read filename; do
    if [ "$1" == "install" ]; then
        echo "Copying $filename to {{ cookiecutter.script_name }}/"
        ln  ./submodules/adabot/tools/$filename ./{{ cookiecutter.script_name }}/$filename;
    elif [ "$1" == "clean" ]; then
        echo "Deleting $filename in {{ cookiecutter.script_name }}/"
        rm ./{{ cookiecutter.script_name }}/$filename;
    fi
done < tools_reqs.txt

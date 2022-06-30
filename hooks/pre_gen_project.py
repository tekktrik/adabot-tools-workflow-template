# SPDX-FileCopyrightText: 2022 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

is_adafruit = "{{ cookiecutter.is_adafruit }}"
valid_options = ("y", "yes", "n", "no")

if is_adafruit not in valid_options:
    print(f"{is_adafruit} is not a valuid option, must be one of {valid_options}")
    raise SystemExit(1)

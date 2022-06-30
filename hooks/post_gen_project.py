# SPDX-FileCopyrightText: 2022 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import subprocess

subprocess.Popen(["git", "init"]).communicate()
subprocess.Popen(["git", "submodule", "add", "https://github.com/adafruit/adabot.git", "submodules/adabot"]).communicate()
subprocess.Popen(["git", "submodule", "update", "--init", "submodules/adabot"]).communicate()

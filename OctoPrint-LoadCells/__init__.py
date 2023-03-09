# -*- coding: utf-8 -*-

from octoprint.util.comm import parse_firmware_line
import logging

import re
import octoprint.plugin
import flask
import base64

import numpy as np
from time import sleep
from time import time

class LoadCellsPlugin(octoprint.plugin.StartupPlugin,
                      octoprint.plugin.TemplatePlugin,
                      octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.BlueprintPlugin):
    """ OctoPrint LoadCells Plugin for monitoring loadcell values and automatically saving them locally """

    def __init__(self):
        self.bed_d = (355, 355)
        self.lc1_pos = (177.5, 118.33)
        self.lc2_pos = (236.67, 236.67)
        self.lc3_pos = (236.67, 118.33)

        pass

    def on_after_startup(self):
        self._logger.info("LoadCells \n(more: %s)" % self._settings.get(["url"]))
        self._logger.info("\n\n\nsaving gcode...\n\n\n")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/flask_test.js"],
            css=["css/gridcam.css"]
        )


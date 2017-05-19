#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import npyscreen

from vent.helpers.meta import Version
from vent.helpers.paths import PathDirs
from vent.menus.add import AddForm
from vent.menus.add_options import AddOptionsForm
from vent.menus.build_core_tools import BuildCoreToolsForm
from vent.menus.build_tools import BuildToolsForm
from vent.menus.core_inventory import CoreInventoryForm
from vent.menus.choose_tools import ChooseToolsForm
from vent.menus.clean_core_tools import CleanCoreToolsForm
from vent.menus.clean_tools import CleanToolsForm
from vent.menus.help import HelpForm
from vent.menus.inventory import InventoryForm
from vent.menus.main import MainForm
from vent.menus.services import ServicesForm
from vent.menus.start_core_tools import StartCoreToolsForm
from vent.menus.start_tools import StartToolsForm
from vent.menus.stop_core_tools import StopCoreToolsForm
from vent.menus.stop_tools import StopToolsForm

class VentApp(npyscreen.NPSAppManaged):
    """ Main menu app for vent CLI """
    keypress_timeout_default = 10
    repo_value = {}

    def onStart(self):
        """ Override onStart method for npyscreen """
        paths = PathDirs()
        paths.host_config()
        version = Version()
        self.addForm("MAIN", MainForm, name="Vent "+version+"\t\t\t\t\tPress ^T to toggle help\t\t\t\t\t\tPress ^Q to quit", color="IMPORTANT")
        self.addForm("HELP", HelpForm, name="Help\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="DANGER")
        self.addForm("COREINVENTORY", CoreInventoryForm, name="Inventory of core tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="STANDOUT")
        self.addForm("INVENTORY", InventoryForm, name="Inventory of plugins\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="STANDOUT")
        self.addForm("ADD", AddForm, name="Add\t\t\t\t\t\t\t\tPress ^T to toggle help (To Be Implemented...)\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("ADDOPTIONS", AddOptionsForm, name="Set options for new plugin\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("CHOOSETOOLS", ChooseToolsForm, name="Choose tools to add for new plugin\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("SERVICES", ServicesForm, name="Services\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="STANDOUT")
        self.addForm("BUILDTOOLS", BuildToolsForm, name="Build tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("STARTTOOLS", StartToolsForm, name="Start tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("STOPTOOLS", StopToolsForm, name="Stop tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("CLEANTOOLS", CleanToolsForm, name="Clean tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("BUILDCORETOOLS", BuildCoreToolsForm, name="Build core tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("STARTCORETOOLS", StartCoreToolsForm, name="Start core tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("STOPCORETOOLS", StopCoreToolsForm, name="Stop core tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")
        self.addForm("CLEANCORETOOLS", CleanCoreToolsForm, name="Clean core tools\t\t\t\t\t\t\t\tPress ^T to toggle main\t\t\t\t\t\tPress ^Q to quit", color="CONTROL")

    def change_form(self, name):
        """ Changes the form (window) that is displayed """
        self.switchForm(name)
        self.resetHistory()

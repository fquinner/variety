# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (c) 2012, Peter Levi <peterlevi@peterlevi.com>
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE
import abc

from jumble.IPlugin import IPlugin
from variety.plugins.downloaders.ImageSource import ImageSource
from variety.plugins.downloaders.DefaultDownloader import DefaultDownloader


class SimpleDownloader(ImageSource, DefaultDownloader, metaclass=abc.ABCMeta):
    def __init__(self):
        ImageSource.__init__(self)
        DefaultDownloader.__init__(
            self,
            source=self,
            description=self.get_description(),
            folder_name=self.get_folder_name())
        IPlugin.activate(self)
        self.queue = []

    @abc.abstractmethod
    def get_description(self):
        pass

    def get_folder_name(self):
        return self.get_source_name()

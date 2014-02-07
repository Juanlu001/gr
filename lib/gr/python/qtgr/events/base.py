# -*- coding: utf-8 -*-
"""..."""
# standard library
import logging
# third party
from PyQt4 import QtCore
# local library
import gr
import qtgr
from gr.pygr import CoordConverter

__author__ = "Christian Felder <c.felder@fz-juelich.de>"
__date__ = "2014-02-07"
__version__ = "0.3.0"
__copyright__ = """Copyright 2012-2014 Forschungszentrum Juelich GmbH

This file is part of GR, a universal framework for visualization applications.
Visit https://iffwww.iff.kfa-juelich.de/portal/doku.php?id=gr for the latest
version.

GR was developed by the Scientific IT-Systems group at the Peter Grünberg
Institute at Forschunsgzentrum Jülich. The main development has been done
by Josef Heinen who currently maintains the software.

GR is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This framework is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with GR. If not, see <http://www.gnu.org/licenses/>.
 
"""

_log = logging.getLogger(__name__)

class EventMeta(QtCore.QEvent):

    def __init__(self, type):
        super(EventMeta, self).__init__(type)
        self._type = type

    def type(self):
        return self._type

class MouseLocationEventMeta(EventMeta):

    def __init__(self, type, width, height, x, y, window=None):
        super(MouseLocationEventMeta, self).__init__(type)
        self._coords = CoordConverter(width, height, window=window)
        self._coords.setDC(x, y)

    def getWindow(self):
        return self._coords.getWindow()

    def getWC(self, viewport):
        return self._coords.getWC(viewport)

    def getNDC(self):
        return self._coords.getNDC()

    def getDC(self):
        return self._coords.getDC()

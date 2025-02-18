#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure('-DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -L', sourceDir = '..')

def build():
    pythonmodules.compile(pyVer = '3')
    shelltools.cd("build")
    cmaketools.make()

def install():
    pythonmodules.install(pyVer = '3')
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())


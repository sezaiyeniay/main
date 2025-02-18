#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DDHT_BOOTSTRAP=OFF',
    ' -DENABLE_STATIC=OFF '
    ])

def setup():
	pisitools.dosed("CMakeLists.txt", "RPATH", deleteLine = True)
	cmaketools.configure("-B_build %s -L" % j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	pisitools.insinto("/etc", "other/bootstrap_daemon/tox-bootstrapd.conf")
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

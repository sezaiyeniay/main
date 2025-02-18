#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --with-opengl',
    ' --enable-jp2',
    ' --enable-debug',
    ' --disable-native',
    ' --disable-static '
    ])

def setup():
	pisitools.dosed("lib/FXRex.cpp", "#define\ TOPIC_REXDUMP", "// #define TOPIC_REXDUMP")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "LICENSE_ADDENDUM", "README")

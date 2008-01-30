# vim:noexpandtab:autoindent:tabstop=8:shiftwidth=8:filetype=make:nocindent:tw=0:

include Makefile-std

pkgconfdir = $(sysconfdir)/firmware/firmware.d/
dist_pkgconf_DATA = pkg/dell-repo-tools.conf

EXTRA_DIST += COPYING-GPL COPYING-OSL

dist_bin_SCRIPTS = \
	bin/build_deb  bin/dup_pkginfo.py  bin/make_dell_mirror  bin/mkbiosrepo.sh

pkgdatadir = $(datadir)/firmware-tools/
dist_pkgdata_DATA = libexec/extract.dat

REPLACE_VARS_ON_INSTALL=

# vim:noexpandtab:autoindent:tabstop=8:shiftwidth=8:filetype=make:nocindent:tw=0:

include Makefile-std

pkgconfdir = $(sysconfdir)/firmware/firmware.d/
dist_pkgconf_DATA = pkg/dell-repo-tools.conf

EXTRA_DIST += COPYING-GPL COPYING-OSL

dist_bin_SCRIPTS = \
	bin/build_deb  bin/make_dell_mirror  bin/mkbiosrepo.sh   bin/findunsigned.py   bin/rpmwrap.sh

pkgdatadir = $(datadir)/firmware-tools/
dist_pkgdata_DATA = libexec/extract.dat

#!/usr/bin/python2
# vim:expandtab:autoindent:tabstop=4:shiftwidth=4:filetype=python:

# import arranged alphabetically
import getopt
import os
import rpmUtils
import shutil
import sys
import traceback
import types
import rpmUtils
import rpmUtils.transaction

sys.path.insert(0, "/usr/libexec/dell-repo-tools/")
sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), "lib"))
sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), "libexec"))

from decorator import decorator
import mebtrace

# levels:
#   0: Nothing
#   1: Basic
#   3: Detailed
#   9: ENTER/LEAVE

mebtrace.debug = {
    '__main__': 0,
    }

def main():
    directory = None
    verbose=0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:v", ["directory=", "verbose",])
        for option, argument in opts:
            if option in ("-d", "--directory"):
                directory = argument
            if option in ("-v", "--verbose"):
                mebtrace.debug["__main__"] = mebtrace.debug["__main__"] + 1
                verbose=1

        if directory is None: raise getopt.GetoptError("no input dir", "no input dir")

        for (dirpath, dirnames, filenames) in os.walk(directory):
            for file in filenames:
                file = os.path.realpath(os.path.join(dirpath, file))
                ts = rpmUtils.transaction.initReadOnlyTransaction()
                try:
                    hdr = rpmUtils.miscutils.hdrFromPackage(ts, file)
                    sig = rpmUtils.miscutils.getSigInfo(hdr)
                    mebtrace.dprint("got hdr: %s\n" % repr(hdr), msgLevel=3)
                    mebtrace.dprint("%s\n" % str(rpmUtils.miscutils.getSigInfo(hdr)), msgLevel=1)
                    if sig[0] and not verbose:
                        # no ouput, just report if outputRepo not set
                        print "%s" % file
                except rpmUtils.RpmUtilsError, e:
                    mebtrace.dprint("could not open rpm: %s\n" % file, msgLevel=3)

    except (Exception), e:
        print str(e)
        sys.exit(2)

    except (getopt.GetoptError):
        print __doc__
        sys.exit(1)

    except:
        traceback.print_exc()
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()

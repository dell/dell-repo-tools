#!/usr/bin/python2
# vim:expandtab:autoindent:tabstop=4:shiftwidth=4:filetype=python:

import inspect
import sys
import traceback
from decorator import decorator

# levels:
#   0: Nothing
#   1: Basic
#   3: Detailed
#   9: ENTER/LEAVE

def dprint(message, msgLevel=1, outLevel=None):
    if outLevel is None:
        e = traceback.extract_stack(limit=2)
        function = str(e[0][2])
        # get function object pointer for whatever called us
        f = inspect.currentframe().f_back.f_globals[function]
        global debug
        outLevel=debug.get("__main__", 0)
        outLevel=debug.get(function, outLevel)
        outLevel=debug.get(f.func_dict.get("module", function), outLevel)

    if outLevel >= msgLevel:
        sys.stdout.write(message)

@decorator
def trace(f, *args, **kw):
    # search path for outLevel
    #   - debug[module]
    #   - debug[f.func_name]
    #   - debug['__main__']
    #   - 0
    global debug
    outLevel=debug.get("__main__", 0)
    outLevel=debug.get(f.func_name, outLevel)
    outLevel=debug.get(f.func_dict.get("module", f.func_name), outLevel)

    msgLevel=9
    dprint("ENTER: %s(%s, %s)\n" % (f.func_name, args, kw), msgLevel=msgLevel, outLevel=outLevel)
    result = f(*args, **kw)
    dprint( "LEAVE %s --> %s\n\n" % (f.func_name, result), msgLevel=msgLevel, outLevel=outLevel)
    return result

def setModule(module):
    def newFunc(func):
        func.func_dict['module'] = module
        return func
    return newFunc


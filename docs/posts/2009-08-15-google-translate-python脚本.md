---
title: "Google translate python脚本"
date: 2009-08-15
author: pengjianqing
categories: ['Tech']
---

学习python,写了一个简单的脚本，利用google翻译API，简单的实现从英文翻译到中文
之前还了一个[Android版的翻译前端](http://www.impjq.net/blog/2009/06/04/androidgoogle-%e7%bf%bb%e8%af%91%e5%89%8d%e7%ab%af/)。

输入q退出。
```

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename:
# author:pengjianqinggmail.com

import urllib
import urllib2
import sys
import simplejson
from optparse import OptionParser

URL = "http://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q=%s&langpair=%s%%7C%s"

parser = OptionParser()
parser.add_option("-f", "--from", dest="lang1",
        help="The language code to translate from", default="en")
parser.add_option("-t", "--to", dest="lang2",
        help="The language code to translate to", default="zh")

(options, args) = parser.parse_args()

def tran(text='hello'):
    print text
    print "Translating '%s' from %s to %s" % (text, options.lang1, options.lang2)
    query = (URL % (urllib.quote(text), options.lang1, options.lang2))
    req = urllib2.Request(query)
    req.add_header("Referer", "http://blog.impjq.net")
    r = urllib2.urlopen(req)
    data = r.read()
    return data
    #print data

text = raw_input('Input(q:to exit):')

while text != 'q':
    data = tran(text)
    if simplejson.loads(data).__getitem__('responseStatus').__str__().__contains__('200'):
        print 'Translate success'
        responseData = simplejson.loads(data).__getitem__('responseData')
        print text+':'+responseData['translatedText']

    else:
        print 'Translate failed'

    text = raw_input('Input(q:to exit):')
else:
    print 'q to exit'

```

打印各个函数说明文档：
```

def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s-> %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])
    print "\n".join(['%s %s'%(method.ljust(spacing)," ".join((str(getattr(object, method).__doc__)).split())) for method in methodList])

info(sys,20)

```

输出结果：
```

__displayhook__     -> displayhook(object) -> None Print an object to sys.stdout and also save it in __builtin__.
__excepthook__      -> excepthook(exctype, value, traceback) -> None Handle an exception by displaying it with a traceback on sys.stderr.
_current_frames     -> _current_frames() -> dictionary Return a dictionary mapping each current thread T's thread id to T's current stack frame. This function should be used for specialized purposes only.
_getframe           -> _getframe([depth]) -> frameobject Return a frame object from the call stack. If optional integer depth is given, return the frame object that many calls below the top of the stack. If that is deeper than the call stack, ValueError is raised. The default for depth is zero, returning the frame at the top of the call stack. This function should be used for internal and specialized purposes only.
call_tracing        -> call_tracing(func, args) -> object Call func(*args), while tracing is enabled. The tracing state is saved, and restored afterwards. This is intended to be called from a debugger from a checkpoint, to recursively debug some other code.
callstats           -> callstats() -> tuple of integers Return a tuple of function call statistics, if CALL_PROFILE was defined when Python was built. Otherwise, return None. When enabled, this function returns detailed, implementation-specific details about the number of function calls executed. The return value is a 11-tuple where the entries in the tuple are counts of: 0. all function calls 1. calls to PyFunction_Type objects 2. PyFunction calls that do not create an argument tuple 3. PyFunction calls that do not create an argument tuple and bypass PyEval_EvalCodeEx() 4. PyMethod calls 5. PyMethod calls on bound methods 6. PyType calls 7. PyCFunction calls 8. generator calls 9. All other calls 10. Number of stack pops performed by call_function()
displayhook         -> displayhook(object) -> None Print an object to sys.stdout and also save it in __builtin__.
exc_clear           -> exc_clear() -> None Clear global information on the current exception. Subsequent calls to exc_info() will return (None,None,None) until another exception is raised in the current thread or the execution stack returns to a frame where another exception is being handled.
exc_info            -> exc_info() -> (type, value, traceback) Return information about the most recent exception caught by an except clause in the current stack frame or in an older stack frame.
exc_type            -> None
excepthook          -> excepthook(exctype, value, traceback) -> None Handle an exception by displaying it with a traceback on sys.stderr.
exit                -> exit([status]) Exit the interpreter by raising SystemExit(status). If the status is omitted or None, it defaults to zero (i.e., success). If the status is numeric, it will be used as the system exit status. If it is another kind of object, it will be printed and the system exit status will be one (i.e., failure).
getcheckinterval    -> getcheckinterval() -> current check interval; see setcheckinterval().
getdefaultencoding  -> getdefaultencoding() -> string Return the current default string encoding used by the Unicode implementation.
getdlopenflags      -> getdlopenflags() -> int Return the current value of the flags that are used for dlopen() calls. The flag constants are defined in the dl module.
getfilesystemencoding-> getfilesystemencoding() -> string Return the encoding used to convert Unicode filenames in operating system filenames.
getrecursionlimit   -> getrecursionlimit() Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.
getrefcount         -> getrefcount(object) -> integer Return the reference count of object. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount().
setcheckinterval    -> setcheckinterval(n) Tell the Python interpreter to check for asynchronous events every n instructions. This also affects how often thread switches occur.
setdlopenflags      -> setdlopenflags(n) -> None Set the flags that will be used for dlopen() calls. Among other things, this will enable a lazy resolving of symbols when importing a module, if called as sys.setdlopenflags(0) To share symbols across extension modules, call as sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
setprofile          -> setprofile(function) Set the profiling function. It will be called on each function call and return. See the profiler chapter in the library manual.
setrecursionlimit   -> setrecursionlimit(n) Set the maximum depth of the Python interpreter stack to n. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. The highest possible limit is platform- dependent.
settrace            -> settrace(function) Set the global debug tracing function. It will be called on each function call. See the debugger chapter in the library manual.
__displayhook__      displayhook(object) -> None Print an object to sys.stdout and also save it in __builtin__.
__excepthook__       excepthook(exctype, value, traceback) -> None Handle an exception by displaying it with a traceback on sys.stderr.
_current_frames      _current_frames() -> dictionary Return a dictionary mapping each current thread T's thread id to T's current stack frame. This function should be used for specialized purposes only.
_getframe            _getframe([depth]) -> frameobject Return a frame object from the call stack. If optional integer depth is given, return the frame object that many calls below the top of the stack. If that is deeper than the call stack, ValueError is raised. The default for depth is zero, returning the frame at the top of the call stack. This function should be used for internal and specialized purposes only.
call_tracing         call_tracing(func, args) -> object Call func(*args), while tracing is enabled. The tracing state is saved, and restored afterwards. This is intended to be called from a debugger from a checkpoint, to recursively debug some other code.
callstats            callstats() -> tuple of integers Return a tuple of function call statistics, if CALL_PROFILE was defined when Python was built. Otherwise, return None. When enabled, this function returns detailed, implementation-specific details about the number of function calls executed. The return value is a 11-tuple where the entries in the tuple are counts of: 0. all function calls 1. calls to PyFunction_Type objects 2. PyFunction calls that do not create an argument tuple 3. PyFunction calls that do not create an argument tuple and bypass PyEval_EvalCodeEx() 4. PyMethod calls 5. PyMethod calls on bound methods 6. PyType calls 7. PyCFunction calls 8. generator calls 9. All other calls 10. Number of stack pops performed by call_function()
displayhook          displayhook(object) -> None Print an object to sys.stdout and also save it in __builtin__.
exc_clear            exc_clear() -> None Clear global information on the current exception. Subsequent calls to exc_info() will return (None,None,None) until another exception is raised in the current thread or the execution stack returns to a frame where another exception is being handled.
exc_info             exc_info() -> (type, value, traceback) Return information about the most recent exception caught by an except clause in the current stack frame or in an older stack frame.
exc_type             None
excepthook           excepthook(exctype, value, traceback) -> None Handle an exception by displaying it with a traceback on sys.stderr.
exit                 exit([status]) Exit the interpreter by raising SystemExit(status). If the status is omitted or None, it defaults to zero (i.e., success). If the status is numeric, it will be used as the system exit status. If it is another kind of object, it will be printed and the system exit status will be one (i.e., failure).
getcheckinterval     getcheckinterval() -> current check interval; see setcheckinterval().
getdefaultencoding   getdefaultencoding() -> string Return the current default string encoding used by the Unicode implementation.
getdlopenflags       getdlopenflags() -> int Return the current value of the flags that are used for dlopen() calls. The flag constants are defined in the dl module.
getfilesystemencoding getfilesystemencoding() -> string Return the encoding used to convert Unicode filenames in operating system filenames.
getrecursionlimit    getrecursionlimit() Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.
getrefcount          getrefcount(object) -> integer Return the reference count of object. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount().
setcheckinterval     setcheckinterval(n) Tell the Python interpreter to check for asynchronous events every n instructions. This also affects how often thread switches occur.
setdlopenflags       setdlopenflags(n) -> None Set the flags that will be used for dlopen() calls. Among other things, this will enable a lazy resolving of symbols when importing a module, if called as sys.setdlopenflags(0) To share symbols across extension modules, call as sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
setprofile           setprofile(function) Set the profiling function. It will be called on each function call and return. See the profiler chapter in the library manual.
setrecursionlimit    setrecursionlimit(n) Set the maximum depth of the Python interpreter stack to n. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. The highest possible limit is platform- dependent.
settrace             settrace(function) Set the global debug tracing function. It will be called on each function call. See the debugger chapter in the library manual.

```

![](http://img.zemanta.com/pixy.gif?x-id=2afb60ac-3275-8bfe-a024-9aee5d10e4dd)
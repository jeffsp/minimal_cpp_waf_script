# Minimal waf script for C++ programs
#
# Contains support for multithreading and debug/release builds
#
# jeffsp@gmail.com
#
# Fri Mar 11 11:08:22 CST 2016

# waf project directories
top = '.'
out = 'build'

# Global definitions
SOURCES='*.cpp'
CXXFLAGS=['-fopenmp','-Wall','-Werror','-std=c++11','-Wl,--no-as-needed']
LIBS=['pthread', 'gomp']

# Variant specific build flags
DEBUG_CXXFLAGS=CXXFLAGS+['-g']
RELEASE_CXXFLAGS=CXXFLAGS+['-O3','-DNDEBUG']

import glob

def configure(ctx):

    ctx.setenv('debug')
    ctx.load('compiler_cxx')
    ctx.env.CXXFLAGS=DEBUG_CXXFLAGS
    ctx.env.SOURCES=glob.glob(SOURCES)


    ctx.setenv('release')
    ctx.load('compiler_cxx')
    ctx.env.CXXFLAGS=RELEASE_CXXFLAGS
    ctx.env.SOURCES=glob.glob(SOURCES)

def options(opt):

    opt.load('compiler_cxx')

def init(ctx):

    # Setup contexts build_debug, build_release, clean_debug, ...
    from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext
    for x in (BuildContext, CleanContext, InstallContext, UninstallContext):
        for y in ['debug','release']:
            class tmp(x):
                variant=y
                cmd=x.__name__.replace('Context','').lower()+'_'+y

def build(ctx):

    # If no variant was specified then build them all
    if not ctx.variant:
        import waflib.Options
        for x in ['debug', 'release']:
            waflib.Options.commands.insert(0, ctx.cmd+'_'+x)
    else:
        # The executable name is the filename without the extension
        for s in ctx.env.SOURCES:
            ctx.program(source=s,target=s.replace('.cpp',''),lib=LIBS)

# C++ waf wscript

Minimal waf script for C++ programs

Contains support for C++11, multi-threading, and debug/release builds

# Examples


Start clean

    [11:31AM] toro ● ~/Projects/wscript ▶ waf clean
    'clean' finished successfully (0.006s)
    'clean_release' finished successfully (0.003s)
    'clean_debug' finished successfully (0.003s)

Build debug and release versions

    [11:31AM] toro ● ~/Projects/wscript ▶ waf
    Waf: Entering directory `/home/jsp/Projects/wscript/build'
    Waf: Leaving directory `/home/jsp/Projects/wscript/build'
    'build' finished successfully (0.004s)
    Waf: Entering directory `/home/jsp/Projects/wscript/build/release'
    [1/2] Compiling program.cpp
    [2/2] Linking build/release/program
    Waf: Leaving directory `/home/jsp/Projects/wscript/build/release'
    'build_release' finished successfully (0.443s)
    Waf: Entering directory `/home/jsp/Projects/wscript/build/debug'
    [1/2] Compiling program.cpp
    [2/2] Linking build/debug/program
    Waf: Leaving directory `/home/jsp/Projects/wscript/build/debug'
    'build_debug' finished successfully (0.449s)

Run debug version

    [11:31AM] toro ● ~/Projects/wscript ▶ ./build/debug/program 100
    DEBUG is ON
    N=100
    -50 -49 -48 ...
    0.00175185s elapsed
    Success

Run release version

    [11:31AM] toro ● ~/Projects/wscript ▶ ./build/release/program 100
    N=100
    -50 -49 -48 ...
    0.00145048s elapsed
    Success

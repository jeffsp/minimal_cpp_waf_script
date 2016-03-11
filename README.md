# C++ waf wscript

Minimal waf script for C++ programs

Contains support for C++11, multi-threading, and debug/release builds

# Examples


Start clean

    [11:31AM] toro ● ~/Dropbox/Projects/wscript ▶ waf clean
    'clean' finished successfully (0.006s)
    'clean_release' finished successfully (0.003s)
    'clean_debug' finished successfully (0.003s)

Build debug and release versions

    [11:31AM] toro ● ~/Dropbox/Projects/wscript ▶ waf
    Waf: Entering directory `/home/jsp/Dropbox/Projects/wscript/build'
    Waf: Leaving directory `/home/jsp/Dropbox/Projects/wscript/build'
    'build' finished successfully (0.004s)
    Waf: Entering directory `/home/jsp/Dropbox/Projects/wscript/build/release'
    [1/2] Compiling program.cpp
    [2/2] Linking build/release/program
    Waf: Leaving directory `/home/jsp/Dropbox/Projects/wscript/build/release'
    'build_release' finished successfully (0.443s)
    Waf: Entering directory `/home/jsp/Dropbox/Projects/wscript/build/debug'
    [1/2] Compiling program.cpp
    [2/2] Linking build/debug/program
    Waf: Leaving directory `/home/jsp/Dropbox/Projects/wscript/build/debug'
    'build_debug' finished successfully (0.449s)

Run debug version

    [11:31AM] toro ● ~/Dropbox/Projects/wscript ▶ ./build/debug/program 100
    DEBUG is ON
    N=100
    -50 -49 -48 -47 -46 -45 -44 -43 -42 -41 -40 -39 -38 -37 -36 -35 -34 -33 -32 -31
    -30 -29 -28 -27 -26 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11
    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
    19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
    45 46 47 48 49
    0.00175185s elapsed
    Success

Run release version

    [11:31AM] toro ● ~/Dropbox/Projects/wscript ▶ ./build/release/program 100
    N=100
    -50 -49 -48 -47 -46 -45 -44 -43 -42 -41 -40 -39 -38 -37 -36 -35 -34 -33 -32 -31
    -30 -29 -28 -27 -26 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11
    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
    19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
    45 46 47 48 49
    0.00145048s elapsed
    Success

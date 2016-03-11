// program.cpp
//
// Dumb example program for minimal C++ waf wscript
//
// jeffsp@gmail.com
//
// Fri Mar 11 10:58:33 CST 2016

#include "timer.h"
#include <cassert>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

using namespace std;

const string usage = "usage: ./program2 N";

int main (int argc, char **argv)
{
    try
    {
        assert (clog << "DEBUG is ON" << endl);

        // Check args
        if (argc != 2)
            throw runtime_error (usage);

        // Allocate our vector
        const int N = atoi (argv[1]);

        clog << "N=" << N << endl;

        vector<int> v (N);
        timer t;
        iota (v.begin(), v.end(), -N / 2);
        for (auto i : v)
            clog << ' ' << i;
        clog << endl;

        clog << t() << "s elapsed" << endl;
        clog << "Success" << endl;

        return 0;
    }
    catch (const exception &e)
    {
        cerr << "exception: " << e.what () << endl;
    }
    return -1;
}

// timer.h
//
// Timer class
//
// jeffsp@gmail.com
//
// Fri Mar 11 11:02:04 CST 2016

#ifndef TIMER_H
#define TIMER_H

#include <chrono>

class timer
{
    public:
    timer ()
    {
        reset ();
    }
    void reset ()
    {
        start  = std::chrono::system_clock::now ();
    }
    double operator() () const
    {
        return elapsed_seconds ();
    }
    double elapsed_seconds () const
    {
        std::chrono::time_point<std::chrono::system_clock> end = std::chrono::system_clock::now ();
        std::chrono::duration<double> elapsed_seconds = end - start;
        return elapsed_seconds.count ();
    }
    private:
    std::chrono::time_point<std::chrono::system_clock> start;
};

#endif // TIMER_H

# Makefile for C++ minimal waf wscript
#
# jeffsp@gmail.com
#
# Fri Mar 11 10:57:20 CST 2016

BUILD=debug
#BUILD=release

.PHONY : \
default
default: waf

.PHONY : \
waf
waf:
	waf configure
	waf

.PHONY : \
check
check:
	./build/$(BUILD)/program 20

.PHONY : \
clean
clean:
	waf clean

#!/bin/sh

objdump -d /usr/lib/libc.so.6 | grep "syscall" | tail -1 | cut -d ":" -f1


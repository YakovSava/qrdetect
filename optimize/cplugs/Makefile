CCP=g++
CC=gcc
FSM=fasm
CFLAGS=-I

all: connector.so linfile.so

connector.so: connector.cpp
	b2 Jamfile

linfile.so: linsys.o linfile.c
	$(CC) $(CFLAGS) linfile.c

linsys.o: asm/linsys.asm
	$(FSM) asm/linsys.asm
	mv asm/linsys.asm .

clean
	rm -f *.o
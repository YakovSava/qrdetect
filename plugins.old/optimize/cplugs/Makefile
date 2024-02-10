CC = gcc
PY = python3
PYFLAGS = build_ext --inplace

all: linfile.so

linfile.so: linsys.o linfile.cpp connector.cpp
	$(PY) $(PYFLAGS)

linsys.o: asm/linsys.asm
	$(FSM) asm/linsys.asm
	mv asm/linsys.asm .

clean:
	rm -f *.o
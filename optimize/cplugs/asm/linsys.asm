format COFF

public Cread
public Cwrite
public exists

section ".bss" readable writeable
    db _buffer, 0

section ".code" executable
    Cread:
        xor eax, eax ; temporary stub
        ret
    Cwrite:
        xor eax, eax ; temporary stub
        ret
    exists:
        xor eax, eax ; temporary stub
        ret
    exit:
        xor eax, eax ; mov eax, 1
        inc eax
        xor ebx, ebx ; mov ebx, 0
        int 0x80
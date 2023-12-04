format COFF

public Cread
public Cwrite
public exists

section '.filedesc' executable
    

section '.Cread' executable
    Cread:
        ret

section '.Cwrite' executable
    Cwrite:
        ret

section '.exists' executable
    exists:
        ret

section '.exit' executable
    exit:
        xor rax, rax
        inc rax
        xor rbx, rbx
        int 0x80
format COFF

public Cread
public Cwrite

extrn Cread
extrn Cwrite

section '.filedesc' executable
    asmfcreate:
    ; Input:
    ;   rax - filename
    ;   rbx - permissions
    ; Output:
    ;   rax - descriptor
        mov rcx, rbx
        mov rbx, rax
        mov rax, 8 ; create file 
        int 0x80
        ret 
    asmfopen:
    ; Input:
    ;   rax - filename
    ;   rbx - mode
    ;       read - 0
    ;       write - 1
    ;       read & write - 2
    ; Output:
    ;   rax - descriptor
        mov rcx, rbx
        mov rbx, rax
        mov rax, 5 ; open
        int 0x80
        ret
    asmfclose:
    ; Input:
    ;   rax - descriptor
        mov rbx, rax
        mov rax, 6 ; close
        int 0x80
        ret
    asmfdelete:
    ; Input:
    ;   rax - descriptor
        mov rbx, rax
        mov rax, 10 ; unlink
        int 0x80
        ret
    asmfseek:
    ; Input:
    ;   rax - descriptor
    ;   rbx - mode
    ;       set - 0
    ;       cur - 1
    ;       end - 2
    ;   rcx - position
        mov rdx, rbx
        mov rbx, rax
        mov rax, 19 ; seek
        int 0x80
    asmfread:
    ; Input:
    ;   rax - descriptor
    ;   rbx - buffer
    ;   rcx - buffer size
        push rbx
        push rcx
    
        mov rbx, 1 
        xor rcx, rcx
        call asmfseek
    
        pop rcx
        pop rbx
    
        mov rdx, rcx
        mov rcx, rbx
        mov rbx, rax
        mov rax, 3 ; read
        int 0x80
    asmfwrite:
    ; Input:
    ;   rax - descriptor
    ;   rbx - data
    ;   rcx - data size
        push rbx
        push rcx
    
        mov rbx, 1 
        xor rcx, rcx
        call fseek
    .
        pop rcx
        pop rbx
    
        mov rdx, rcx
        mov rcx, rbx
        mov rbx, rax
        mov rax, 4 ; write
        int 0x80

section '.Cread' executable
    Cread:
        ret

section '.Cwrite' executable
    Cwrite:
        ret

section '.exit' executable
    exit:
        xor rax, rax
        inc rax
        xor rbx, rbx
        int 0x80
BITS 64
GLOBAL _start
SECTION .data
    filepath: db "/bin/sh"
SECTION .text
_start:
    mov rax, 59
    mov rdi, filepath
    mov rsi, 0
    mov rdx, 0
    syscall
    mov rax, 231
    mov rdi, 42
    syscall


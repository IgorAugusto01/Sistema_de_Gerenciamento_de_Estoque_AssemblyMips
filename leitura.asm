.data

arquivo:    .asciiz "produtos.txt"
linha:      .space  80


.text
.globl main

main:  

    li      $v0,    13
    la      $a0,    arquivo
    li      $a1,    0
    syscall
    move    $s0,    $v0

    li      $t2,    0

  
loop:
    li      $v0,    14
    move    $a0,    $s0
    la      $a1,    linha
    li      $a2,    80
    syscall
    move    $s1,    $v0


    beq     $s1,    $zero,      fechar_arquivo


    li      $v0,    4
    la      $a0,    linha
    syscall

    li      $t0,    0
    j       loop










fechar_arquivo:
    li      $v0,    16
    move    $a0,    $s0
    syscall



    li      $v0,    10
    syscall

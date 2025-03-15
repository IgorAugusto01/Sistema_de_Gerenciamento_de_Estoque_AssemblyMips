.data
arquivo_temporario: .asciiz "temporario.txt"
arquivo_produtos: .asciiz "produtos.txt"
linha: .space 1024
string_produto: .asciiz "Produto: "
cod_string: .asciiz ", cod: "
quebra_linha: .byte '\n'
cod: .word 0

.text
.globl main

main:
    jal contar_linhas
    jal ler_arquivo_temporario
    jal escrever_arquivo_produtos
    li $v0, 10
    syscall

ler_arquivo_temporario:
    addi $sp, $sp, -4
    sw $ra, 0($sp)

    li $v0, 13
    la $a0, arquivo_temporario
    li $a1, 0
    syscall
    move $s0, $v0

    li $v0, 14
    move $a0, $s0
    la $a1, linha
    li $a2, 1024
    syscall
    move $s1, $v0

    li $v0, 16
    move $a0, $s0
    syscall

    lw $ra, 0($sp)
    addi $sp, $sp, 4
    jr $ra

escrever_arquivo_produtos:
    addi $sp, $sp, -4
    sw $ra, 0($sp)

    li $v0, 13
    la $a0, arquivo_produtos
    li $a1, 9
    syscall
    move $s0, $v0

    li $v0, 15
    move $a0, $s0
    la $a1, string_produto
    li $a2, 9
    syscall

    li $v0, 15
    move $a0, $s0
    la $a1, linha
    move $a2, $s1
    syscall

    li $v0, 15
    move $a0, $s0
    la $a1, cod_string
    li $a2, 7
    syscall

    lw $t0, cod
    addi $t0, $t0, 48
    sb $t0, linha
    li $v0, 15
    move $a0, $s0
    la $a1, linha
    li $a2, 1
    syscall

    li $v0, 15
    move $a0, $s0
    la $a1, quebra_linha
    li $a2, 1
    syscall

    li $v0, 16
    move $a0, $s0
    syscall

    lw $ra, 0($sp)
    addi $sp, $sp, 4
    jr $ra

contar_linhas:
    addi $sp, $sp, -4
    sw $ra, 0($sp)

    li $v0, 13
    la $a0, arquivo_produtos
    li $a1, 0
    syscall
    move $s0, $v0

    li $t0, 0

ler_linha:
    li $v0, 14
    move $a0, $s0
    la $a1, linha
    li $a2, 1024
    syscall
    move $t1, $v0

    beqz $t1, fim_contar_linhas

    la $a1, linha
    li $t2, 0
loop_contar:
    lb $t3, 0($a1)
    beq $t3, 10, incrementar_linha
    beqz $t3, ler_linha
    addi $t2, $t2, 1
    addi $a1, $a1, 1
    j loop_contar

incrementar_linha:
    addi $t0, $t0, 1
    addi $a1, $a1, 1
    j loop_contar

fim_contar_linhas:
    li $v0, 16
    move $a0, $s0
    syscall

    addi $t0, $t0, 1
    sw $t0, cod

    lw $ra, 0($sp)
    addi $sp, $sp, 4
    jr $ra
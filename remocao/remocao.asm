.data
arquivo_produtos: .asciiz "produtos2.txt"  
arquivo_temporario: .asciiz "temporario2.txt"  
arquivo_auxiliar: .asciiz "auxiliar.txt"  
produto_remover: .space 1024  
linha_produtos: .space 1024  
string_produto: .asciiz "Produto: "
cod_string: .asciiz ", cod: "
quebra_linha: .byte '\n'
cod: .byte 0  

.text
.globl main

main:
  jal recolher_produto_remover 
   
   
    li $v0,13
    la $a0,arquivo_produtos
    li $a1,0
    syscall
    move $s0,$v0   
  
  
  jal procurar_produto
   



procurar_produto:

    li $t5,1
    
    li $v0,14
    move $a0,$s0
    la $a1,linha_produtos
    li $a2,1024
    syscall
    move $s1,$v0

    beq $s1,$zero,fim

    la $t0,linha_produtos
    la $t1,produto_remover

    addi $t0,$t0,9


ler_caracteres:
    lb $t2,0($t0)
    lb $t3,0($t1)

    bne $t2,$t3,escrever_auxiliar
    
    addi $t0,$t0,1
    addi $t1,$t1,1
    addi $t5,$t5,1

    beq $t5,$t4,possivel_produto_igual
    
    j ler_caracteres

    


escrever_auxiliar:
    
    li $v0,13
    la $a0,arquivo_auxiliar
    li $a1,9
    syscall
    move $s2,$v0




    li $v0,15
    move $a0,$s2
    move $a1,$t0
    move $a2,$s1
    syscall





    li $v0,16
    move $a0,$s2
    syscall
    j procurar_produto






possivel_produto_igual:

    addi $t0,$t0,1
    lb $t2,0($t0)

    beq $t2,44,procurar_produto

    j escrever_auxiliar







































recolher_produto_remover:
    li $v0,13
    la $a0,arquivo_temporario
    li $a1,0
    syscall
    move $s0,$v0


    li $v0,14
    move $a0,$s0
    la $a1,produto_remover
    li $a2,1024
    syscall
    move $t4,$v0
   

    li $v0,16
    move $a0,$s0
    syscall
    jr $ra











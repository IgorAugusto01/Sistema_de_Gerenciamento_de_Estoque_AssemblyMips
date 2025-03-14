.data 
arquivo: .asciiz "texto.txt"
linha: .space 1024
qtd: .word 0
.text

.globl main

main:

#abre o arquivo para leitura
li $v0,13
la $a0,arquivo
li $a1,0
syscall

#move o valor de retorno para o registrador $s0
move $s0,$v0

#inicializa o acumulador de linhas = 0
li $t0,0

loop:
#Começa o laço para ler as linhas
li $v0,14
move $a0,$s0
la $a1,linha
li $a2, 1024
syscall
#move o valor de bytes lidos para o registrador $s1
move $s1,$v0
la $a1, linha             # Reinicializa $a1 para o início do buffer
 

beq $s1,$zero,fechar_arquivo
li $t2,0
contar_quebra_de_linhas:

lb $t1,0($a1)
beq $t1,10,adicionar_acumulador
addi $a1,$a1,1
addi $t2, $t2, 1
beq $t2,$s1 loop
j contar_quebra_de_linhas







adicionar_acumulador:
addi $t0,$t0,1
addi $a1,$a1,1
j contar_quebra_de_linhas


fechar_arquivo:
li $v0,16
move $a0,$s0
syscall
j fim




fim:
sw $t0,qtd

li $v0,1
lw $a0,qtd
syscall

li $v0,10
syscall

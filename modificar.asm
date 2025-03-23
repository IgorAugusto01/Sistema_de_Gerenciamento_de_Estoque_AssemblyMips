.data
arquivo_temporario: .asciiz "temporario.txt"  
arquivo_produtos: .asciiz "produtos.txt"
arquivo_auxiliar: .asciiz "auxiliar.txt"      
linha_arquivo: .space 80
linha_temporario: .space 80
cod_temporario: .space 80
nome_temporario: .space 80
tamanho_linha:  .word 80   
string_cod: .asciiz "COD: "      
string_produto: .asciiz "; PRODUTO: "
string_requisao: .asciiz "Escreva o nome modificado: "
codigo_encontrado: .asciiz "NOME ALTERADO"
codigo_nao_encontrado: .asciiz "CODIGO NAO ALTERADO"
buffer: .space 100
nda: .ascii ""
.text


.globl main

main:
li $t7,0
  jal coletar_informacoes_temporario        #coleta as informações do arquivo temporário
  jal separar_codigo_produto                # guarda em $t1 grandeza codigo,$t2 total de bytes o nome
  add $t7,$t1,$t7
  add $t7,$t2,$t7
  addi $t7,$t7,5
  addi $t7,$t7,11

  jal calcular_espacos_brancos

li $v0, 10
syscall
  
    
    




















calcular_espacos_brancos:

    lw $s4,tamanho_linha
    sub $s5,$s4,$t7
    subi $s5,$s5,2
    jr $ra









separar_codigo_produto:

    li $t1,0    #contador para a grandeza do número
    li $t2,0    # contador para bytes do novo nome

    la $t0, linha_temporario
    la $s2, cod_temporario
    la $s3, nome_temporario

contar_codigo:
    lb $t4, 0($t0)
    addi $t0,$t0,1
    beq $t4, 59, contar_nome
    sb $t4,0($s2)
    addi $t1,$t1,1
    addi $s2,$s2,1
    j contar_codigo
    

contar_nome:
    lb $t4, 0($t0)
    addi $t0,$t0,1
    beq $t4,$zero,fim_nome
    sb $t4,0($s3)
    addi $t2,$t2,1
    addi $s3,$s3,1
    j contar_nome


fim_nome:
    sb $zero, 0($s2)
    sb $zero, 0($s3)
    jr $ra









coletar_informacoes_temporario:

    li $v0,13
    la $a0,arquivo_temporario
    li $a1,0
    syscall
    move $s0,$v0

    li $v0, 14
    move $a0, $s0
    la $a1, linha_temporario
    li $a2, 80
    syscall

    li $v0, 16
    move $a0, $s0
    syscall

    jr $ra 


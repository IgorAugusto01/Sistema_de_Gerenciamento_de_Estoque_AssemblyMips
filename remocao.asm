.data
produto_removido: .asciiz "REMOVIDO                                                                      \n"
arquivo_produtos: .asciiz "produtos.txt"  # Arquivo de produtos
arquivo_temporario: .asciiz "temporario.txt"  # Arquivo temporário com a string a ser removida
arquivo_auxiliar: .asciiz "auxiliar.txt"  # Arquivo auxiliar para escrita
produto_remover: .space 80 # Buffer para armazenar a string a ser removida
linha_procura: .space 80 # Buffer para armazenar cada linha do arquivo de produtos
cod: .byte 0  # Buffer temporário para armazenar um caractere

.text
.globl main

main:

   jal recolher_produto_remover
   jal procurar_produto


    li $v0,10
    syscall



recolher_produto_remover:

    li $v0,13
    la $a0,arquivo_temporario
    li $a1,0
    syscall
    move $s0,$v0
    
    li $v0,14
    move $a0,$s0
    la $a1,produto_remover
    li $a2,80
    syscall
    
    move $s1,$a1   #endereço do produto que será removido
    move $t0,$v0   #número de bytes que o produto a ser removido possui

    li $v0,16
    move $a0,$s0
    syscall
    
    jr $ra



procurar_produto:

    li $v0,13
    la $a0,arquivo_produtos
    li $a1,0
    syscall
    move $s0,$v0

    leitura_linha:
        li $v0,14
        move $a0,$s0
        la $a1, linha_procura
        li $a2, 80
        syscall
        move $s4,$v0
        beq $s4,$zero,fim

        move $s2, $a1

        ajuste_inicial_ponteiro:
            beq $s2, 59, fim_ajuste_inicial_ponteiro

            addi $s2, $s2, 1      
            
            j ajuste_inicial_ponteiro

        fim_ajuste_inicial_ponteiro:
            li $t3,0    # contador para comparar com $t0, que contem o tamanho do produto do arq temporario
            addi $s2, $s2, 10    # "; PRODUTO: xCOCA COLA|"

        loop_comparacao_produto:                       
            lb $t1,0($s1)
            lb $t2,0($s2)

            bne $t1,$t2,escrever_auxiliar
            
            addi $s1,$s1,1
            addi $s2,$s2,1
            addi $t3,$t3,1
            
            bne $t0,$t3,loop_comparacao_produto
            
            addi $s2,$s2,1
            lb $t2,0($s2)
            beq $t2,124,escrever_removido
            j escrever_auxiliar



        escrever_auxiliar:

            li $v0,13
            la $a0,arquivo_auxiliar
            li $a1,9
            syscall
            move $s3,$v0

            li $v0,15
            move $a0,$s3
            move $a1,$s2
            li $a2, 80
            syscall

            li $v0,16
            move $a0,$s3
            syscall
            
            j leitura_linha


        escrever_removido:
            li $v0,13
            la $a0,arquivo_auxiliar
            li $a1,9
            syscall
            move $s3,$v0

            li $v0,15
            move $a0,$s3
            la $a1,produto_removido
            li $a2, 80
            syscall

            li $v0,16
            move $a0,$s3
            syscall
            
            j leitura_linha
        
        fim:
        
        li $v0,16
        move $a0,$s0
        syscall
        jr $ra
        
        



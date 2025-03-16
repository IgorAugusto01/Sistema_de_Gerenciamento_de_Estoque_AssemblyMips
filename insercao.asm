.data
arquivo_temporario: .asciiz "temporario.txt"  
arquivo_produtos: .asciiz "produtos.txt"      
linha: .space 1024                            
string_produto: .asciiz "Produto: "
cod_string: .asciiz ", cod: "
quebra_linha: .byte '\n'
cod: .byte 0                                  

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

    
    
    jal converter_numero      
    
   
    li $v0, 15                 
    move $a0, $s0              
    la $a1, quebra_linha        
    li $a2, 1                   
    syscall

    # Fechar o arquivo de produtos
    li $v0, 16                  # Syscall para fechar arquivo
    move $a0, $s0               # Descritor do arquivo
    syscall

    lw $ra, 0($sp)              # Restaurar $ra
    addi $sp, $sp, 4
    jr $ra                      # Retornar

contar_linhas:
    addi $sp, $sp, -4           # Salvar $ra na pilha
    sw $ra, 0($sp)

    
    li $v0, 13                 
    la $a0, arquivo_produtos    
    li $a1, 0                  
    syscall
    move $s0, $v0               

    
    li $t0, 0                 

ler_linha:
    # Ler uma linha do arquivo
    li $v0, 14                  # Syscall para leitura
    move $a0, $s0               # Descritor do arquivo
    la $a1, linha               # Buffer para armazenar os dados
    li $a2, 1024                # Número máximo de bytes a serem lidos
    syscall
    move $t1, $v0               # Salvar o número de bytes lidos

    # Verificar se chegou ao final do arquivo
    beqz $t1, fim_contar_linhas  # Se nenhum byte foi lido, terminar

    # Contar as linhas
    la $a1, linha               # Carregar o endereço do buffer
    li $t2, 0                   # Contador de caracteres na linha
loop_contar:
    lb $t3, 0($a1)              # Carregar o próximo byte
    beq $t3, 10, incrementar_linha  # Se for '\n', incrementar contador de linhas
    beqz $t3, ler_linha         # Se for zero, terminar a linha
    addi $t2, $t2, 1            # Incrementar contador de caracteres
    addi $a1, $a1, 1            # Avançar para o próximo byte
    j loop_contar

incrementar_linha:
    addi $t0, $t0, 1            # Incrementar contador de linhas
    addi $a1, $a1, 1            # Avançar para o próximo byte
    j loop_contar                # Ler a próxima linha

        

fim_contar_linhas:
    # Fechar o arquivo de produtos
    li $v0, 16                  # Syscall para fechar arquivo
    move $a0, $s0               # Descritor do arquivo
    syscall

    # Salvar o número de linhas em cod
    addi $t0,$t0,1

    lw $ra, 0($sp)              # Restaurar $ra
    addi $sp, $sp, 4
    jr $ra                      # Retornar


converter_numero:

    li $t3,10
    div $t0,$t3
    mflo $t1
    mfhi $t2

    addi $t1,$t1,48
    addi $t2,$t2,48
    sb $t1,cod
    li $v0,15
    move $a0,$s0
    la $a1,cod
    li $a2,1
    syscall

    sb $t2,cod
    li $v0,15
    move $a0,$s0
    la $a1,cod
    li $a2,1
    syscall
    jr $ra
  

  
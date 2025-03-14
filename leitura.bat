echo off
java -jar "C:\Users\augus\OneDrive\Desktop\Mars4_5.jar" nc leitura.asm













#     li $v0, 13
#     la $a0, arquivo        
#     li $a1, 9               
#     syscall
#     move $s0, $v0           

   
#     # Calcular o tamanho da string
#     la $a0, msg             # Carrega o endereço da string em $a0
#     jal strlen              # Chama a função strlen
#     move $a2, $v0           # Salva o tamanho da string em $a2

#     li $v0, 15           
#     move $a0, $s0           
#     la $a1, msg             
#     syscall
    
    

   
#     li $v0, 16              
#     move $a0, $s0          
#     syscall




    
#     li $v0, 10           
#     syscall


# strlen:
#     li $v0, 0              # Inicializa o contador de tamanho ($v0 = 0)
# strlen_loop:
#     lb $t0, 0($a0)         # Carrega o byte atual da string em $t0
#     beqz $t0, strlen_end    # Se o byte for \0, termina o loop
#     addi $v0, $v0, 1       # Incrementa o contador de tamanho
#     addi $a0, $a0, 1       # Avança para o próximo byte da string
#     j strlen_loop           # Volta para o início do loop
# strlen_end:
#     jr $ra                 # Retorna para o chamador
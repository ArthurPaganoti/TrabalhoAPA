import re # Biblioteca para manipulação de expressões regulares
import time # Biblioteca para manipulação de tempo
import math # Biblioteca para manipulação de funções matemáticas

def identifica_laco(codigo, n): # Função que identifica o tipo de laço e a complexidade
    global iteracoes

    # Verifica se no código que o no código inserido possui as palavras-chave for, while ou do
    tipo_laco = re.search("(for|while|do)", codigo)
    tipo_laco = tipo_laco.group() if tipo_laco else "Unknown" # Se não existir, retorna "Unknown"

# Modifica o código inserido pelo úsuario para que seja possível contar o número de iterações
    codigo_modificado = f'''
global iteracoes, n
iteracoes = 0
n = {n}
{codigo}
iteracoes += 1
'''

# Inicia a contagem de tempo e executa o código modificado
    start_time = time.time()
    exec(codigo_modificado, globals())
    end_time = time.time()

    Tn = end_time - start_time # Calcula o tempo de execução

# Verifica a complexidade do código com base no contador de iterações e no tempo de execução
    if tipo_laco == "for" or tipo_laco == "while":
        if n == 1:
            complexidade = "O(1)"
        elif Tn <= math.log(n, 2) + 0.1 and Tn >= math.log(n, 2) - 0.1:
            complexidade = "O(log n)"
        elif Tn > 0 and abs(math.log(Tn, 2) - (math.log(n, 2) * math.log(n, 2))) < 0.1:
            complexidade = "O(n log n)"
        elif codigo.count(tipo_laco) == 3:
            complexidade = "O(n^3)"
        elif codigo.count(tipo_laco) > 1:
            complexidade = "O(n^2)"
        elif Tn == n:
            complexidade = "O(2^n)"
        else:
            complexidade = "O(n)"
    else:
        complexidade = "Unknown"

    return tipo_laco, complexidade, Tn # Retorna o tipo de laço, a complexidade e o tempo de execução

# Função principal
def main():
    print("Insira o código com laço de repetição (termine com uma linha vazia): ")
    codigo = ""
    while True: # Loop para inserir o código
        linha = input()
        if linha:
            codigo += linha + '\n'
        else:
            break

    tipo_laco, complexidade, Tn = identifica_laco(codigo, 10) # Chama a função identifica_laco

# Retorna os resultados
    print(f"Tipo de laço: {tipo_laco}")
    print(f"Complexidade: {complexidade}")
    print(f"T(n): {Tn}")


if __name__ == "__main__":
    main()
    input("Pressione Enter para finalizar...")
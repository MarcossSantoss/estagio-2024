# 1)

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# 2)

def pertence_sequencia_fibonacci(numero):
    fib1, fib2 = 0, 1

    while fib2 <= numero:
        if fib2 == numero:
            return True
        fib1, fib2 = fib2, fib1 + fib2

    return False

# Exemplo: verificando se o número 21 pertence à sequência de Fibonacci
numero_informado = 21
if pertence_sequencia_fibonacci(numero_informado):
    print(f"{numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_informado} não pertence à sequência de Fibonacci.")

# 3)

# a) 1, 3, 5, 7, 9
# b) 2, 4, 8, 16, 32, 64, 128
# c) 0, 1, 4, 9, 16, 25, 36, 49
# d) 4, 16, 36, 64, 100
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2, 10, 12, 16, 17, 18, 19, 20

# 4)

# Identificação dos Interruptores:
# Ligue o primeiro interruptor e aguarde alguns minutos.
# Desligue o primeiro interruptor e ligue o segundo interruptor.
# Entre na sala das lâmpadas.

# Observação na Sala das Lâmpadas:
# Se a lâmpada estiver acesa, o segundo interruptor controla essa lâmpada.
# Se a lâmpada estiver apagada, toque na lâmpada. Se ela estiver quente, o primeiro interruptor controla essa lâmpada.
# Se ela estiver fria, o terceiro interruptor controla essa lâmpada.

# No primeiro passo, identifica dois interruptores. Se a lâmpada estiver acesa quando entrar na sala,
# o segundo interruptor a controla. Se estiver apagada, já sabe que o primeiro interruptor controla essa lâmpada
# e o terceiro interruptor controla a outra.

# 5)

def inverter_string(string):
    tamanho = len(string)
    string_invertida = ""

    # Loop para inverter a string
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

# Exemplo de uso
entrada = input("Digite uma string: ")
resultado = inverter_string(entrada)

print("String original:", entrada)
print("String invertida:", resultado)

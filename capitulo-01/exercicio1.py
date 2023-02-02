#1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?

print()
#R: Imprime na tela uma linha em branco

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?

print(hello world)
#R: Erro de sintaxe por não incluir as ""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?

++2
2++2
#R: Realiza a operação dos sinais matemáticos, atribui ao número que vai a frente um resultado positivo ou negativo, como o sinal de + (positivo) somado a outro +(positivo) resulta em um número positivo. O mesmo comportamento serve para o símbolo - (negativo).
#   Adicionando mais e um sinal, realiza a operação matemática correspondente ao primeiro sinal e o segundo atribui um resultado(negativo ou positivo) ao número.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?

02
#R: Erro de sintaxe, não é permitido a inclusão de 0 antes de um número inteiro literal, apenas para inteiros octais.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#5. O que acontece se você tiver dois valores sem nenhum operador entre eles?

42 42
#R: Erro de sintaxe, o python espera que contenha um operador entre os números inteiros. Mas caso sejam duas strings, é impresso na tela ambas strings juntas.

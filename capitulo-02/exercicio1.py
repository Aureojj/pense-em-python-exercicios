# Exercícios realizados no modo interativo

#1. Vimos que n = 42 é legal. E 42 = n?

42 = 'n'

#R: SyntaxError: can't assign to literal; Em Python valores literais não podem ser adicionados como variáveis 
#----------------------------------------------------------------------------------------------------------------

#2. Ou x = y = 1?

X = Y = 1

#R: No terminal interativo nada acontece, entretanto, se colocarmos para imprimir na tela a variável X
# ela irá conter o valor de 1, pois o valor foi atribuído a variável Y que foi atribuída a X.
#----------------------------------------------------------------------------------------------------------------

#3. Em algumas linguagens, cada instrução termina em um ponto e vírgula ;. O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?

print('hello world');

#R: A instrução é executa sem apresentar erro, o que leva a crer que é ignorada.
#----------------------------------------------------------------------------------------------------------------

#4. E se puser um ponto no fim de uma instrução?

print('hello world').

#R: Ocorre o error de sintaxe, pois ele espera que venha outro argumento após o ponto.
#----------------------------------------------------------------------------------------------------------------

#5. Em notação matemática é possível multiplicar x e y desta forma: xy. O que acontece se você tentar fazer o mesmo no Python?

X = 5 
Y = 6
print(XY)

#R: NameError xy não está definido, com isso, concluímos que ele entende xy como uma nova variável.

#Lara Franco Chaves Vidal

#OBS.: Para mudar o arquivo .txt, modificar na linha 51

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
#3 
#abbaba 
#abababb 
#bbabbaaab 
#Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado da validação conforme o formato indicado a seguir: 
#abbaba: não pertence.   
#A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída. Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de testes criado pelo próprio professor.  


#Iniciei definindo a função para validar as strings de entrada como possível:
def validando_entrada(entrada):
  #Variável validacao será a variável para retorno bool
  validacao = True
  #Alfabeto com as letras possíveis, segundo o enunciado
  alfabeto = ['a', 'b', 'c']
  #Verifica o tamanho da string de entrada
  lenght = len(entrada)

  #Agora, vou verificar cada caracter da string individualmente, por meio de um for ainda dentro da função de validação de entrada:
  for i in range(0, lenght):
    caracter = entrada[i]

    #No caso de ser um caracter que não está incluso no alfabeto do enunciado:
    if caracter not in alfabeto:
      return False

    #Dado que a regra é ter dois B's após a letra A, não pode haver nenhum A na última ou penúltima posição. Então já iremos eliminar logo a possibilidade
    elif caracter == 'a':
      if i == lenght - 1 or i == lenght - 2:
        return False
      #Se não for este o caso, continuarei checando os demais caracteres normalmente
      elif entrada[i+1] == 'b' and entrada[i+2] == 'b':
        return True
      else:
        return False

  return validacao


#Agora começarei a mexer com o arquivo .txt
#Nome do arquivo

#Caso queira rodar o código com outra string de entrada, é preciso mudar o nome abaixo
#with fecha automaticamente o arquivo após ter sido utilizado no código
with open('string1.txt') as dados:
  strings = dados.readlines()
  num_palavras = int(strings[0])

  #Verificando se o número inteiro da primeira linha (a quantidade de strings do arquivo) está correto
  if len(strings) == num_palavras + 1:
    contador = 1
    #Verificando as strings dos txt individualmente
    while contador <= num_palavras:
      #Neste momento vamos eliminar o "\n" e verificar com a função criada no início deste código
      entrada = strings[contador].strip('\n')
      saida = validando_entrada(entrada)

      #Finalmente, vamos printar o resultado da validação
      #TRUE
      if saida:
        print("%s: pertence" % entrada)
      #FALSE
      else:
        print("%s: não pertence" % entrada)
      contador += 1

  #ERRO
  else:
    print("ERRO. A quantidade de strings inseridas no arquivo, segundo o que está escrito na linha inicial, não corresponde com a quantidade de strings verdadeiramente contidas.")
        
        
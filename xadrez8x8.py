'''
melhorar a função de captura

'''
def transformaCords(cords):
  
  if len(cords) != 2:
   print("Use formato A1")
   return None

  elif not cords[1].isdigit():
    print("Segundo caractere precisa ser número")
    return None


  letras = ["a","b","c","d","e","f","g","h"]
  
  cords = cords.strip()
  
  try:
    coluna = letras.index(cords[0].lower())
  except ValueError:
    print("Faça outro movimento")
    return None
  try:
    linha =  8 - int(cords[1]) 
  except ValueError:
    return None
  if linha > 8:
    return None
  listaDeCords = [linha, coluna]

  return listaDeCords

def pegarIdDoMoveAnterior(coordenadas, matriz):
  id_da_peca = matriz[coordenadas[0]][coordenadas[1]] #pegar o id da posição na matriz

  return id_da_peca

def movimentoNaMatriz(coordenadasAtual, coordenadasAnterior, matriz,dados, id):
  match dados[id]["tipo"]:
    case "p" | "P":
     if captura(coordenadasAtual,matriz) and not verificarP(coordenadasAtual, coordenadasAnterior, dados, id):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     elif veficarVazio(coordenadasAtual, matriz) and verificarP(coordenadasAtual, coordenadasAnterior, dados, id) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "t" | "T":
     if captura(coordenadasAtual,matriz) and  verificarT(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarT(coordenadasAtual, coordenadasAnterior) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "b" | "B":
     if captura(coordenadasAtual,matriz) and  verificarB(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarB(coordenadasAtual, coordenadasAnterior) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "c" | "C":
     if captura(coordenadasAtual,matriz) and  verificarC(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarC(coordenadasAtual, coordenadasAnterior):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "r" | "R":
     if captura(coordenadasAtual,matriz) and  verificarR(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarR(coordenadasAtual, coordenadasAnterior) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "q" | "Q":
     if captura(coordenadasAtual,matriz) and  verificarQ(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarQ(coordenadasAtual, coordenadasAnterior) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

def verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz):
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1] #4,2
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1] #2,2
  

  difLinha = (linhaA - linhaB) #2
  difColuna = (colunaA - colunaB) #0

  linha_step = 0 if difLinha == 0 else (1 if difLinha > 0 else -1)
  coluna_step = 0 if difColuna == 0 else (1 if difColuna > 0 else -1)

  linha, coluna = linha_step + linhaB, coluna_step + colunaB 

  while (linha,coluna) != (linhaA, colunaA):
    if matriz[linha][coluna] != 0:
      return False
    linha += linha_step
    coluna += coluna_step

  return True

def verificaAtaque(coordenadasAtual, coordenadasAnterior, matriz, dados, idPeca):
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  tipo = dados[idPeca]["tipo"]

  if tipo.lower() == "c":
    return (difColuna == 1 and difLinha == 2) or (difColuna == 2 and difLinha == 1) 
  
  if tipo.lower() == "b":
    return (difLinha == difColuna) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz)
  
  if tipo.lower() == "t":
    return (difColuna == 0 or difLinha == 0) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz)
  
  if tipo.lower() == "q":
    return (difLinha == difColuna or linhaA == linhaB or colunaA == colunaB) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz)
  
  if tipo.lower() == "r":
    return (max(difLinha, difColuna) == 1) and verificarCaminho(coordenadasAtual, coordenadasAnterior, matriz)
  
  if tipo.lower() == "p":
     direcao = - 1 if dados[idPeca]["cor"] == "branco" else 1
     return (linhaA == linhaB + direcao) and difColuna == 1

def acharRei(matriz, dados, cor):
  for i in range(0,8):
    for j in range(0,8):
      idPeca = matriz[i][j]
      if idPeca != 0:
        if dados[idPeca]["tipo"].lower() == "r" and dados[idPeca]["cor"] == cor:
         return i, j

def xeque(matriz, dados, cor_rei):
  posRei = acharRei(matriz, dados, cor_rei)
  for i in range(0,8):
    for j in range(0,8):
      idPeca = matriz[i][j]
  
      if idPeca != 0 and dados[idPeca]["cor"] != cor_rei:
        if verificaAtaque((i,j), posRei, matriz, dados, idPeca):
          return True
  return False

def verificarP(coordenadasAtual, coordenadasAnterior, dados, id):
  valido = True
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  if difLinha == 1 or difLinha == 2 and difColuna == 0 and dados[id]["primeiroMove"] == True:
    valido = True
    dados[id]["primeiroMove"] = False
    print("Duas casa")
  elif difLinha == 1 and difColuna == 0:
    valido = True
    print("uma casa")
  else: 
    valido = False
    print("movimento invalido")
  return valido

def verificarC(coordenadasAtual, coordenadasAnterior):
  valido = True
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1] 
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  if difLinha <= 2 and difColuna <= 2:
    valido = True
  else:
    print("movimento invalido")
    valido = False
  return valido

def verificarT(coordenadasAtual, coordenadasAnterior):
  valido = True
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  if difColuna == 0 or difLinha == 0:
    valido = True
  else:
    print("movimento invalido")
    valido = False  
  return valido

def verificarB(coordenadaAtual, coordenadasAnterior):
  linhaA, colunaA = coordenadaAtual[0], coordenadaAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]
  i = 0
  j = 0
  valido = True
  while True:
    difLinha = abs(linhaA- linhaB) - i
    difColuna = abs(colunaA - colunaB ) - j

    if difLinha != 0: 
     i += 1
    else: i += 0
 
    if difColuna != 0:
       j += 1
    else: j += 0

    if i != j:
     valido = False
     break
    elif difColuna == 0 and difLinha == 0 and i == j:
      valido = True
      break

  return valido

def verificarR(coordenadasAtual, coordenadasAnterior):
  valido = True
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  if difLinha == 0 and difColuna == 1 or difLinha == 1 and difColuna == 0 or difLinha == 1 and difColuna == 1:
    valido == True
  else: valido = False
  return valido

def verificarQ(coordenadasAtual, coordenadasAnterior):
  valido = True
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  if difLinha == 0 or difColuna == 0:
    valido = True
    return print(valido)

  i = 0
  j = 0
  while True:
   difLinha = abs(linhaA- linhaB) - i
   difColuna = abs(colunaA - colunaB ) - j

   if difLinha != 0:
    i += 1
   else: i += 0

   if difColuna != 0:
      j += 1
   else: j += 0

   if i != j:
    valido = False
    break
   elif difColuna == 0 and difLinha == 0 and i == j:
     valido = True
     break

  return valido

def veficarVazio(coordenadasAtual, matriz):
  valido = True
  move = matriz[coordenadasAtual[0]][coordenadasAtual[1]]
  if move == 0:
    return (valido)
  else: 
    print("Há uma peça no local")
    valido = False
    return valido

def verificarVazioAnterior(coordenadasAnterior, matriz):
  move = matriz[coordenadasAnterior[0]][coordenadasAnterior[1]]
  if move == 0:
    print("Não pode escolher um local vazio")
    return False
  else: 
    return True

def captura(coordenadasAtual, matriz):
  valido = True
  move = matriz[coordenadasAtual[0]][coordenadasAtual[1]]
  if move != 0:
    return valido 
  else:
    print("Captura não pode ser realizada")
    valido = False
    return valido
  
def print_tabuleiro(matriz, dados):
  for linha in matriz:
   for casa in linha:
    if casa == 0:
      print(".", end=" ")
    else:
      print(dados[casa]["tipo"], end=" ")
   print()

 
xadrez = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [16,15,14,13,12,11,10,9],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [24,23,22,21,20,19,18,17],
    [32,31,30,29,28,27,26,25],
]

dadosPecas = {
  1: {"tipo": "T", "cor": "preto"},
  2: {"tipo": "C", "cor": "preto"},
  3: {"tipo": "B", "cor": "preto"},
  4: {"tipo": "Q", "cor": "preto"},
  5: {"tipo": "R", "cor": "preto"},
  6: {"tipo": "B", "cor": "preto"},
  7: {"tipo": "C", "cor": "preto"},
  8: {"tipo": "T", "cor": "preto"},
  9: {"tipo": "P", "cor": "preto","primeiroMove": True},
  10: {"tipo": "P", "cor": "preto","primeiroMove": True},
  11: {"tipo": "P", "cor": "preto","primeiroMove": True},
  12: {"tipo": "P", "cor": "preto","primeiroMove": True},
  13: {"tipo": "P", "cor": "preto","primeiroMove": True},
  14: {"tipo": "P", "cor": "preto","primeiroMove": True},
  15: {"tipo": "P", "cor": "preto","primeiroMove": True},
  16: {"tipo": "P", "cor": "preto","primeiroMove": True},
  17: {"tipo": "p", "cor": "branco","primeiroMove": True},
  18: {"tipo": "p", "cor": "branco","primeiroMove": True},
  19: {"tipo": "p", "cor": "branco","primeiroMove": True},
  20: {"tipo": "p", "cor": "branco","primeiroMove": True},
  21: {"tipo": "p", "cor": "branco","primeiroMove": True},
  22: {"tipo": "p", "cor": "branco","primeiroMove": True},
  23: {"tipo": "p", "cor": "branco","primeiroMove": True},
  24: {"tipo": "p", "cor": "branco","primeiroMove": True},
  25: {"tipo": "t", "cor": "branco"},
  26: {"tipo": "c", "cor": "branco"},
  27: {"tipo": "b", "cor": "branco"},
  28: {"tipo": "r", "cor": "branco"},
  29: {"tipo": "q", "cor": "branco"},
  30: {"tipo": "b", "cor": "branco"},
  31: {"tipo": "c", "cor": "branco"},
  32: {"tipo": "t", "cor": "branco"},
}

cor = "preto"



#print(verificarCaminho(transformaCords("c1"), transformaCords("b2"), xadrez))

#movimentoNaMatriz(transformaCords("e5"), transformaCords("f3"), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords("f3"),xadrez))


jogo = True
movimentoBranco = True
movimentoPreto = True
xequeBool = True


while jogo:
  print_tabuleiro(xadrez, dadosPecas)
  match xeque(xadrez, dadosPecas, "branco"):
    case True:
       while True:
        print("Seu rei está atacado, faça um movimento que saia do xeque.")
       

        movimentoAnterior = input("Digite a coordenada da peça que quer mover: ").lower()

        if transformaCords(movimentoAnterior) == None:
          continue

        idDaPeca = pegarIdDoMoveAnterior(transformaCords(movimentoAnterior), xadrez)


        print(f" peça escolhida {dadosPecas[idDaPeca]["tipo"]}")
        movimentoAtual = input("Digite a coordenada que a peça iria ficar: ").lower()

        if transformaCords(movimentoAnterior) == None:
         continue

        if xeque(xadrez, dadosPecas, "branco"):
          print("Rei ainda está em xeque, outro movimento")
          xequeBool = True
        else:
          movimentoNaMatriz(transformaCords(movimentoAtual), transformaCords(movimentoAnterior), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords(movimentoAnterior),xadrez))
          print_tabuleiro(xadrez, dadosPecas)
          movimentoBranco = False
          movimentoPreto = True
          break
  
    case False:
     while movimentoBranco:
    
       movimentoAnterior = input("Digite a coordenada da peça que quer mover: ").lower()
       
       if transformaCords(movimentoAnterior) == None:
         continue
       
       if pegarIdDoMoveAnterior(transformaCords(movimentoAnterior), xadrez) == 0:
          print("Faça outro movimento.")
          continue
       
         
       idDaPeca = pegarIdDoMoveAnterior(transformaCords(movimentoAnterior), xadrez)
       print(f" peça escolhida {dadosPecas[idDaPeca]["tipo"]}")
       movimentoAtual = input("Digite a coordenada que a peça iria ficar: ").lower()

       if transformaCords(movimentoAtual) == None:
         continue
         
       if verificarVazioAnterior(transformaCords(movimentoAnterior), xadrez) == False:
         print("Faça outro movimento")
       else:
        movimentoNaMatriz(transformaCords(movimentoAtual), transformaCords(movimentoAnterior), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords(movimentoAnterior),xadrez))
        print_tabuleiro(xadrez, dadosPecas)

        movimentoBranco = False
        movimentoPreto = True
        break
       
  match xeque(xadrez, dadosPecas, "preto"): 
   case True:
    while xequeBool:
      print("seu rei está em xeque, mova ele para sair do xeque")

      movimentoAnteriorP = input("Digite a coordenada da peça que quer mover: ").lower()

      if transformaCords(movimentoAnterior) == None:
         continue

      if pegarIdDoMoveAnterior(transformaCords(movimentoAnterior), xadrez) == 0:
          print("Faça outro movimento.")
          continue
      
      idDaPeca = pegarIdDoMoveAnterior(transformaCords(movimentoAnterior), xadrez)
      print(f" peça escolhida {dadosPecas[idDaPeca]["tipo"]}")
      movimentoAtualP = input("Digite a coordenada que a peça iria ficar: ").lower()

      if transformaCords(movimentoAtualP) == None:
         continue

      if xeque(xadrez, dadosPecas, "preto"):
        print("Rei ainda está em xeque, faça outro movimento")
      else:
        movimentoNaMatriz(transformaCords(movimentoAtual), transformaCords(movimentoAnterior), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords(movimentoAnterior),xadrez))
        print_tabuleiro(xadrez, dadosPecas)

        movimentoBranco = False
        movimentoPreto = True
        break
      


   case False:
    
       while movimentoPreto:
  
        movimentoAnteriorP = input("Digite a coordenada da peça que quer mover: ").lower()

        if transformaCords(movimentoAnterior) == None:
         continue

        if pegarIdDoMoveAnterior(transformaCords(movimentoAnteriorP), xadrez) == 0:
          print("Faça outro movimento.")
          continue

        idDaPeca = pegarIdDoMoveAnterior(transformaCords(movimentoAnteriorP), xadrez)
        print(f" peça escolhida {dadosPecas[idDaPeca]["tipo"]}")
        movimentoAtualP = input("Digite a coordenada que a peça iria ficar: ").lower()

        if transformaCords(movimentoAtualP) == None:
         continue

        if verificarVazioAnterior(transformaCords(movimentoAnteriorP), xadrez) == False:
          print("Faça outro movimento")
        else:
         movimentoNaMatriz(transformaCords(movimentoAtualP), transformaCords(movimentoAnteriorP), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords(movimentoAnteriorP),xadrez))
         print_tabuleiro(xadrez, dadosPecas)

        movimentoPreto = False
        movimentoBranco = True


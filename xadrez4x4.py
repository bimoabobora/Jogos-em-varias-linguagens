

def transformaCords(cords):
 
  letras = ["a","b","c","d","e","f","g","h"]
  
  
  coluna = letras.index(cords[0].lower())
  linha =  8 - int(cords[1]) 
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
     elif veficarVazio(coordenadasAtual, matriz) and verificarP(coordenadasAtual, coordenadasAnterior, dados, id):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "t" | "T":
     if captura(coordenadasAtual,matriz) and not verificarT(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarT(coordenadasAtual, coordenadasAnterior):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "b" | "B":
     if captura(coordenadasAtual,matriz) and not verificarB(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarB(coordenadasAtual, coordenadasAnterior):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "c" | "C":
     if captura(coordenadasAtual,matriz) and not verificarC(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarC(coordenadasAtual, coordenadasAnterior):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "r" | "R":
     if captura(coordenadasAtual,matriz) and not verificarR(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarR(coordenadasAtual, coordenadasAnterior):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

    case "q" | "Q":
     if captura(coordenadasAtual,matriz) and not verificarQ(coordenadasAtual, coordenadasAnterior):
       matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
       matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0
     if veficarVazio(coordenadasAtual, matriz) and verificarQ(coordenadasAtual, coordenadasAnterior):
      matriz[coordenadasAtual[0]][coordenadasAtual[1]] = id
      matriz[coordenadasAnterior[0]][coordenadasAnterior[1]] = 0

def verificarP(coordenadasAtual, coordenadasAnterior, dados, id):
  valido = True
  linhaA, colunaA = coordenadasAtual[0], coordenadasAtual[1]
  linhaB, colunaB = coordenadasAnterior[0], coordenadasAnterior[1]

  difLinha = abs(linhaA - linhaB)
  difColuna = abs(colunaA - colunaB)

  if difColuna == 0 and difLinha == 1 or difLinha == 2 and dados[id]["primeiroMove"] == True:
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



#verificarP(transformaCords("e4"), transformaCords("e2"), dadosPecas, pegarIdDoMoveAnterior(transformaCords("e2"), xadrez))

#movimentoNaMatriz(transformaCords("c6"), transformaCords("b8"), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords("b8"),xadrez))
#print_tabuleiro(xadrez, dadosPecas)

#interface de usuario

jogo = True
movimentoBranco = True
movimentoPreto = True


while jogo:
  print_tabuleiro(xadrez, dadosPecas)
  while movimentoBranco:
    movimentoAnterior = input("Digite a coordenada da peça que quer mover: ").lower()
    movimentoAtual = input("Digite a coordenada que a peça iria ficar: ").lower()

    if verificarVazioAnterior(transformaCords(movimentoAnterior), xadrez) == False:
      print("Faça outro movimento")
    else:
     movimentoNaMatriz(transformaCords(movimentoAtual), transformaCords(movimentoAnterior), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords(movimentoAnterior),xadrez))
     print_tabuleiro(xadrez, dadosPecas)

     movimentoBranco = False
     movimentoPreto = True

  while movimentoPreto:
    movimentoAnteriorP = input("Digite a coordenada da peça que quer mover: ").lower()
    movimentoAtualP = input("Digite a coordenada que a peça iria ficar: ").lower()

    if verificarVazioAnterior(transformaCords(movimentoAnteriorP), xadrez) == False:
      print("Faça outro movimento")
    else:
     movimentoNaMatriz(transformaCords(movimentoAtualP), transformaCords(movimentoAnteriorP), xadrez, dadosPecas, pegarIdDoMoveAnterior(transformaCords(movimentoAnteriorP),xadrez))
     print_tabuleiro(xadrez, dadosPecas)

     movimentoPreto = False
     movimentoBranco = True

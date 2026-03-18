

def transformaCords(cords):
 
  letras = ["a","b","c","d","e","f","g","h"]
 
  coluna = letras.index(cords[0]) 
  linha = 8 - int(cords[1]) 

  return linha, coluna

def removerP(coordenadas, matriz,):
  cords = list(coordenadas)
  for i in range(0,8):
   for j in range(0,8):
    if matriz[i][j] == idp[1]:
      matriz[i][cords[1]] = "."
   
def verificarC(coordenadas):
  valido = True
  cords = list(coordenadas)
  
  if cords[0] - matrizPosicao == 2 or cords[0] - matrizPosicao == 1:
      return valido 
  else:
      valido = False
      print("movimento invalido")
      return valido

def movimento(coordenadaMatriz, matriz, peca):
    linha, coluna = transformaCords(coordenadaMatriz)
    

    if verificarC((linha, coluna)) == True and peca == "c":
       matriz[linha][coluna] = peca

    elif peca == "p" or peca == "P":
      removerP((linha,coluna), matriz)
      matriz[linha][coluna] = peca
      

    

movimentandoBranco = True
movimentandoPreto = False
mostrar = False
jogo = True

while jogo:
 xadrez = [
    ["t","c","b","q","r","b","c","t"],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    ["T","C","B","Q","R","B","C","T"],
]
 idp = {
   1: xadrez[1][0],
   2: xadrez[1][1],
   3: xadrez[1][2],
   4: xadrez[1][3],
   5: xadrez[1][4],
   6: xadrez[1][5],
   7: xadrez[1][6],
   8: xadrez[1][7]
}
 idc = {
   1: (xadrez[0]),
   2: xadrez[0]
 }

 while movimentandoBranco:
  move = input("Digite seu movimento: ").lower()
  peca = input("Qual peça: ").lower()
  if move == "a1" or move == "b1" or move == "c1" or move == "d1":
     print("Movimento invalido, faça outro.")
     movimentandoBranco = True
  else:
     movimentandoBranco = False
     movimentandoPreto = True
     mostrar1 = True

  while movimentandoPreto:
   move = input("Digite seu movimento: ").lower()
   peca = input("Qual peça: ").capitalize()
   if move == "a6" or move == "b6" or move == "c6" or move == "d6":
     print("Movimento invalido, faça outro.")
     movimentandoPreto = True
   else:
      movimentandoPreto = False
      mostrar2 = True

  while mostrar1 == True and mostrar2 == True:
   movimento(move, xadrez, peca)

   for row in xadrez:
     print(row)
 
     mostrar1 = False
     mostrar2 = False
     movimentandoBranco = True
     movimentandoPreto = True
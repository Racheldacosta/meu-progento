# Registrar o e a sua nata...
Conteudo = input("qual o filme ou série preferido? ")
Avaliação = int(input("Atrbuir uma nota de 1 a 5: "))

# Realizar a avaliação...
match Avaliação:
    case 1:
        print("pésssimo!")
        porque = input("Descreva porque a avaliação foi baixo: ")
     case 2:
        print("Rui!")
        porque = input("Descreva porque a avaliação foi baixa: ")
     case 3:
        print("Razoável!")
        porque = input("Descreva porque a avaliação foi media: ")
     case 4:
        print("Bom!")
        porque = input("Descreva porque a avaliação foi bom: ")
     case 5:
        print("Ótimo!")
        porque = input("Descreva porque a avaliação foi ótimo: ")
     case 1:
       print("Oção nõa reconhecida...!")
       porque = input("Descreva porque a avaliação foi baixo: ")  

1 # Demostação do uso da condicional match/ case...
2 print("digite o número referente ao estado da moeda:")
3 print("1. flor de cunho")
4 print("2. soberba")
5 print("3. muito bem conservada")
6 print("4. bem conservada")
7 print("5. outros estados")
8 Estado = int(input())
9
10 match Estado:
11   case 1:
12    print("perfeital vou pagar R$1 1.000.000,00!")
13    case 2:
14      print("Quase perfeito!ofeereço  R$ 250.000,00!")
15    case 3:
16      print("Que ótimo! posso dar uns R$ 100.000,00!")
17    case 4:  
18      print("Que bom. aceitaria R$1 30.000,00?") 
19    case 5:
20      print("desculpe, não aceito neste estado.")
21    case =:
22       print("opção não reconhecida!")


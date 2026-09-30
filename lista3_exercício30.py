peso = int(input("Digite o peso (Kg) do peixe: "))

peso_excedente = peso - 50

multa = peso_excedente * 4

print(f"O peso passou do limite das normas, a multa é de R${multa}")

if peso <= 50:
    print("O peso do peixe está dentro das normas")

    
    
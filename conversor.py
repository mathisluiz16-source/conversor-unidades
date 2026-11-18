"""Conversor de unidades.

Programa de terminal com menu interativo que converte:
- Celsius para Fahrenheit
- Quilômetros para milhas
- Quilogramas para libras
"""


def celsius_para_fahrenheit(c):
    """Converte uma temperatura de graus Celsius para Fahrenheit.

    Fórmula: F = C * 9/5 + 32

    Args:
        c (float): temperatura em graus Celsius.

    Returns:
        float: temperatura equivalente em graus Fahrenheit.
    """
    return c * 9 / 5 + 32


# Alias com a grafia usada no enunciado do exercício.
celsius_para_fahreheit = celsius_para_fahrenheit


def km_para_milhas(km):
    """Converte uma distância de quilômetros para milhas.

    Fórmula: milhas = km * 0,621371

    Args:
        km (float): distância em quilômetros.

    Returns:
        float: distância equivalente em milhas.
    """
    return km * 0.621371


def kg_para_libras(kg):
    """Converte uma massa de quilogramas para libras.

    Fórmula: libras = kg * 2,20462

    Args:
        kg (float): massa em quilogramas.

    Returns:
        float: massa equivalente em libras.
    """
    return kg * 2.20462


def ler_numero(mensagem):
    """Lê um número digitado pelo usuário, repetindo até ser válido.

    Aceita vírgula ou ponto como separador decimal.

    Args:
        mensagem (str): texto exibido ao pedir o valor.

    Returns:
        float: o número digitado pelo usuário.
    """
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def exibir_menu():
    """Exibe as opções do menu principal no terminal."""
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1 - Celsius para Fahrenheit")
    print("2 - Quilômetros para milhas")
    print("3 - Quilogramas para libras")
    print("0 - Sair")


def main():
    """Executa o menu interativo até o usuário escolher sair."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            c = ler_numero("Temperatura em °C: ")
            print(f"{c:.2f} °C = {celsius_para_fahrenheit(c):.2f} °F")
        elif opcao == "2":
            km = ler_numero("Distância em km: ")
            print(f"{km:.2f} km = {km_para_milhas(km):.2f} milhas")
        elif opcao == "3":
            kg = ler_numero("Massa em kg: ")
            print(f"{kg:.2f} kg = {kg_para_libras(kg):.2f} libras")
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 0, 1, 2 ou 3.")


if __name__ == "__main__":
    main()

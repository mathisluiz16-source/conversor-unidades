# Conversor de Unidades

Programa em Python com menu interativo no terminal para converter unidades,
usando uma função dedicada para cada tipo de conversão.

## Conversões disponíveis

| Opção | Conversão               | Função                                 |
|-------|-------------------------|----------------------------------------|
| 1     | Celsius → Fahrenheit    | `celsius_para_fahrenheit(c)`           |
| 2     | Quilômetros → milhas    | `km_para_milhas(km)`                   |
| 3     | Quilogramas → libras    | `kg_para_libras(kg)`                   |
| 0     | Sair do programa        | —                                      |

> A função também está disponível com o nome `celsius_para_fahreheit(c)`,
> conforme a grafia do enunciado.

## Requisitos

- Python 3.6 ou superior (não usa bibliotecas externas)

## Como executar

```bash
git clone <URL-DO-SEU-REPOSITORIO>
cd <NOME-DO-REPOSITORIO>
python conversor.py
```

No Linux/macOS, use `python3 conversor.py` se `python` não funcionar.

## Exemplo de uso

```
=== CONVERSOR DE UNIDADES ===
1 - Celsius para Fahrenheit
2 - Quilômetros para milhas
3 - Quilogramas para libras
0 - Sair
Escolha uma opção: 1
Temperatura em °C: 100
100.00 °C = 212.00 °F
```

O menu se repete até você digitar `0`. Valores inválidos (letras, por exemplo)
e opções inexistentes são tratados sem encerrar o programa. Você pode usar
vírgula ou ponto como separador decimal.

## Fórmulas utilizadas

- Fahrenheit = Celsius × 9/5 + 32
- Milhas = km × 0,621371
- Libras = kg × 2,20462

## Estrutura do projeto

```
.
├── conversor.py   # código-fonte
└── README.md      # documentação
```

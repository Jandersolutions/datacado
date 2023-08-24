# Datacado

Datacado é um pacote Python para gerar dados fictícios de vendas em formato CSV. Ele utiliza a biblioteca Faker para criar informações de vendas aleatórias, como CPFs, produtos, preços, quantidades, datas e mais. É útil para criar conjuntos de dados simulados para fins de teste, aprendizado de máquina ou análise.

## Instalação

Para instalar o pacote, você pode usar o pip. Abra um terminal e execute o seguinte comando:

```bash
pip install datacado
```

## Uso

Após instalar o pacote, você pode utilizar a função `generate_sales_data` para gerar dados fictícios de vendas. Veja um exemplo de uso:

```python
from datacado import main

num_records = 100
mes = 8
ano = 2023
num_cpf = 50
num_op = 5

main.generate_sales_data(num_records, mes, ano, num_cpf, num_op)
```

## Parâmetros

A função `generate_sales_data` aceita os seguintes parâmetros:

- `num_records`: O número de registros de venda a serem gerados.
- `mes`: O número do mês desejado.
- `ano`: O ano desejado.
- `num_cpf`: A quantidade de CPFs (clientes) a serem gerados.
- `num_op`: A quantidade de operadoras a serem geradas.

## Mantenedor

Este pacote é mantido por [Jandersolutions](https://github.com/Jandersolutions).

## Licença

Este projeto é licenciado sob a Licença MIT 




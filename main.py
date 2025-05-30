import json

def lambda_handler(event, context):
    """
    Função Lambda simples que recebe um JSON com chave "input"
    e retorna um JSON com chave "output".
    Exemplo de evento de entrada:
    {
        "input": "Olá, Lambda!"
    }
    """
    # Obtém o dado de entrada
    input_data = event.get("input", "")

    # Processamento: converte para maiúsculas
    output_data = input_data.upper()

    # Formata a resposta como API
    return {
        "statusCode": 200,
        "body": json.dumps({"output": output_data})
    }

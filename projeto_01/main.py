def funcao(saudacao: str = 'Ola mundo') -> str:
    """
    Essa funcao recebe 'str' e retorna 'str'

    Args:
        saudacao (str): A saudacao que o usuario insere.

    Returns:
        saudacao_upper (str): A saudacao que o usuario insere maiuscula.
    """
    saudacao_upper: str = saudacao.upper
    return saudacao_upper
from projeto_01.main import funcao


def test_saudacao_deve_retornar_ola_tdd():
    input = "ola TDD"
    output_esperado = "OLA TDD"
    output: str = funcao(input)
    assert output == output_esperado

def test_saudacao_deve_nao_deve_retornar_algo():
    input = "ola TDD"
    output_esperado = "isso e coisa de dev"
    output: str = funcao(input)
    assert output != output_esperado

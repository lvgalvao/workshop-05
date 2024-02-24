from projeto_01.main import funcao


def test_saudacao_deve_retornar_ola_tdd():
    gabarito = "ola TDD"
    resultado: str = funcao(gabarito)
    assert resultado == gabarito

def test_saudacao_deve_nao_deve_retornar_algo():
    gabarito_2 = "ola TDD"
    resultado: str = funcao(gabarito_2)
    assert resultado != "isso e coisa de dev"

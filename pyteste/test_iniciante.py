import pytest


# Função para testar
def soma(a, b):
    return a + b


def test_soma():
    assert soma(1, 2) == 3


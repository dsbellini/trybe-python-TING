import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Criei a fila de prioridade
    queue = PriorityQueue()

    # Adicionei 2 elementos
    queue.enqueue({"qtd_linhas": 8})
    queue.enqueue({"qtd_linhas": 2})

    # Verifiquei se a fila tem 2 elementos
    assert len(queue) == 2
    # Verifiquei se o primeiro elemento [0] é o de maior prioridade
    assert queue.search(0) == {"qtd_linhas": 2}
    assert queue.search(1) == {"qtd_linhas": 8}

    # Removi o elemento menor e verifiquei se a fila tem 1 elemento
    assert queue.dequeue() == {"qtd_linhas": 2}
    assert len(queue) == 1

    # Verifiquei se o erro é lançado ao tentar acessar um índice inválido
    with pytest.raises(IndexError):
        queue.search(1)

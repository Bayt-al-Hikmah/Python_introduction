from solution import accept_solution,solver # type: ignore
import pytest
def test_negative_detla():
    assert accept_solution(11,1,1) == False
    assert accept_solution(10,0,1) == False
def test_noequation():
    assert accept_solution(0,0,0) == False
    assert accept_solution(0,0,5) == False
    assert accept_solution(0,0,1) == False
def try_acceptsolution():
    assert accept_solution(2,4,2) == True
    assert accept_solution(-5,9,2) == True
    assert accept_solution(0,4,3) == True 
def test_solver():
    assert solver(0,4,3,accept_solution) == -3 / 4
    assert solver(2,4,2,accept_solution) == -1

def test_accept_solution_error():
    with pytest.raises(TypeError):
        accept_solution(2,"4",2)
def test_solver_error():
    with pytest.raises(TypeError):
        solver(2,"4",2,True)
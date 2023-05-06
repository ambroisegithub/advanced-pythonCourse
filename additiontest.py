import addition
# import pytest
def test_add():
    assert addition.add(4, 5) ==9
    
def test_sub():
        assert addition.sub(4, 5) == -1
        
#to test this write below commands
# python3 -m pytest additiontest.py 
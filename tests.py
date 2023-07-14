import pytest
import importlib
import sys
import io
import builtins

@pytest.mark.parametrize("original_sentence,encrypted_sentence",
                        [['python is fun!', 'The encrypted sentence is: udymts nx kzs!'],
                        ['aaa', 'The encrypted sentence is: fff'],
                        ['xyz', 'The encrypted sentence is: cde'],
                        ['A sentence with Capital letters.', 'The encrypted sentence is: f xjsyjshj bnym hfunyfq qjyyjwx.'],
                        ['#$%^&*()', 'The encrypted sentence is: #$%^&*()']
                        ])
def test_cipher(original_sentence, encrypted_sentence, monkeypatch):
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        inputs = iter([original_sentence])
        m.setattr(builtins, "input", lambda _: next(inputs))
        m.setattr(sys, "stdout", mocked_stdout)
        sys.modules.pop("cipher", None)
        importlib.import_module(name="cipher", package="files")
    
    assert mocked_stdout.getvalue().strip() == encrypted_sentence
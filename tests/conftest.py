import pytest
from tkinter import Tk, TclError
from calculator import Buttons


@pytest.fixture
def root():
    root = None
    while root is None:
        try:
            root = Tk()
            root.title('Testing Calc')
            return root
        except TclError:
            continue


@pytest.fixture
def buttons(root):
    return Buttons(root)


@pytest.fixture
def app(root, buttons):
    buttons.describe_interface()
    return root

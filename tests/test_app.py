from tkinter import Tk


def test_app(app):
    assert isinstance(app, Tk)


def test_entry(root, buttons):
    buttons.button_2.invoke()
    buttons.button_0.invoke()
    buttons.button_2.invoke()
    buttons.button_3.invoke()

    entry = buttons.entry_box.get()

    assert entry == '2023'


def test_float_type(root, buttons):
    buttons.button_3.invoke()
    buttons.button_comma.invoke()
    buttons.button_1.invoke()
    buttons.button_4.invoke()

    # 3.14
    entry = buttons.entry_box.get()

    assert float(entry) == 3.14


def test_backspace(root, buttons):
    buttons.button_2.invoke()
    buttons.button_0.invoke()
    buttons.button_2.invoke()
    buttons.button_3.invoke()

    entry = buttons.entry_box.get()
    assert entry == '2023'

    buttons.button_backspace.invoke()

    entry = buttons.entry_box.get()
    assert entry == '202'


def test_clear_entry(root, buttons):
    buttons.button_2.invoke()
    buttons.button_0.invoke()
    buttons.button_2.invoke()
    buttons.button_3.invoke()

    entry = buttons.entry_box.get()
    assert entry == '2023'

    buttons.button_clear.invoke()
    entry = buttons.entry_box.get()
    assert entry == '0'



def test_adding(root, buttons):
    buttons.button_3.invoke()
    buttons.button_add.invoke()
    buttons.button_8.invoke()
    buttons.button_equal.invoke()

    # op: 3 + 8
    result = buttons.entry_box.get()

    assert result == '11'


def test_subtraction(root, buttons):
    buttons.button_1.invoke()
    buttons.button_1.invoke()
    buttons.button_subtract.invoke()
    buttons.button_5.invoke()
    buttons.button_equal.invoke()

    # op: 11 - 5
    result = buttons.entry_box.get()

    assert result == '6'


def test_multiplication(root, buttons):
    buttons.button_7.invoke()
    buttons.button_multiply.invoke()
    buttons.button_8.invoke()
    buttons.button_equal.invoke()

    # op: 7 * 8
    result = buttons.entry_box.get()

    assert result == '56'


def test_division(root, buttons):
    buttons.button_9.invoke()
    buttons.button_divide.invoke()
    buttons.button_3.invoke()
    buttons.button_equal.invoke()

    # op: 9 / 3
    result = buttons.entry_box.get()

    assert result == '3'


def test_division_by_zero(root, buttons):
    buttons.button_9.invoke()
    buttons.button_divide.invoke()
    buttons.button_0.invoke()
    buttons.button_equal.invoke()

    # op: 9 / 0
    result = buttons.entry_box.get()

    assert ZeroDivisionError
    assert 'Cannot divide by zero!' in result


def test_opposite(root, buttons):
    buttons.button_5.invoke()
    buttons.button_opposite.invoke()

    # -5
    result = buttons.entry_box.get()
    assert result == '-5'


def test_inverse(root, buttons):
    buttons.button_5.invoke()
    buttons.button_inverse.invoke()

    # 1/5 = 0.2
    result = buttons.entry_box.get()
    assert float(result) == 0.2


def test_percent(root, buttons):
    buttons.button_5.invoke()
    buttons.button_percent.invoke()

    # 5% = 0.05
    result = buttons.entry_box.get()
    assert float(result) == 0.05


def test_percent_with_multiplication(root, buttons):
    buttons.button_8.invoke()
    buttons.button_multiply.invoke()
    buttons.button_2.invoke()
    buttons.button_5.invoke()
    buttons.button_percent.invoke()
    buttons.button_equal.invoke()

    # 8 * 25% = 2
    result = buttons.entry_box.get()
    assert float(result) == 2


def test_sqr(root, buttons):
    buttons.button_8.invoke()
    buttons.button_sqr.invoke()

    # sqr(8) = 64
    result = buttons.entry_box.get()
    assert float(result) == 64


def test_sqrt(root, buttons):
    buttons.button_3.invoke()
    buttons.button_6.invoke()
    buttons.button_sqrt.invoke()

    # sqrt(36) = 6
    result = buttons.entry_box.get()
    assert float(result) == 6

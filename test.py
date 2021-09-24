import pytest


def test_positive_big_list():
    user_names = ["Anya", "Vova", "Ilya", "Alex"]
    assert user_names[1] == "Vova"
    assert len(user_names) == 4


def test_positive_empty_list():
    user_names = []
    assert len(user_names) == 0


def test_negative_list_index_error():
    user_names = []
    try:
        assert user_names[0]
    except IndexError:
        pass


def test_positive_single_tuple():
    tpl_test = ('s',)
    assert tpl_test == ('s',)
    assert len(tpl_test) == 1


def test_negative_single_tuple():
    tpl_test = ('s',)
    assert tpl_test != 's'


def test_positive_big_tuple():
    tpl_test = tuple("Test!")
    assert (tpl_test[0]) == "T"
    assert (tpl_test[1]) == "e"
    assert (tpl_test[2]) == "s"
    assert (tpl_test[3]) == "t"
    assert (tpl_test[4]) == "!"
    assert tpl_test == ('T', 'e', 's', 't', '!')
    assert len(tpl_test) == 5


def test_negative_error_tuple():
    tpl_test = ('s',)
    try:
        assert tpl_test[1]
    except IndexError:
        pass


@pytest.mark.parametrize("divided_by_three", [-300, -3, 0, 3, 6, 600])
def test_param_positive_list(divided_by_three):
    assert divided_by_three % 3 == 0


@pytest.mark.parametrize("not_divided_by_three", [-299, -1, 1, 5, 235])
def test_param_negative_list(not_divided_by_three):
    assert not_divided_by_three % 3 != 0


@pytest.mark.parametrize("not_divided_by_three_char", ["1", "one", " "])
def test_param_negative_error_list(not_divided_by_three_char):
    try:
        assert not_divided_by_three_char
    except TypeError:
        pass

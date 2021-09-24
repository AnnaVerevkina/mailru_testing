
def test_positive_list():
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

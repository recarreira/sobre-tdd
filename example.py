def test_division_should_return_2_for_entries_4_and_2():
    assert 2 == division(4, 2)


def test_division_should_return_None_for_division_by_0():
	assert None == division(4, 0)


def division(a, b):
	try:
		return a/b
	except ZeroDivisionError, e:
		return None
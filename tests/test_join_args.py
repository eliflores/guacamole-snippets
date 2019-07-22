def test_join_strings():
    args = ('avocados', 'are', 'delicious', '')
    joined_args = ' '.join(args)
    assert joined_args == 'avocados are delicious'

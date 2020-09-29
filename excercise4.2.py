def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    keyword_kwargs_count = len(kwargs)
    print(f"I have received {positional_args_count} positional arguments")
    print(f"I have received {keyword_kwargs_count} keyword arguments")

count_them_all(1, 2, 3, shop ="A")
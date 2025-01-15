def unlimited_arguments(*args, **kargs):
    print(kargs)
    for k, argument in kargs.items():
        print(k, argument)

unlimited_arguments(1,2,3, name='Max', age=29)
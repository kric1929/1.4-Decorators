from datetime import datetime


def parameterized_logger(path):
    def logger(foo):
        def new_foo(*args, **kwargs):
            result = foo(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{str(datetime.now())}\n')
                f.write(f'{foo.__name__}\n')
                f.write(f'{str(args)},{str(kwargs)}\n')
                f.write(f'{str(result)}\n')
                f.write('\n')
            return result
        return new_foo
    return logger

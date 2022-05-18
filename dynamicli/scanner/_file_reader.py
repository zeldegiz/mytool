import time

def read_generator(path,url,delay):
        with open(f'./{path}') as file:
            for line in file:
                yield f'{url}{line[:-1]}'
                time.sleep(delay)
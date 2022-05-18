def except_handler(func):
            def wrapper(*args,**kwargs):
                try : return func(*args,**kwargs)
                except : return False
            return wrapper
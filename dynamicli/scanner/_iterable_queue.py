'''
This class inherite Queue object. But same time this is iterable, can convert bool value, so you can use if blocks directly
and has length parameter
'''
from queue import Queue
class IterableQueue(Queue):
    def __init__(self, *args, **kwargs):
        self.length = 0
        super().__init__(*args,**kwargs)
            
    def get(self):
        self.length -= 1
        return super().get()
            
    def put(self,element):
        self.length += 1
        super().put(element)
        
    def __len__(self):
        return self.length
        
    def __bool__(self):
        return self.length>0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            if(not self.empty()):
                return self.get()
            else:
                raise StopIteration
        except ValueError:
            raise StopIteration
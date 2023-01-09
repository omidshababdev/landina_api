from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    file = open(path, mode)
    yield file
    file.close()
    
with filestream("file.txt", "w") as file:
    file.write("Hello File")
    
print(file.closed)
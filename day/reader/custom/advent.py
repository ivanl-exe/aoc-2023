from day.reader import Reader

class AdventReader(Reader):
    def __init__(self,  filepath: str) -> None:
        super().__init__(filepath, AdventReader.__parser__)
    
    def __parser__(raw_data: str) -> list:
        data = raw_data.split('\n')
        return data
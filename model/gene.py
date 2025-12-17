from dataclasses import dataclass
@dataclass
class Gene:
    id:str
    cromosoma:int

    def __repr__(self):
        return f'{self.id} ({self.cromosoma})'
    def __hash__(self):
        return hash(self.id)+hash(self.cromosoma)
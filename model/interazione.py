from dataclasses import dataclass
@dataclass
class Interazione:
    coppia:tuple
    correlazione:float

    def __repr__(self):
        return f'Interazione: {self.coppia}, {self.correlazione}'
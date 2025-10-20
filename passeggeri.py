class Passeggero:
    def __init__(self, codice_passeggero ,nome_passeggero, cognome_passeggero):
        self._codice_passeggero = codice_passeggero
        self._nome_passeggero = nome_passeggero
        self._cognome_passeggero = cognome_passeggero

    def __str__(self):
        return f"Codice passeggero: {self._codice_passeggero} - Nome: {self._nome_passeggero} - Cognome: {self._cognome_passeggero}"

    def __eq__(self, other):
        if isinstance(other, Passeggero):
            return self._codice_passeggero == other._codice_passeggero


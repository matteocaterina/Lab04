class Cabina:
    def __init__(self, codice_cabina, num_letti, ponte, prezzo):
        self._codice_cabina = codice_cabina
        self._num_letti = num_letti
        self._ponte = ponte
        self._prezzo = float(prezzo)
        self._disponibile = 'Disponibile'

    def __str__(self):
        return f"{self._codice_cabina} Standard | {self._num_letti} letti - Ponte {self._ponte} - Prezzo {self._prezzo} - {self._disponibile}"

    def __eq__(self, other):
        if isinstance(other, Cabina):
            return self._codice_cabina == other._codice_cabina
        return False

class Animali(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo, numero_animali):
        super().__init__(codice_cabina, num_letti, ponte, prezzo)
        self._max_animali = int(numero_animali)
        self._disponibile = 'Disponibile'

    def assegna_prezzo_animali(self):
        self._prezzo = self._prezzo * (1 + 0.1 * self._max_animali)


    def __str__(self):
        return f"{self._codice_cabina} Animali | {self._num_letti} letti - Ponte {self._ponte} - Prezzo {self._prezzo} -  Max Animali {self._max_animali} - {self._disponibile}"

class Deluxe(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo, stringa_tipologia):
        super().__init__(codice_cabina, num_letti, ponte, prezzo)
        self._val_agg = stringa_tipologia
        #self._prezzo = float(prezzo) * 1.20
        self._disponibile = 'Disponibile'

    def assegna_prezzo_deluxe(self):
        self._prezzo = self._prezzo * 1.20


    def __str__(self):
        return f"{self._codice_cabina} Deluxe | {self._num_letti} letti - Ponte {self._ponte} - Prezzo {self._prezzo} - Tipologia {self._val_agg} - {self._disponibile}"








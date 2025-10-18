import csv
from cabina import Cabina
from cabina import Animali
from cabina import Deluxe
from passeggeri import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self._info_passeggeri = []
        self._cabina_standard = []
        self._cabina_animali = []
        self._cabina_deluxe = []
        self._cabine = []
        self._passeggeri = []
        self._comb = []
        
    """Aggiungere setter e getter se necessari"""

    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, set_nome):
        if set_nome == "":
            raise ValueError("Il nome non puo essere vuoto!")
        self._nome = set_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            infile = open(file_path, 'r', encoding='utf-8')
            righe = csv.reader(infile)
            for riga in righe:
                if len(riga) == 3:
                    #passeggeri
                    self._info_passeggeri.append(Passeggero(riga[0], riga[1], riga[2]))
                if len(riga) == 4:
                    self._cabina_standard.append(Cabina(riga[0], riga[1], riga[2], riga[3]))
                if len(riga) == 5:
                    try:
                        val = int(riga[4])
                        self._cabina_animali.append(Animali(riga[0], riga[1], riga[2], riga[3], val))
                    except ValueError:
                        val = str(riga[4])
                        self._cabina_deluxe.append(Deluxe(riga[0], riga[1], riga[2], riga[3], val))

            infile.close()

        except FileNotFoundError:
            raise FileNotFoundError('File non trovato')

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        #La classe Crociera deve prevedere inoltre un metodo per l’assegnazione di un
        # passeggero a una cabina, chiamato assegna_passeggero_a_cabina(codice_cabina, codice_passeggero).
        # Quando viene effettuata una prenotazione, il sistema deve verificare
        # che la cabina e il passeggero esistano, che la cabina sia effettivamente
        # disponibile e che il passeggero non sia già associato a un’altra cabina.
        # Se tutte le condizioni sono soddisfatte, la cabina viene contrassegnata
        # come non disponibile e viene registrata l’associazione tra passeggero e cabina.
        # Se una delle verifiche non va a buon fine, il metodo deve sollevare un’eccezione
        # per segnalare l’errore.

        cabina_disponibile = False
        passeggero_disponibile = False

        for cabina in self._cabina_animali:
            if cabina._codice_cabina == codice_cabina and codice_cabina not in self._cabine:
                self._cabine.append(codice_cabina)
                cabina_disponibile = True
                cabina._disponibile = 'Non disponibile'

                break

        for cabina in self._cabina_deluxe:
            if cabina._codice_cabina == codice_cabina and codice_cabina not in self._cabine:
                self._cabine.append(codice_cabina)
                cabina_disponibile = True
                cabina._disponibile = 'Non disponibile'

                break

        for cabina in self._cabina_standard:
            if cabina._codice_cabina == codice_cabina and codice_cabina not in self._cabine:
                self._cabine.append(codice_cabina)
                cabina_disponibile = True
                cabina._disponibile = 'Non disponibile'

                break

        for passeggero in self._info_passeggeri:
            if passeggero._codice_passeggero == codice_passeggero and codice_passeggero not in self._passeggeri:
                self._passeggeri.append(codice_passeggero)
                passeggero_disponibile = True

                break

        if cabina_disponibile == True and passeggero_disponibile == True:
            self._comb.append((codice_cabina, codice_passeggero))
            print(f'{codice_cabina} - {codice_passeggero}')
            return True

        if cabina_disponibile == False and passeggero_disponibile == False:
            raise Exception('cabina falsa passeggero falso')

        if cabina_disponibile == True and passeggero_disponibile == False:
            raise Exception('cabina vero passeggero falso')

        if cabina_disponibile == False and passeggero_disponibile == True:
            raise Exception('cabina falso passeggero vero')


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        cabine_tot = []
        for cabina in self._cabina_standard:
            cabine_tot.append(cabina)
        for cabina in self._cabina_animali:
            cabine_tot.append(cabina)
        for cabina in self._cabina_deluxe:
            cabine_tot.append(cabina)

        lista_ordinata = sorted(cabine_tot, key = lambda cabina: cabina._prezzo)

        return lista_ordinata



    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

        for p in self._info_passeggeri:
            cabina = 'nessuna cabina assegnata'
            for codice_cabina, codice_passeggero in self._comb:
                if codice_passeggero == p._codice_passeggero:
                    cabina = codice_cabina
                    break
            print(p._codice_passeggero, p._nome_passeggero, p._cognome_passeggero, cabina)















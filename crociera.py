import csv
from cabina import Cabina
from cabina import Animali
from cabina import Deluxe
from passeggeri import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome               #nome della crociera
        self._info_passeggeri = []      #informazioni sui passeggeri
        self._cabina_standard = []      #informazioni sulle cabine standard
        self._cabina_animali = []       #informazioni sulle cabine con animali
        self._cabina_deluxe = []        #informazioni sulle cabine deluxe
        self._cabine = []               #lista con i codici delle cabine assegnate
        self._passeggeri = []           #lista con i codici dei passeggeri assegnati
        self._comb = []                 #lista con la combinazione di (codice_cabina, codice_passeggero)
        
    """Aggiungere setter e getter se necessari"""

    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, set_nome):
        if set_nome == "":
            raise ValueError("IL CAMPO DEL NOME NON PUO' ESSERE VUOTO")
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

                        animali = Animali(riga[0], riga[1], riga[2], float(riga[3]), val)

                        animali.assegna_prezzo_animali()

                        self._cabina_animali.append(animali)

                    except ValueError:
                        val = str(riga[4])
                        deluxe = Deluxe(riga[0], riga[1], riga[2], float(riga[3]), val)

                        deluxe.assegna_prezzo_deluxe()

                        self._cabina_deluxe.append(deluxe)

            infile.close()

        except FileNotFoundError:
            raise FileNotFoundError('FILE NON TROVATO')

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

        cabina_assegnata = False
        passeggero_assegnato= False

        for cabina in self._cabina_animali:
            if cabina._codice_cabina == codice_cabina and codice_cabina not in self._cabine:
                self._cabine.append(codice_cabina)
                cabina_assegnata = True
                cabina._disponibile = 'Non disponibile'

                break

        for cabina in self._cabina_deluxe:
            if cabina._codice_cabina == codice_cabina and codice_cabina not in self._cabine:
                self._cabine.append(codice_cabina)
                cabina_assegnata = True
                cabina._disponibile = 'Non disponibile'

                break

        for cabina in self._cabina_standard:
            if cabina._codice_cabina == codice_cabina and codice_cabina not in self._cabine:
                self._cabine.append(codice_cabina)
                cabina_assegnata = True
                cabina._disponibile = 'Non disponibile'

                break

        for passeggero in self._info_passeggeri:
            if passeggero._codice_passeggero == codice_passeggero and codice_passeggero not in self._passeggeri:
                self._passeggeri.append(codice_passeggero)
                passeggero_assegnato = True

                break

        if cabina_assegnata == True and passeggero_assegnato == True:
            self._comb.append((codice_cabina, codice_passeggero))
            print(f'{codice_cabina} - {codice_passeggero}')
            return True

        if cabina_assegnata == False and passeggero_assegnato == False:
            raise Exception('ASSEGNAZIONE NON DISPONIBILE: \n'
                            '----------------------------------------------- \n '
                            '- CABINA GIA ASSEGNATA OPPURE NON ESISTENTE \n '
                            '- PASSEGGERO GIA ASSEGNATO OPPURE NON ESISTENTE')


        if cabina_assegnata == True and passeggero_assegnato == False:
            self._cabine.remove(codice_cabina)
            raise Exception('ASSEGNAZIONE NON DISPONIBILE: \n'
                            '----------------------------------------------- \n'
                            '- CABINA DISPONIBILE \n'
                            '- PASSEGGERO GIA ASSEGNATO OPPURE NON ESISTENTE')

        if cabina_assegnata == False and passeggero_assegnato == True:
            self._passeggeri.remove(codice_passeggero)
            raise Exception('ASSEGNAZIONE NON DISPONIBILE: \n'
                            '----------------------------------------------- \n'
                            '- CABINA GIA ASSEGNATA OPPURE NON ESISTENTE \n'
                            '- PASSEGGERO DISPONIBILE')


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
            print(f'Codice passeggero: {p._codice_passeggero} - Nome: {p._nome_passeggero} - Cognome: {p._cognome_passeggero} - Cabina: {cabina}')















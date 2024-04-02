class Appuntamento:
    def __init__(self, data, ora, tipo_di_servizio, cliente):
        # Inizializzazione della classe Appuntamento con data, ora, tipo di servizio e cliente associato
        self.data = data  # Data dell'appuntamento
        self.ora = ora  # Ora dell'appuntamento
        self.tipo_di_servizio = tipo_di_servizio  # Tipo di servizio richiesto
        self.cliente = cliente  # Cliente associato all'appuntamento
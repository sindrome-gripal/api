import requests


class ElasticHttpSearch:
    """
    OPENDATASUS

    Notificações de Síndrome Gripal - API ElasticSearch
    https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch
    
    """
    
    def __init__(self) -> None:
        self.__ELASTIC_PWD = "Za4qNXdyQNSa9YaA"
        self.__ELASTIC_USER = "user-public-notificacoes"
        self.__HOST = 'https://' + self.__ELASTIC_USER + ':' + self.__ELASTIC_PWD + '@elasticsearch-saps.saude.gov.br:443'


    def req(self, uf: str, municipio=None):

        full_url = self.__HOST + self.__search_path(uf, municipio)
        resp = requests.get(url=full_url)
        return resp.json(), resp.status_code


    def __search_path(self, uf: str, municipio=None):
        """
        
        Parameters:
        ----------
        uf : str
            Unidade da Federação. Sigla do estado
        
        municipio : str
            Nome do município. (População acima de 300 mil habitantes)

        """
        if uf in self.uf_list():
            if municipio:
                return f'/desc-esus-notifica-municipio-{uf.lower()}-{municipio.lower()}/_search?pretty'

            return f'/desc-esus-notifica-estado-{uf.lower()}/_search?pretty'
        
        return 'UF inválida. Verifique uf_list().'


    def uf_list(self):
        return [
            'ac', 'al', 'am',
            'ap', 'ba', 'ce',
            'df', 'es', 'go',
            'ma', 'mg', 'ms',
            'mt', 'pa', 'pb',
            'pe', 'pi', 'pr',
            'rj', 'rn', 'ro',
            'rr', 'rs', 'sc',
            'se', 'sp', 'to',
        ]

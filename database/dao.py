from database.DB_connect import DBConnect
from model.gene import Gene
from model.interazione import Interazione

class DAO:

    @staticmethod
    def get_gene():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione al database")
            return None
        result = []

        cursor = cnx.cursor(dictionary=True)
        query = """ select id,cromosoma
                    from gene
                    where cromosoma !=0
                    group by id"""

        cursor.execute(query)

        for row in cursor:
            gene=Gene(id=row['id'],
                      cromosoma=row['cromosoma'])
            result.append(gene)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_interazione():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione al database")
            return None
        result = []

        cursor = cnx.cursor(dictionary=True)
        query = """select id_gene1 , id_gene2 , correlazione 
                    from interazione
                    WHERE id_gene1
                    group by id_gene1 , id_gene2 """

        cursor.execute(query)

        for row in cursor:
            coppiaT=[row['id_gene1'],row['id_gene2']]
            interazione=Interazione(coppia=coppiaT,
                                    correlazione=row['correlazione'])
            result.append(interazione)

        cursor.close()
        cnx.close()
        return result


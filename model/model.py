import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G=nx.DiGraph()
        self.listgene=[]
        self.listinterazione=[]
        self.dizInterazioni={}
        self.pesi = []
        self.S=None
        self.best_path=[]
        self.best_cost=0.0

    def crea_grafo(self):
        self.G.clear()
        self.listGene=DAO.get_gene()
        self.listInterazione=DAO.get_interazione()

        for interazione in self.listInterazione:
            cromosoma1=0
            cromosoma2=0
            coppiaC=set()

            gene_1=interazione.coppia[0]
            for gene in self.listGene:
                if gene.id == gene_1:
                    cromosoma1= gene.cromosoma

            gene_2=interazione.coppia[1]
            for gene in self.listGene:
                if gene.id == gene_2:
                    cromosoma2= gene.cromosoma

            coppiaC=(cromosoma1, cromosoma2)

            if coppiaC not in self.dizInterazioni:
                self.dizInterazioni[coppiaC]=interazione.correlazione
            else:
                self.dizInterazioni[coppiaC]+=interazione.correlazione
        print(self.dizInterazioni)

            #creazione grafo
        for chiave in self.dizInterazioni:
            self.G.add_edge(chiave[0], chiave[1],weight=self.dizInterazioni[chiave])

        print(self.G)
        return self.G
    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        for n1,n2,weight in self.G.edges(data=True):
            self.pesi.append(weight["weight"])
        return  min(self.pesi),max(self.pesi)

    def count_edges_by_threshold(self, soglia):
        minori=0
        maggiori=0
        for pesi in self.pesi:
            if pesi < soglia:
                minori+=1
            elif pesi > soglia:
                maggiori+=1
        return minori, maggiori

    def ricerca_cammino(self):
        print("parto")
        if self.G is None:
            raise ValueError("grafo ancora da creare")
        self.best_path=[]
        self.best_cost=0.0

        vertici=list(self.G.nodes())

        #avvio ricercerca ricorsiva
        for i in range(len(self.G.nodes)):
            start=vertici[i]
            self.ricorsione(start,[start],0.0)



    def ricorsione(self,start_vertex,cammino_parziale,costo_corrente:float):
        if costo_corrente>self.best_cost:
            self.best_cost=costo_corrente
            self.best_path=cammino_parziale.copy()

        ultimo=cammino_parziale[-1]

        for v in self.G.neighbors(ultimo):
            if v in cammino_parziale:
                continue
            peso=self.G[ultimo][v]["weight"]

           # if peso<=self.S:
                #continue

            nuovo_costo=costo_corrente+float(peso)
            cammino_parziale.append(v)

            self.ricorsione(v,cammino_parziale,nuovo_costo)
            cammino_parziale.pop()

    def get_cammino_massimo(self):
        print(self.best_path,self.best_cost)
        return self.best_path,self.best_cost



















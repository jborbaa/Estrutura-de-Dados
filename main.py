import re
from listaduplamente import ListaDuplamente
from listasimplesmente import ListaSimplesmente


class main:
    def printList(list: ListaSimplesmente):
        if list.size == 0:
            return False
        list.primeiro_Node()

        while list.iterator:
            print(f'[{list.iterator.data}, {list.iterator.listaDE}]')
            list.proxNode()

    def printListData(list: ListaSimplesmente):
        if list.size == 0:
            return False

        list.primeiro_Node()

        while list.iterator:
            print(list.iterator.data)
            list.proxNode()

    def printListListaDE(list: ListaSimplesmente):
        if list.size == 0:
            return False

        list.primeiro_Node()

        while list.iterator:
            print(list.iterator.listaDE)
            list.proxNode()

    def getEstradas():

        estradasList = ListaSimplesmente()
        cidadesList = ListaDuplamente()

        entrada = open("entrada.txt")

        lines = entrada.readlines()
        estradasList.primeiro_Node()
        cidadesList.primeiro_Node()

        for line in lines:
            estradas = re.findall(r"[A-Z]{2}-\d{3}", line)
            cidades = re.findall(r'"([^"]+)"', line)

            for cidade in cidades:
                cidadesList.addNode(cidade)

            estradasList.addNode(estradas[0], cidades)
        return estradasList

    def cidadeEstradas(cidadeNome: str, estradasList: ListaSimplesmente):

        estradas = ListaSimplesmente
        estradasList.primeiro_Node()

        while estradasList.iterator:

            for cidade in estradasList.iterator.listaDE:
                if cidade == cidadeNome:
                    estradas.addNode(estradasList.iterator.data, None)
            estradasList.nextNode()

        return estradas

    if __name__ == "__main__":

        estradas = getEstradas()

        resultado = cityEstradas("Joinville", estradas)

        printListData(resultado)

import re

from listaduplaencad import ListaDuplaEncadeada

from listasimplesencad import ListaSimplesEncadeada



class main:

    def printListaDE(list: ListaSimplesEncadeada):
        if list.size == 0:
            return False

        list.first_No()

        while list.iterator:
            print(list.iterator.listaDE)
            list.nextNo()


    def printLista(list: ListaSimplesEncadeada):
        if list.size == 0:
            return False

        list.first_No()

        while list.iterator:
            print(f'[{list.iterator.data}, {list.iterator.listaDE}]')
            list.nextNo()


    def printListaData(list: ListaSimplesEncadeada):
        if list.size == 0:
            return False

        list.first_No()

        while list.iterator:
            print(list.iterator.data)
            list.nextNo()


    def estadoRodovias(cidadeName: str, rodoviasList: ListaSimplesEncadeada):

        rodovias = ListaSimplesEncadeada()
        rodoviasList.first_No()

        while rodoviasList.iterator:

            for cidade in rodoviasList.iterator.listaDE:
                if cidade == cidadeName:
                    rodovias.addNo(rodoviasList.iterator.data, None)
            rodoviasList.nextNo()
    
        return rodovias


    def getRodovias():

        rodoviasList = ListaSimplesEncadeada()
        cidadesList = ListaDuplaEncadeada()

        entrada = open("entrada.txt")
        lines = entrada.readlines()

        rodoviasList.first_No()
        cidadesList.first_No()



        for line in lines:
            rodovia = re.findall(r"[A-Z]{2}-\d{3}", line)

            cidades = re.findall(r'"([^"]+)"', line)

            for cidade in cidades:
                cidadesList.addNo(cidade)

            rodoviasList.addNo(rodovia[0], cidades)
        return rodoviasList



    if __name__ == "__main__":
        rodovias = getRodovias()
        resultado = estadoRodovias("Maravilha", rodovias)
        printListaData(resultado)

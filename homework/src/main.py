import argparse


class ArgumentParser:
    def __init__(self):

        self.input=None
        self.output = None
        self.parser= None
        self.crear_parser()

    def crear_parser(self):
        
        self.parser = argparse.ArgumentParser(description="Count words in files.")
        self.parser.add_argument(
            "input",
            type=str,
            help="Path to the input folder containing files to process",
        )
        self.parser.add_argument(
            "output",
            type=str,
            help="Path to the output folder for results",
        )

    def run(self):
        

        parsed_args = self.parser.parse_args()
        self.input=parsed_args.input
        self.output=parsed_args.output

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    def print(self):
        print("El nombre es",self.nombre," ",self.apellido)




def main():
    #argument_parser=ArgumentParser()
    #argument_parser.run()
    #print(argument_parser.input)
    #print(argument_parser.output)

    pepita=Persona("Pepita","Rojas")
    marcos=Persona("Marcos","Puetas")

    pepita.print()
    marcos.print()
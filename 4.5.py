#brak Polskich znaków w stringach bo gitbash wywala unicode error  
import logging
import math
logging.basicConfig(level=logging.DEBUG)
def value_check(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def calc(*args):
    if args[0]==1:
        arguments="Dodaję:"
        for i in range(len(args[1])):
            arg=args[1]
            arguments+=f" {arg[i]}"
            if i < len(args[1])-1:
                arguments+=f" do "
        logging.info(arguments)
        print(f"Wynik dodawania to: {sum(args[1])}")
    elif args[0]==2:
        logging.info(f"Od {args[1]} odejmuje {args[2]}")
        print(f"Wynik odejmowania to: {args[1]-args[2]}")
    elif args[0]==3:
        arguments="Mnożę:"
        for i in range(len(args[1])):
            arg=args[1]
            arguments+=f" {arg[i]}"
            if i < len(args[1])-1:
                arguments+=f" przez "
        logging.info(arguments)
        print(f"Wynik mnozenia to:{math.prod(args[1])}")
    elif args[0]==4:
        logging.info(f"Dziele {args[1]} przez {args[2]}")
        print(f"Wynik dzielenia to: {args[1]/args[2]}")

if __name__=="__main__":
    method=input("Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie:")
    while value_check(method) == False or value_check(method) == True and float(method) not in [1.0,2.0,3.0,4.0]:
        method=input("Niepoprawna wartosc, podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie:")
    if int(method)==2 or int(method)==4:
        value_1=input("podaj pierwsza wartosc:")
        while value_check(value_1)==False:
            value_1=input(f"'{value_1}' jest niepoprawna wartoscia, podaj inna wartosc:")
            value_check(value_1)
        value_2=input("podaj druga wartosc:")
        while value_check(value_2)==False:
            value_2=input(f"'{value_2}' jest niepoprawna wartoscia, podaj inna wartosc:")
            value_check(value_2)
        calc(int(method), float(value_1), float(value_2))
    elif int(method)==1 or int(method)==3:
        values_list=input("Podaj wartosci rozdzielone przecinkiem: ")
        value=values_list.split(",")
        for i in range(len(value)):
            while value_check(value[i])==False:
                value[i]=input(f"'{value[i]}' jest niepoprawna wartoscia, podaj nowa wartosc:")
                value_check(value[i])
            value[i]=float(value[i])
        calc(int(method),value)

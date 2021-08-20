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
        logging.info(f"Od {args[1]} odejmuję {args[2]}")
        print(f"Wynik odejmowania to: {args[1]-args[2]}")
    elif args[0]==3:
        arguments="Mnożę:"
        for i in range(len(args[1])):
            arg=args[1]
            arguments+=f" {arg[i]}"
            if i < len(args[1])-1:
                arguments+=f" przez "
        logging.info(arguments)
        print(f"Wynik mnożenia to:{math.prod(args[1])}")
    elif args[0]==4:
        logging.info(f"Dzielę {args[1]} przez {args[2]}")
        print(f"Wynik dzielenia to: {args[1]/args[2]}")

method=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
while value_check(method) == False or value_check(method) == True and float(method) not in [1.0,2.0,3.0,4.0]:
    method=input("Niepoprawna wartość, podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
if int(method)==2 or int(method)==4:
    value_1=input("podaj pierwszą wartość:")
    while value_check(value_1)==False:
        value_1=input(f"'{value_1}' jest niepoprawną wartością, podaj inną wartość:")
        value_check(value_1)
    value_2=input("podaj drugą wartość:")
    while value_check(value_2)==False:
        value_2=input(f"'{value_2}' jest niepoprawną wartoscią, podaj inną wartość:")
        value_check(value_2)
    calc(int(method), float(value_1), float(value_2))
elif int(method)==1 or int(method)==3:
    values_list=input("Podaj wartości rozdzielone przecinkiem: ")
    value=values_list.split(",")
    for i in range(len(value)):
        while value_check(value[i])==False:
            value[i]=input(f"'{value[i]}' jest niepoprawną wartoscią, podaj nową wartość:")
            value_check(value[i])
        value[i]=float(value[i])
    calc(int(method),value)

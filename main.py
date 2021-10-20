def read_list():
    '''
    Citeste lista de intregi
    :return: Returneaza lista de intregi
    '''
    list_str = input("Introduceti lista de itemi: ").split(" ")
    lst = []
    for el in list_str:
        lst.append(el)
    return lst

def show_menu():
    '''
    Printeaza meniul
    :return:
    '''
    print('''
    1.Citeste lista de nr intregi
    2.Afișarea tuturor numerelor negative nenule din listă
    3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    4.Afișarea tuturor numerelor din listă care sunt superprime.
    5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
      CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    x.Iesire
    ''')

def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Comanda: ")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida!")

main()
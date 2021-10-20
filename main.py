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

def is_prime(n):
    """
    Afla daca un numar este prim
    :param n: n nr natural
    :return: Returneaza True daca n este prim, altfel False
    """
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def is_superprime(n):
    """
    Afla daca un numar este superprim
    :param n: n nr natural
    :return: Returneaza True daca n este superprim, altfel False
    """
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def test_is_superprime():
    assert is_superprime(317) == True
    assert is_superprime(214) == False
    assert is_superprime(33) == True

def show_menu():
    test_is_superprime()
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
        cmd = input('Selectati o alta comanda: ')

main()
#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista = []
    for i in range(max(len(my_list_1), len(my_list_2))):
        try:
            lista.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            lista.append(0)
        except IndexError:
            print("out of range")
            lista.append(0)
        except ZeroDivisionError:
            print("division by 0")
            lista.append(0)
        finally:
            print(end="")
    return lista

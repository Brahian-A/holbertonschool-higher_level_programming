#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            resultado = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print('division by 0')
            resultado = 0
        except (ValueError, TypeError):
            print('wrong type')
        except (IndexError):
            print('out of range')
        finally:
            new_list.append(resultado)
    return(new_list)
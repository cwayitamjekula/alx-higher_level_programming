def list_division(my_list_1, my_list_2, list_length):
    list_total = []
    for i in range(list_length):
        try:
            n = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            n = 0
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        finally:
            list_total.append(n)
            return (list_total)

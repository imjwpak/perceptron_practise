from dlearn.iris import IrisModel

if __name__ == '__main__':
    def print_menu():
        print('0. EXIT')
        print('1. IRIS DATA')
        print('2. IRIS SCATTER')
        print('3. IRIS 결정경계')
        return input('CHOOSE ONE : ')

    while 1:
        menu = print_menu()

        if menu == '0':
            print('EXIT')
            break
        elif menu == '1':
            m = IrisModel()
            print('RESULT : ' % m.get_iris())
            break
        elif menu == '2':
            m = IrisModel()
            m.draw_scatter()
            break
        elif menu == '3':
            m = IrisModel()
            m.plot_decision_regions()
            break
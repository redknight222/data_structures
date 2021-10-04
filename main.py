from vector import vector


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myVector = vector()
    myVector.add_element('sensay')
    myVector.add_element('loh')
    myVector.add_element('sam')
    myVector.add_element('privet')
    myVector.debug_print()
    myVector.remove_element()
    myVector.debug_print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

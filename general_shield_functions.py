import random

def choose_element():
    random_integer = random.randint(0,3)
    switcher = {
        0: 'Incendiary',
        1: 'Corrosion',
        2: 'Shock',
        3: 'Explosion'
    }
    return switcher.get(random_integer, 'nothing')

def get_valid_nova_spike_manufacturer_element_combo(manufacturer, element, type):
    generated_element = element #set generated_element to be the same as element for now
    while True:
        if(is_nova_spike_manufacturer_element_combo_valid(manufacturer, generated_element) is True):
            print("Valid %s element/manufacturer combo" % type)
            print("%s %s shield has element %s" % (manufacturer, type, generated_element))
            break
        else:
            print("Invalid %s element/manufacturer combo" % type)
            print("%s %s shield has element %s" % (manufacturer, type, generated_element))
            generated_element = choose_element()

    return generated_element

def is_nova_spike_manufacturer_element_combo_valid(manufacturer, element):
    # Maliwan shields can only be incendiary, corrosion or shock, and
    # Torgue shields can only be

    test_1 = True
    test_2 = True

    if(manufacturer == 'Maliwan'):
        test_1 = (element != 'Explosion')
    elif(manufacturer == 'Torgue'):
        test_2 = (element == 'Explosion')

    return test_1 and test_2
import random

def choose_element():
    elements = ['Incendiary', 'Corrosion', 'Shock', 'Explosion']
    return random.choice(elements)

def get_valid_nova_spike_manufacturer_element_combo(manufacturer, element, type):
    generated_element = element #set generated_element to be the same as element for now
    while True:
        if is_nova_spike_manufacturer_element_combo_valid(manufacturer, generated_element) is True:
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
    # Torgue shields can only be explosive

    test = True

    if manufacturer == 'Maliwan':
        test = (element != 'Explosion')
    elif manufacturer == 'Torgue':
        test = (element == 'Explosion')

    return test

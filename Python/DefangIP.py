def defangIPaddr(address):
    address = address.replace('.', '[.]')
    return address

def defangIPaddr2(address):
    newstring = ''
    for i in range(len(address)):
        if address[i] == '.':
            newstring += '[.]'
        else:
            newstring += address[i]
    return newstring

print(defangIPaddr('1.1.1.1'))
print(defangIPaddr2('1.1.1.1'))

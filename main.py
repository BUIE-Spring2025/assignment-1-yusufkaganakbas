def int_to_roman(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    romans = []
    roman_type = ''
    match num // 1000:
        case 0:
            pass
        case 1:
            romans.append('M')
        case 2:
            romans.append('MM')
        case 3:
            romans.append('MMM')

    match (num % 1000) // 100:
        case 0:
            pass
        case 1:
            romans.append('C')
        case 2:
            romans.append('CC')
        case 3:
            romans.append('CCC')
        case 4:
            romans.append('CD')
        case 5:
            romans.append('D')
        case 6:
            romans.append('DC')
        case 7:
            romans.append('DCC')
        case 8:
            romans.append('DCCC')
        case 9:
            romans.append('CM')
    match (num % 100) // 10:
        case 0:
            pass
        case 1:
            romans.append('X')
        case 2:
            romans.append('XX')
        case 3:
            romans.append('XXX')
        case 4:
            romans.append('XL')
        case 5:
            romans.append('L')
        case 6:
            romans.append('LX')
        case 7:
            romans.append('LXX')
        case 8:
            romans.append('LXXX')
        case 9:
            romans.append('XC')
    match num % 10:
        case 0:
            pass
        case 1:
            romans.append('I')
        case 2:
            romans.append('II')
        case 3:
            romans.append('III')
        case 4:
            romans.append('IV')
        case 5:
            romans.append('V')
        case 6:
            romans.append('VI')
        case 7:
            romans.append('VII')
        case 8:
            romans.append('VIII')
        case 9:
            romans.append('IX')
    for item in romans:
        roman_type = roman_type + item
    return roman_type

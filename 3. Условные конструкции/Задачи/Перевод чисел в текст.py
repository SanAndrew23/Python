num = int(input())
x1 = num % 10
x2 = num // 10 % 10
x3 = num // 100

res = ''

match x3:
    case 1:
        res += 'сто '
    case 2:
        res += 'двести '
    case 3:
        res += 'триста '
    case 4:
        res += 'четыреста '
    case 5:
        res += 'пятьсот '
    case 6:
        res += 'шестьсот '
    case 7:
        res += 'семьсот '
    case 8:
        res += 'восемьсот '
    case 9:
        res += 'девятьсот '

match x2:
    case 1:
        match x1:
            case 0:
                res += 'десять '
            case 1:
                res += 'одиннадцать '
            case 2:
                res += 'двенадцать '
            case 3:
                res += 'тринадцать '
            case 4:
                res += 'четырнадцать '
            case 5:
                res += 'пятнадцать '
            case 6:
                res += 'шестнадцать '
            case 7:
                res += 'семнадцать '
            case 8:
                res += 'восемнадцать '
            case 9:
                res += 'девятнадцать '
    case 2:
        res += 'двадцать '
    case 3:
        res += 'тридцать '
    case 4:
        res += 'сорок '
    case 5:
        res += 'пятьдесят '
    case 6:
        res += 'шестьдесят '
    case 7:
        res += 'семьдесят '
    case 8:
        res += 'восемьдесят '
    case 9:
        res += 'девяносто '

if x2 != 1:
    match x1:
        case 1:
            res += 'один '
        case 2:
            res += 'два '
        case 3:
            res += 'три '
        case 4:
            res += 'четыре '
        case 5:
            res += 'пять '
        case 6:
            res += 'шесть '
        case 7:
            res += 'семь '
        case 8:
            res += 'восемь '
        case 9:
            res += 'девять '

print(res)

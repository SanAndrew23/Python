num = int(input())

x1 = num % 10
x2 = num // 10 % 10
x3 = num // 100

match x1:
    case 0:
        strx1 = ''
    case 1:
        strx1 = 'один'
    case 2:
        strx1 = 'два'
    case 3:
        strx1 = 'три'
    case 4:
        strx1 = 'четыре'
    case 5:
        strx1 = 'пять'
    case 6:
        strx1 = 'шесть'
    case 7:
        strx1 = 'семь'
    case 8:
        strx1 = 'восемь'
    case 9:
        strx1 = 'девять'

match x2:
    case 1:
        match x1:
            case 1:
                srtx2 = 'одиннадцать'
            case 2:
                strx2 = 'двенадцать'
            case 3:
                strx2 = 'тринадцать'
            case 4:
                strx2 = 'четырнадцать'
            case 5:
                strx2 = 'пятнадцать'
            case 6:
                strx2 = 'шестнадцать'
            case 7 :
                strx2 = 'семнадцать'
            case 8:
                strx2 = 'восемнадцать'
            case 9:
                strx2 = 'девятнадцать'
    case 2:
        strx2 = 'двадцать'
    case 3:
        strx2 = 'тридцать'
    case 4:
        strx2 = 'сорок'
    case 5:
        strx2 = 'пятьдесят'
    case 6:
        strx2 = 'шестьдесят'
    case 7:
        strx2 = 'семьдесят'
    case 8:
        strx2 = 'восемьдесят'
    case 9:
        strx2 = 'девяносто'
match x3:
    case 1:
        strx3 = 'сто'
    case 2:
        strx3 = 'двести'
    case 3:
        strx3 = 'триста'
    case 4:
        strx3 = 'четыреста'
    case 5:
        strx3 = 'пятьсот'
    case 6:
        strx3 = 'шестьсот'
    case 7:
        strx3 = 'семьсот'
    case 8:
        strx3 = 'восемьсот'
    case 9:
        strx3 = 'девятьсот'

if (strx2 == 'одиннадцать') or (strx2 == 'двенадцать') or (strx2 == 'тринадцать') or (strx2 == 'четырнадцать') or (strx2 == 'пятнадцать') or (strx2 == 'шестнадцать') or (strx2 == 'семнадцать') or (strx2 == 'восемнадцать') or (strx2 == 'девятнадцать'):
    print(f'{strx3} {strx2}')
else:
    print(f'{strx3} {strx2} {strx1}')
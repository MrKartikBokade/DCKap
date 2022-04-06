
def process(num, index):
    words = ""

    unit_place = ('zero', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine')
    teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    tenth_place = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred')
    counter = ('', 'thousand', 'million')

    if num == '0':
        return 'Zero'

    length = len(num)
    if(length > 3):
        return False
    num = num.zfill(3)

    hundredth_digit = int(num[0])
    tenth_digit = int(num[1])
    unit_digit = int(num[2])

    if num[0] == '0':
        words += ''
    else:
        words += unit_place[hundredth_digit]

    if not words == '':
        words += ' hundred '
    else:
        words += ''

    if(tenth_digit > 1):
        words += tenth_place[tenth_digit - 2]
        words += '-'
        words += unit_place[unit_digit]

    elif(tenth_digit == 1):
        words += teens[(int(tenth_digit + unit_digit) % 10) - 1]

    elif(tenth_digit == 0):
        words += unit_place[unit_digit]

    if(words.endswith('zero')):
        words = words[:-4]
    else:
        words += ' '

    if(not len(words) == 0):
        words += counter[index]

    return words


def getWords(num):
    if num == 1000000000:
        return 'one billion dollars'
    length = len(str(num))

    if length > 9:
        return 'This program supports upto 9 digit nums.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length-1, -1, -3):
        words.append(process(str(num)[0 if i - 2 < 0 else i - 2: i + 1], copy - count))
        count -= 1

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    final_words += "dollars"
    return final_words


num = int(input('Enter any number: '))
print(getWords(num))

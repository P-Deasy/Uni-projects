def removeVowels(sentence):
    '''
    Removes vowels from a list
    '''
    vowels = 'aeiou'
    filtered_list = [l for l in sentence if l not in vowels]
    return ''.join(filtered_list)


def hailStone(n):
    '''
    Generates the hailstone
    sequence of a given positive number n 
    and prints the sequence to the screen
    '''
    hail_sequence = []
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        hail_sequence.append(int(n))
    return hail_sequence


hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                    '6': '0110', '7': '0111', '8': '1000 ', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D':
                        '1101', 'E': '1110', 'F': '1111'}


def hexToBinary(hex, d):
    '''
    Changes Hexadecimal value to binary
    '''
    hexlist = [d[i] for i in hex]
    return ''.join(hexlist)


codon_map = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
             'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine',
             'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC':
             'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop'}


def RNA_Transcript(rna):
    '''
    Changes RNA sequence to protein sequence and prints it
    '''
    protein_list = []
    rna_list = [rna[i:i + 3] for i in range(0, len(rna), 3)]
    for i in rna_list:
        if codon_map[i] == 'stop':
            break
        protein_list.append(codon_map[i])
    print(rna_list)
    print(protein_list)


    
# Consider 10 employees, numbered 0
#to 9, with the number of steps taken by each employee recorded over a 5 day week
#with days numbered 0 to 4, in a table having 10 rows and 5 columns. Thus, for
#example, the entry in row 8 and column 3 gives the number of the steps by
#employee number 8 on day number 3.

    
    
def tenkSteps(stepData):
    '''
    The number of week-days on which at least 100,000 steps were made
    cumulatively by all employees.
    '''
    n = 0
    m = 0
    day = 0
    while m <= 4:
        templist = []
        total = 0
        while n <= 9:
            templist.append(stepData[n][m])
            for nm in range(0, len(templist)):
                total = total + templist[nm]
            if total >= 100000:
                day += 1
            n += 1
        m += 1
    return total


def mostSteps(stepData):
    '''
    Number of employee who took the most steps
    '''
    n = 0
    m = 0
    i = 0
    empindex = 0
    empnum = 0
    while m <= 9:
        templist = []
        total = 0
        while n <= 4:
            templist.append(stepData[m][n])
            for nm in range(0, len(templist)):
                total = total + templist[nm]
                emplist.append(total)
            n += 1
        m += 1
    while i < len(emplist):
        if emplist[i] > empnum:
            empnum = emplist[i]
            empindex = i
    return empindex

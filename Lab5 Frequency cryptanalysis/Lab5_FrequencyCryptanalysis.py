from collections import Counter

#def symbolFreq(openTextFile: str, openTextFileEncoding: str, cryptedTextFile: str, cryptedTextFileEncoding: str):
def symbolFreq(file: str, encoding: str) -> list :
    with open(file, 'r', encoding = encoding) as f:
        buf = f.read()
    #print(buf)
    text_freq = Counter(buf)
    #print(text_freq)


    def by_value(item):
        return item[1]

    symList = list()
    for k, v in sorted(text_freq.items(), key = by_value, reverse = True):
        #print(k, '->', v)
        symList.append(k)
    print(symList)
    return symList

openTextFreqList = symbolFreq('open_text.txt', 'UTF-8')
cryptedTextFreqList = symbolFreq('crypted_text.txt', 'UTF-8')
print('Длина алфавита открытого текста', len(openTextFreqList))
print('Длина алфавита зашифрованного текста', len(cryptedTextFreqList))

dictionary = dict()
for i in range(len(cryptedTextFreqList)):
    dictionary[cryptedTextFreqList[i]] = openTextFreqList[i]
print(dictionary)

print(openTextFreqList)
print(cryptedTextFreqList)
with open('crypted_text.txt', 'r', encoding='UTF-8') as f:
    cryptedTextBuf = f.read()
with open('decrypted_text.txt', 'a', encoding='UTF-8') as f:
    for symbol in cryptedTextBuf:
        print(dictionary[symbol], file = f, end='')

def alignText(text: str, keyLen: int) -> list:
    textList = list(text)
    if (len(textList) % keyLen != 0):
        for i in range(keyLen - (len(text) % keyLen)):
            textList.append(' ')
    #print('Aligned text:\n\t', text)
    #print('Aligned textList:\n\t', textList)
    return textList

#textList = alignText(text, len(key))

def splitBlocks(textList: list, keyLen: int) -> list:
    textBlocks = list()
    textLen = len(textList)
    start = 0
    for i in range(int(textLen / keyLen)):
        stop = start + keyLen
        textBlocks.append(list(textList[start:stop]))
        start = stop
    #print('Splitted text:\n\t', textBlocks)
    return textBlocks

#textBlocks = splitBlocks(textList, len(key))+

def encrypt(text: str, key: str) -> str:
    textList = alignText(text, len(key))
    textBlocks = splitBlocks(textList, len(key))
    encryptedText = ''
    for textBlocksEl in textBlocks:
        for k in key:
            encryptedText += ''.join(textBlocksEl[int(k) - 1])
    print('Encrypted text:\n\t', encryptedText)
    #print('Encrypted list:\n\t', list(encryptedText))
    return encryptedText

def decrypt(text: str, key: str) -> str:
    textList = alignText(text, len(key))
    textBlocks = splitBlocks(textList, len(key))
    decryptedText = ''
    for textBlocksEl in textBlocks:
        decryptedBlock = list(textBlocksEl)
        for i in range(len(key)):
            decryptedBlock[int(key[i]) - 1] = textBlocksEl[i]
        decryptedText += ''.join(decryptedBlock)
    print('Decrypted text:\n\t', decryptedText)
    #print('Decrypted list:\n\t', list(decryptedText))
    return decryptedText

text = input('Введите текст: ')
key = '1472536' #'897613254'
encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

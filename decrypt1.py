# Decrypting with the private key
import ecies

def decryptWithPrivateKey(privateKey):
    with open('encryptedData.bin', "rb") as f:
        encryptedData = f.read()
    privateKey = str(privateKey)
    print(len(privateKey))
    print(type(privateKey))
    data = ecies.decrypt(privateKey, encryptedData)
    with open('text.bin', 'wb') as f:
        f.write(data)
    print(data)


# print(decryptWithPrivateKey(0x0f0a9f071c868b2a75a504c29c2f93ceb7464a8f0d9f768abaced69a66d90713))

# import decrypt1
import encrypt1
# import encrypt2
# import decrypt2
import generatePrivateKey
from eth_account import Account


class mailbox():
    def __init__(self, ifHadAccount=False):
        self.__privateKey = 0x0
        self.address = 0x0
        """
        Initialize and Generate a EVM account.The Private Key Will Be stored As A Parameter
        :param ifHadAccount:
        """
        if ifHadAccount == False:
            self.__privateKey, self.address = generatePrivateKey.generate()

        else:
            privateKeyInHex = input('Please Import Your Private Key In Hex')
            acct = Account.privateKeyToAccount(privateKeyInHex)
            self.__privateKey = privateKeyInHex
            self.address = acct.address

    def encrypt(self):
        encrypt1.encryptWithPublicKey(type,self.__privateKey)
    #
    # def sign(self):
    #     encrypt2.signWithPrivateKey()
    #
    # def dycrypt(self):
    #     if decrypt2.verify():
    #         decrypt1.decryptWithPrivateKey()
    #     else:
    #         raise "ERROR"


msg = mailbox()
print(msg.address)


import openfhe
import numpy as np
import time
import matplotlib.pyplot as plt


context = None
def main(plaintext_modulus = 65537, N_DO=2,scheme = "BFV",  length_of_data = 8):
    global context
    if scheme == "BFV":
        params = openfhe.CCParamsBFVRNS()
    elif scheme == "BGV":
        params = openfhe.CCParamsBGVRNS()
    else:
        raise ValueError("Unsupported scheme. Use BFV or BGV.")

    params.SetPlaintextModulus(plaintext_modulus)
    context = openfhe.GenCryptoContext(params)
    context.Enable(openfhe.PKESchemeFeature.PKE)
    context.Enable(openfhe.PKESchemeFeature.LEVELEDSHE)
    context.Enable(openfhe.PKESchemeFeature.ADVANCEDSHE)

    Cloud.timer = 0
    Cloud.publicKey = 0
    Cloud.length_of_data = length_of_data


class Cloud:
    timer: int = 0
    publicKey: int

    length_of_data = 8
    @staticmethod
    def function_to_eval(C):
        result = context.Encrypt(Cloud.publicKey, context.MakePackedPlaintext([0]*Cloud.length_of_data))
        for c in C:
            result = context.EvalAdd(result, c)
        return result

    @staticmethod
    def function_equiv(D):
        result = [0]*Cloud.length_of_data
        for d in D:
            result = [result[i] + d[i] for i in range(len(result))]
        return result


class Type1:
    pass
class PureFHE(Type1):
    @staticmethod
    def EncodeData(v):  # Ciphertext
        return context.Encrypt(Cloud.publicKey, context.MakePackedPlaintext(v))

    @staticmethod
    def ProcessData(C):  # List of ciphertexts
        return Cloud.function_to_eval(C)
class Transcipher(Type1):
    @staticmethod
    def EncodeData(v): # Ciphertext
        raise NotImplementedError

    @staticmethod
    def ProcessData(C):  # List of ciphertexts
        raise NotImplementedError






class Type3:
    def __init__(self):
        self.total_time = 0
        self.spent_time = {}

    def append_time(self, naam, function, args=[], kwargs={}):
        start = time.time()
        resultaat = function(*args, **kwargs)
        enc_time = time.time() - start

        self.total_time += enc_time
        self.spent_time[naam] = enc_time

        return resultaat

class DataOwner(Type3):
    data: list
    CV: bool
    def __init__(self):
        super().__init__()
        self.data = np.random.randint(0, 2**10, size=Cloud.length_of_data).tolist()
        self.CV = 1 > 0.75  # rand

    def Encrypt_data(self):
        return context.Encrypt(Cloud.publicKey, context.MakePackedPlaintext(self.data))


class Server(Type3):
    def Computation(self, Data):
        # Data_CV = [d for d in Data if d is not None] # Should be done pre-transfer
        # Todo: thresholding
        return PureFHE.ProcessData(Data)

class DataCustomer(Type3):
    def __init__(self):
        super().__init__()
        self.secretKey = None

    def generate_key(self):
        keypair = context.KeyGen()
        context.EvalMultKeyGen(keypair.secretKey)
        context.EvalSumKeyGen(keypair.secretKey)

        Cloud.publicKey = keypair.publicKey
        self.secretKey = keypair.secretKey


    def decrypt_result(self, resultaat):
        return context.Decrypt(self.secretKey, resultaat).GetPackedValue()[0:Cloud.length_of_data]


class Type2:
    def __init__(self, transciphering: bool = False):
        # Logic to choose which class
        self.type1 = Transcipher if transciphering else PureFHE

        self.DO_s = [DataOwner() for i in range(N_DO)]
        self.S = Server()
        self.DC = DataCustomer()

        Cloud.timer += 1

    def main(self):
        # Step 1: Key generation
        self.DC.generate_key()

        # Step 2 Data Encryption
        Data = [DO.Encrypt_data() for DO in self.DO_s if DO.CV]  # If Nochoice/wel kijk effe
        Cloud.timer += len(Data)


        # Step 3: Transfer + computation
        enc_result = self.S.Computation(Data)

        # Step 4 + 5: Result transfer + Decryption
        resultaat = self.DC.decrypt_result(enc_result)

        Cloud.timer += 1
        return resultaat

    def verify(self):
        return Cloud.function_equiv([DO.data for DO in self.DO_s if DO.CV])

class NoChoice(Type2):
    pass


class ImpliedCV(Type2):
    pass



if __name__ == "__main__":
    ## WITH DO
    plaintext_modulus_list = [65537]  # [65537, 8088322049]
    repeat = 10

    if False:
        X = np.unique([int(x) for x in np.logspace(0, 3, 20)])
        Y = [[] for x in X]
        LEGEND = []
        for plaintext_modulus in plaintext_modulus_list:
            LEGEND.append("p=" + str(plaintext_modulus))  # laintext_modulus
            start_start = time.time()
            for index, N_DO in enumerate(X):
                lijajjaj = []
                for _ in range(repeat):
                    start = time.time()
                    main(plaintext_modulus, N_DO)
                    manager = Type2()
                    f1 = manager.main()
                    enc_time = time.time() - start
                    f2 = manager.verify()
                    lijajjaj.append(enc_time)

                Y[index].append(np.median(lijajjaj))
                # if all([f1[i] == f2[i] for i in range(Cloud.length_of_data)]):
                #     Y[index].append(enc_time)
                # else:
                #     Y[index].append(None)

                print("Modulus=", plaintext_modulus," N=",N_DO," Time=", Y[index][-1]," Transfer:",Cloud.timer)
            print(time.time() - start_start)

        plt.loglog(X, Y)
        # plt.xticks([i for i in range(len(X))],X)
        # plt.bar([str(x) for x in X], [x[0] for x in Y])
        # plt.legend(LEGEND)
        plt.xlabel("Amount of DOs")
        plt.ylabel("Time required for full Algorithm")
        plt.savefig("OpenFHE_DO.png", bbox_inches="tight")
        plt.close()


    ## WITH DC
    if False:
        N_DO = 50
        X = np.unique([int(x) for x in np.logspace(0,2,20)])
        Y = [[] for x in X]
        LEGEND = []
        for plaintext_modulus in plaintext_modulus_list:
            LEGEND.append("p=" + str(plaintext_modulus))  # laintext_modulus
            start_start = time.time()
            for index, N_DC in enumerate(X):

                som = 0
                for _ in range(repeat):
                    start = time.time()
                    main(plaintext_modulus, N_DO)
                    manager = Type2()
                    for _ in range(min(N_DC,1)):
                        f1 = manager.main()
                    enc_time = N_DC * (time.time() - start)
                    f2 = manager.verify()

                    som += enc_time

                Y[index].append(som / repeat)
                # if all([f1[i] == f2[i] for i in range(Cloud.length_of_data)]):
                #     Y[index].append(enc_time)
                # else:
                #     Y[index].append(None)

                print("Modulus=", plaintext_modulus," N=", N_DC," Time=", Y[index][-1]," Transfer:", Cloud.timer)

            print(time.time() - start_start)

        plt.loglog(X, Y)
        # plt.legend(LEGEND)
        plt.xlim([1,100])
        plt.xlabel("Amount of DCs")
        plt.ylabel("Time required for full Algorithm")
        plt.savefig(f"OpenFHE_DC.png", bbox_inches="tight")
        plt.close()

    ## WITH Data points
    if False:
        repeat *= 10
        N_DO = 50
        X = np.unique([int(x) for x in np.logspace(0,3,20)])
        Y = [[] for x in X]
        LEGEND = []
        for plaintext_modulus in plaintext_modulus_list:
            LEGEND.append("p=" + str(plaintext_modulus))  # laintext_modulus
            start_start = time.time()
            for index, N_DP in enumerate(X):

                som = 0
                for _ in range(repeat):
                    start = time.time()
                    main(plaintext_modulus, N_DO, length_of_data=N_DP)
                    manager = Type2()
                    f1 = manager.main()
                    enc_time = time.time() - start
                    f2 = manager.verify()

                    som += enc_time

                Y[index].append(som / repeat)
                # if all([f1[i] == f2[i] for i in range(Cloud.length_of_data)]):
                #     Y[index].append(enc_time)
                # else:
                #     Y[index].append(None)

                print("Modulus=", plaintext_modulus, " N=", N_DP, " Time=", Y[index][-1], " Transfer:", Cloud.timer)

            print(time.time() - start_start)

        plt.loglog(X, Y)
        # plt.legend(LEGEND)
        plt.xlabel("Amount of Data points's")
        plt.ylabel("Time required for full Algorithm")
        plt.title("Time requirement across different Plaintext Moduli")
        plt.savefig(f"OpenFHE_point.png", bbox_inches="tight")
        plt.close()
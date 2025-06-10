import random
from openfhe import *

def main():
    # Step 1: Initialize CKKS parameters and context
    parameters = CCParamsCKKSRNS()
    parameters.SetMultiplicativeDepth(1)
    parameters.SetScalingModSize(50)
    parameters.SetBatchSize(8)

    cc = GenCryptoContext(parameters)
    cc.Enable(PKESchemeFeature.PKE)
    cc.Enable(PKESchemeFeature.KEYSWITCH)
    cc.Enable(PKESchemeFeature.LEVELEDSHE)

    # Step 2: Generate keys
    keys = cc.KeyGen()
    cc.EvalMultKeyGen(keys.secretKey)
    cc.EvalRotateKeyGen(keys.secretKey, [1, -2])

    # Step 6: Weighted average calculation
    data_plain = [[random.random() * 10 for _ in range(8)] for _ in range(5)]
    packed_data = [cc.MakeCKKSPackedPlaintext(d) for d in data_plain]
    encrypted_data = [cc.Encrypt(keys.publicKey, pd) for pd in packed_data]

    som = cc.Encrypt(keys.publicKey, cc.MakeCKKSPackedPlaintext([0] * 8))
    for encd in encrypted_data:
        som = cc.EvalAdd(som, encd)
    average = cc.EvalMult(som, 1/5)

    result = cc.Decrypt(average, keys.secretKey)
    print("Average: ", result.GetFormattedValues(8))

if __name__ == "__main__":
    main()
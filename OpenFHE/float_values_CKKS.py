import random

from openfhe import *

import time

def main():
    start = time.time()

    mult_depth = 1
    scale_mod_size = 50
    batch_size = 8

    parameters = CCParamsCKKSRNS()
    parameters.SetMultiplicativeDepth(mult_depth)
    parameters.SetScalingModSize(scale_mod_size)
    parameters.SetBatchSize(batch_size)

    cc = GenCryptoContext(parameters)
    cc.Enable(PKESchemeFeature.PKE)
    cc.Enable(PKESchemeFeature.KEYSWITCH)
    cc.Enable(PKESchemeFeature.LEVELEDSHE)


    print(f'Time Step 1: {time.time() - start}')
    start = time.time()

    print("The CKKS scheme is using ring dimension: " + str(cc.GetRingDimension()))

    keys = cc.KeyGen()
    cc.EvalMultKeyGen(keys.secretKey)
    cc.EvalRotateKeyGen(keys.secretKey, [1, -2])


    print(f'Time Step 2: {time.time() - start}')
    start = time.time()

    x1 = [0.25, 0.5, 0.75, 1.0, 2.0, 3.0, 4.0, 5.0]
    x2 = [5.0, 4.0, 3.0, 2.0, 1.0, 0.75, 0.5, 0.25]

    ptx1 = cc.MakeCKKSPackedPlaintext(x1)
    ptx2 = cc.MakeCKKSPackedPlaintext(x2)

    print("Input x1: " + str(ptx1))
    print("Input x2: " + str(ptx2))



    # Encrypt the encoded vectors
    c1 = cc.Encrypt(keys.publicKey, ptx1)
    c2 = cc.Encrypt(keys.publicKey, ptx2)

    print(f'Time Step 3: {time.time() - start}')
    start = time.time()


    # Step 4: Evaluation
    # Homomorphic additions
    c_add = cc.EvalAdd(c1, c2)
    # Homomorphic subtraction
    c_sub = cc.EvalSub(c1, c2)
    # Homomorphic scalar multiplication
    c_scalar = cc.EvalMult(c1, 4)
    # Homomorphic multiplication
    c_mult = cc.EvalMult(c1, c2)
    # Homomorphic rotations
    c_rot1 = cc.EvalRotate(c1, 1)
    c_rot2 = cc.EvalRotate(c1, -2)


    print(f'Time Step 4: {time.time() - start}')
    start = time.time()

    # Step 5: Decryption and output
    # Decrypt the result of additions
    ptAdd = cc.Decrypt(c_add, keys.secretKey)
    print("\nResults of homomorphic additions: ")
    print(ptAdd)

    # We set the precision to 8 decimal digits for a nicer output.
    # If you want to see the error/noise introduced by CKKS, bump it up
    # to 15 and it should become visible.

    precision = 8
    print("\nResults of homomorphic computations:")
    result = cc.Decrypt(c1, keys.secretKey)
    result.SetLength(batch_size)
    print("x1 = " + result.GetFormattedValues(precision))

    # Decrypt the result of scalar multiplication
    result = cc.Decrypt(c_scalar, keys.secretKey)
    result.SetLength(batch_size)
    print("4 * x1 = " + result.GetFormattedValues(precision))

    # Decrypt the result of multiplication
    result = cc.Decrypt(c_mult, keys.secretKey)
    result.SetLength(batch_size)
    print("x1 * x2 = " + result.GetFormattedValues(precision))

    # Decrypt the result of rotations
    result = cc.Decrypt(c_rot1, keys.secretKey)
    result.SetLength(batch_size)
    print("\nIn rotations, very small outputs (~10^-10 here) correspond to 0's:")
    print("x1 rotated by 1 = " + result.GetFormattedValues(precision))

    result = cc.Decrypt(c_rot2, keys.secretKey)
    result.SetLength(batch_size)
    print("x1 rotated by -2 = " + result.GetFormattedValues(precision))



    print(f'Time Step 5: {time.time() - start}')
    start = time.time()











    print("\n" * 5)


    print("Now we can also do the average calculation on the 'cloud'/untrusted computer")
    print("Lets take 5 datapoints and average them. Lets pick some number between 0 (inclusive) and 10(Exclusive)")

    data_plain = [[random.random() * 10 for i in range(batch_size)]for j in range(5)]
    packed_data = [cc.MakeCKKSPackedPlaintext(d) for d in data_plain]
    print(packed_data)
    encryped_data = [cc.Encrypt(keys.publicKey, pd) for pd in packed_data]


    som = cc.Encrypt(keys.publicKey, cc.MakeCKKSPackedPlaintext([0 for i in range(batch_size)]))
    for encd in encryped_data:
        som = cc.EvalAdd(som, encd)
    average = cc.EvalMult(som, 1/5)

    result = cc.Decrypt(som, keys.secretKey)
    result.SetLength(batch_size)
    print(f"Sum: {result.GetFormattedValues(precision)}")

    result = cc.Decrypt(average, keys.secretKey)
    result.SetLength(batch_size)
    print(f"average: {result.GetFormattedValues(precision)}")



    direct = [sum([data_plain[j][i] for j in range(5)])/5 for i in range(batch_size)]
    print(f"Direct calc: {direct}")
    indirect = Plaintext.GetRealPackedValue(cc.Decrypt(average, keys.secretKey))
    diff = [indirect[i] - direct[i] for i in range(batch_size)]

    print(f"sum: {sum([abs(d) for d in diff])}, difference: {diff}")




    print(f'Time Step: {time.time() - start}')
    start = time.time()


















if __name__ == "__main__":
    main()
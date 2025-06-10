# Initial Settings
from openfhe import *
import os

# import openfhe.PKESchemeFeature as Feature

import time




def main():
    start = time.time()
    
    # Sample Program: Step 1: Set CryptoContext
    parameters = CCParamsBGVRNS()
    parameters.SetPlaintextModulus(65537)
    parameters.SetMultiplicativeDepth(2)

    crypto_context = GenCryptoContext(parameters)
    # Enable features that you wish to use
    crypto_context.Enable(PKESchemeFeature.PKE)
    crypto_context.Enable(PKESchemeFeature.KEYSWITCH)
    crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)


    print(f'Time Step 1: {time.time() - start}')
    start = time.time()
    # Sample Program: Step 2: Key Generation

    # Generate a public/private key pair
    key_pair = crypto_context.KeyGen()

    # Generate the relinearization key
    crypto_context.EvalMultKeyGen(key_pair.secretKey)

    # Generate the rotation evaluation keys
    crypto_context.EvalRotateKeyGen(key_pair.secretKey, [1, 2, -1, -2])


    print(f'Time Step 2: {time.time() - start}')
    start = time.time()
    # Sample Program: Step 3: Encryption



    # First plaintext vector is encoded
    vector_of_ints1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plaintext1 = crypto_context.MakePackedPlaintext(vector_of_ints1)

    # Second plaintext vector is encoded
    vector_of_ints2 = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plaintext2 = crypto_context.MakePackedPlaintext(vector_of_ints2)

    # Third plaintext vector is encoded
    vector_of_ints3 = [1, 2, 5, 2, 5, 6, 7, 8, 9, 10, 11, 12]
    plaintext3 = crypto_context.MakePackedPlaintext(vector_of_ints3)

    # The encoded vectors are encrypted
    ciphertext1 = crypto_context.Encrypt(key_pair.publicKey, plaintext1)
    ciphertext2 = crypto_context.Encrypt(key_pair.publicKey, plaintext2)
    ciphertext3 = crypto_context.Encrypt(key_pair.publicKey, plaintext3)

    loopwaardig = [ciphertext1, ciphertext2, ciphertext3]

    n = len(vector_of_ints1)
    def get_constant(number):
        return crypto_context.Encrypt(key_pair.publicKey, crypto_context.MakePackedPlaintext([number for i in range(n)]))

    


    print(f'Time Step 3: {time.time() - start}')
    start = time.time()
    #  Sample Program: Step 4: Evaluation

    # Homomorphic additions
    ciphertext_add12 = crypto_context.EvalAdd(ciphertext1, ciphertext2)
    ciphertext_add_result = crypto_context.EvalAdd(ciphertext_add12, ciphertext3)

    # Homomorphic Multiplication
    ciphertext_mult12 = crypto_context.EvalMult(ciphertext1, ciphertext2)
    ciphertext_mult_result = crypto_context.EvalMult(ciphertext_mult12, ciphertext3)

    # Weighted average:
    weights = [2, 1, 3]
    sum_weights = sum(weights)



    weighted_sum = get_constant(0)
    for i in range(3):
        weights_array = [get_constant(w) for w in weights]
        weighted_sum = crypto_context.EvalAdd(weighted_sum, crypto_context.EvalMult(weights_array[i], loopwaardig[i]))



    print(f'Time Step 4: {time.time() - start}')
    start = time.time()
    # Sample Program: Step 5: Decryption

    # Decrypt the result of additions
    plaintext_add_result = crypto_context.Decrypt(
        ciphertext_add_result, key_pair.secretKey
    )

    # Decrypt the result of multiplications
    plaintext_mult_result = crypto_context.Decrypt(
        ciphertext_mult_result, key_pair.secretKey
    )


    # Decrytpt of weighted numerator
    plaintext_teller = crypto_context.Decrypt(
        weighted_sum, key_pair.secretKey
    )

    
    
    print(f'Time Step 5: {time.time() - start}')
    
    print("\n" * 5)

    print("Plaintext #1: " + str(plaintext1))
    print("Plaintext #2: " + str(plaintext2))
    print("Plaintext #3: " + str(plaintext3))
    

    # Output Results
    print("\nResults of homomorphic computations")
    print("#1 + #2 + #3 = " + str(plaintext_add_result))
    print("#1 * #2 * #3 = " + str(plaintext_mult_result))
    print()
    print(f"Weights: {weights}")
    print(f"Weighted sum: {plaintext_teller} / {sum_weights}")
    print(f"= {[i/sum_weights for i in Plaintext.GetPackedValue(plaintext_teller) if i != 0]}")


    print("\n" * 5)

    print("testing if negativeintegers work")
    print(f" 0 + -1 = {crypto_context.Decrypt(crypto_context.EvalAdd(get_constant(0), get_constant(-1)), key_pair.secretKey)}")
    print(f" 1 + -0 = {crypto_context.Decrypt(crypto_context.EvalAdd(get_constant(1), get_constant(-0)), key_pair.secretKey)}")
    print(f"-1 + -1 = {crypto_context.Decrypt(crypto_context.EvalAdd(get_constant(-1), get_constant(-1)), key_pair.secretKey)}")
    print(f" 2 + -1 = {crypto_context.Decrypt(crypto_context.EvalAdd(get_constant(2), get_constant(-1)), key_pair.secretKey)}")
    print(f"-1 +  2 = {crypto_context.Decrypt(crypto_context.EvalAdd(get_constant(-1), get_constant(2)), key_pair.secretKey)}")
    print(f"-2 + -1 = {crypto_context.Decrypt(crypto_context.EvalAdd(get_constant(-2), get_constant(-1)), key_pair.secretKey)}")
    print(f"-1 *  1 = {crypto_context.Decrypt(crypto_context.EvalMult(get_constant(-1), get_constant(1)), key_pair.secretKey)}")
    print(f"-1 * -1 = {crypto_context.Decrypt(crypto_context.EvalMult(get_constant(-1), get_constant(-1)), key_pair.secretKey)}")
    print(f"-1 * -0 = {crypto_context.Decrypt(crypto_context.EvalMult(get_constant(-1), get_constant(-0)), key_pair.secretKey)}")


    a = get_constant(-1)











if __name__ == "__main__":
    main()

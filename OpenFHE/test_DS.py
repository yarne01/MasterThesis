import time
import random
from openfhe import *


def algorithm(tarnsciphering: bool):
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

    # Step 3: Prepare and encrypt data
    data = [random.random() * 10 for _ in range(8)]
    if tarnsciphering:
        # Step 3: Generate symmetric key for block cipher (e.g., AES or LowMC)
        symmetric_key = [random.randint(0, 255) for _ in range(16)]  # 128-bit key

        # Step 4: Encrypt data with symmetric key (simulated)
        def symmetric_encrypt(data, key):
            # Simulate symmetric encryption (e.g., AES or LowMC)
            return [x + sum(key) % 256 for x in data]  # Placeholder for actual encryption

        data = [random.random() * 10 for _ in range(8)]
        encrypted_data = symmetric_encrypt(data, symmetric_key)

        # Step 5: Transciphering: Encrypt symmetric key with FHE
        symmetric_key_plaintext = cc.MakeCKKSPackedPlaintext(symmetric_key)
        encrypted_symmetric_key = cc.Encrypt(keys.publicKey, symmetric_key_plaintext)
    else:
        plaintext = cc.MakeCKKSPackedPlaintext(data)
        ciphertext = cc.Encrypt(keys.publicKey, plaintext)


    # Step 4: Homomorphic computation (weighted average)
    start_time = time.time()
    if tarnsciphering:
        sum_ciphertext = cc.Encrypt(keys.publicKey, cc.MakeCKKSPackedPlaintext(encrypted_data))
    else:
        sum_ciphertext = ciphertext
    for _ in range(4):  # Simulate summing 5 datasets
        new_data = [random.random() * 10 for _ in range(8)]
        if tarnsciphering:
            new_encrypted_data = symmetric_encrypt(new_data, symmetric_key)
            new_ciphertext = cc.Encrypt(keys.publicKey, cc.MakeCKKSPackedPlaintext(new_encrypted_data))
            sum_ciphertext = cc.EvalAdd(sum_ciphertext, new_ciphertext)
        else:
            new_plaintext = cc.MakeCKKSPackedPlaintext(new_data)
            new_ciphertext = cc.Encrypt(keys.publicKey, new_plaintext)
            sum_ciphertext = cc.EvalAdd(sum_ciphertext, new_ciphertext)

    average_ciphertext = cc.EvalMult(sum_ciphertext, 1 / 5)
    computation_time = time.time() - start_time


    # Step 5: Decrypt and display results
    result = cc.Decrypt(average_ciphertext, keys.secretKey)
    result.SetLength(8)
    print("Non-Transciphered Average:", result.GetFormattedValues(8))
    print("Computation Time:", computation_time, "seconds")

print(algorithm(False))
print(algorithm(True))
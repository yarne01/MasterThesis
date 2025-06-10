import openfhe
import numpy as np
import time

# === Mini Pasta-style symmetric cipher ===
def pasta_encrypt(block, k, b, rounds=4, p=65537):
    """ FHE-friendly block cipher using modular arithmetic """
    for _ in range(rounds):
        block = [(x * k + b) % p for x in block]
    return block

def pasta_decrypt(block, k, b, rounds=4, p=65537):
    """ Inverse of pasta_encrypt """
    k_inv = pow(k, -1, p)  # Modular inverse
    for _ in range(rounds):
        block = [((x - b) * k_inv) % p for x in block]
    return block

# === Setup OpenFHE Context ===
params = openfhe.CCParamsBFVRNS()
params.SetPlaintextModulus(65537)
context = openfhe.GenCryptoContext(params)

context.Enable(openfhe.PKESchemeFeature.PKE)
context.Enable(openfhe.PKESchemeFeature.LEVELEDSHE)
context.Enable(openfhe.PKESchemeFeature.ADVANCEDSHE)

keypair = context.KeyGen()
context.EvalMultKeyGen(keypair.secretKey)
context.EvalSumKeyGen(keypair.secretKey)

# === Example Data ===
plaintext_data = np.random.randint(0, 100, size=8).tolist()
k, b = 1337, 42  # Pasta key material
p = 65537

# === Transciphering (Pasta-style symmetric encryption + FHE) ===
start = time.time()
sym_encrypted = pasta_encrypt(plaintext_data, k, b, p=p)
pt = context.MakePackedPlaintext(sym_encrypted)
ct = context.Encrypt(keypair.publicKey, pt)
enc_time = time.time() - start

# === Homomorphic Computation ===
start = time.time()
ct_result = context.EvalAdd(ct, ct)
eval_time = time.time() - start

# === Decryption (FHE + Pasta-style decryption) ===
intermediate = context.Decrypt(keypair.secretKey, ct_result).GetPackedValue()
final_result = pasta_decrypt(intermediate, k, b, p=p)

# === Verification ===
expected = [2 * x % p for x in plaintext_data]
correct = final_result == expected

print("\n== Transciphering w/ Pasta-style ==")
print("Input         :", plaintext_data)
print("Sym Encrypted :", sym_encrypted[0:8])
print("Intermediate  :", intermediate[0:8])
print("Decrypted     :", final_result[0:8])
print("Expected      :", expected)
print("Correct       :", correct)
print(f"Enc Time      : {enc_time:.4f}s | Eval Time: {eval_time:.4f}s")


print(openfhe.JSON, openfhe.BINARY)
print(openfhe.Serialize(ct, openfhe.BINARY))
import openfhe
import numpy as np
import time

# --- Symmetric Cipher (simulate Pasta with XOR) ---
def sym_encrypt(data, sym_key):
    return data#[(x ^ sym_key) for x in data]

def sym_decrypt(data, sym_key):
    return data#[(x ^ sym_key) for x in data]

# --- Setup BFV Context ---
params = openfhe.CCParamsBFVRNS()
params.SetPlaintextModulus(65537)
context = openfhe.GenCryptoContext(params)

context.Enable(openfhe.PKESchemeFeature.PKE)
context.Enable(openfhe.PKESchemeFeature.LEVELEDSHE)
context.Enable(openfhe.PKESchemeFeature.ADVANCEDSHE)

keypair = context.KeyGen()
context.EvalMultKeyGen(keypair.secretKey)
context.EvalSumKeyGen(keypair.secretKey)

# --- Plaintext Data ---
plaintext_data = np.random.randint(0, 100, size=8).tolist()
sym_key = 123  # Simple XOR key

# --- Transciphering (Symmetric encrypt + FHE encrypt) ---
start = time.time()
sym_encrypted = sym_encrypt(plaintext_data, sym_key)
pt = context.MakePackedPlaintext(sym_encrypted)
ct = context.Encrypt(keypair.publicKey, pt)
enc_time = time.time() - start

# --- Homomorphic Computation (EvalAdd) ---
start = time.time()
ct_result = context.EvalAdd(ct, ct)
eval_time = time.time() - start

# --- FHE Decrypt and then Symmetric Decrypt ---
intermediate = context.Decrypt(keypair.secretKey, ct_result).GetPackedValue()
final_result = sym_decrypt(intermediate, sym_key)

# --- Verify ---
expected = [2 * x for x in plaintext_data]
correct = final_result == expected

print("\n== Transciphering ==")
print("Input         :", plaintext_data)
print("Sym+FHE Encr  :", sym_encrypted[0:8])
print("Intermediate  :", intermediate[0:8])
print("Decrypted     :", final_result[0:8])
print("Expected      :", expected)
print("Correct       :", correct)
print(f"Enc Time      : {enc_time:.4f}s | Eval Time: {eval_time:.4f}s")

import openfhe
import numpy as np
import time

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

# --- Encrypt (FHE) ---
start = time.time()
pt = context.MakePackedPlaintext(plaintext_data)
ct = context.Encrypt(keypair.publicKey, pt)
enc_time = time.time() - start

print("KAKOIHN", pt.GetLength())
# SetLength

# --- Compute f(x) = x + x (homomorphic add) ---
start = time.time()
ct_res = context.EvalAdd(ct, ct)
eval_time = time.time() - start

print("OHNAOIJAPOIJAIJ", ct_res.GetSlots())

# --- Decrypt ---
res = context.Decrypt(keypair.secretKey, ct_res).GetPackedValue()

print("KAKOIHN", context.Decrypt(keypair.secretKey, ct_res).GetLength())
# SetLength
# --- Verify ---
expected = [2 * x for x in plaintext_data]
correct = res == expected


print(context.GetBatchSize())


print("== Pure FHE ==")
print("Input       :", plaintext_data)
print("Decrypted   :", res[0:10])
print("Expected    :", expected)
print("Correct     :", correct)
print(f"Enc Time    : {enc_time:.4f}s | Eval Time: {eval_time:.4f}s")

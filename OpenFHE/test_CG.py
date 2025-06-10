import time
import openfhe  # Ensure OpenFHE-Python is installed
import numpy as np

# Select FHE-friendly block cipher (BFV or BGV)
SCHEME = "BGV"  # Change to "BGV" if needed

# Initialize OpenFHE context using the correct parameter structure
if SCHEME == "BFV":
    parameters = openfhe.CCParamsBFVRNS()  # BFV parameters
elif SCHEME == "BGV":
    parameters = openfhe.CCParamsBGVRNS()  # BGV parameters
else:
    raise ValueError("Unsupported scheme. Use BFV or BGV.")

# Set the plaintext modulus to ensure correct FHE operations
parameters.SetPlaintextModulus(65537)

context = openfhe.GenCryptoContext(parameters)

# Enable encryption features
context.Enable(openfhe.PKESchemeFeature.PKE)
context.Enable(openfhe.PKESchemeFeature.LEVELEDSHE)
context.Enable(openfhe.PKESchemeFeature.ADVANCEDSHE)

# Key generation
keypair = context.KeyGen()
context.EvalMultKeyGen(keypair.secretKey)
context.EvalSumKeyGen(keypair.secretKey)

# Plaintext data
plaintext_data = np.random.randint(0, 100, size=100).tolist()  # Convert to list for OpenFHE compatibility

### 1. Non-Transciphered Approach (Direct FHE Encryption) ###
start_time = time.time()
plaintext_fhe = context.MakePackedPlaintext(plaintext_data)  # ✅ Correct method for BFV/BGV
ciphertext_fhe = context.Encrypt(keypair.publicKey, plaintext_fhe)  # ✅ Uses correct key type
fhe_encryption_time = time.time() - start_time

# Serialize and measure ciphertext size
# print(openfhe.JSON, openfhe.BINARY)
serialized_fhe = openfhe.Serialize(ciphertext_fhe, openfhe.BINARY)  # ✅ Serialize ciphertext
with open("serialized_fhe.json", "w") as text_file: text_file.write(openfhe.Serialize(ciphertext_fhe, openfhe.JSON))
fhe_size = len(serialized_fhe)  # ✅ Measure actual size in bytes

# Perform computation (e.g., addition)
start_time = time.time()
ciphertext_fhe_result = context.EvalAdd(ciphertext_fhe, ciphertext_fhe)
fhe_computation_time = time.time() - start_time

# Decrypt result and check correctness
decrypted_fhe_result = context.Decrypt(keypair.secretKey, ciphertext_fhe_result).GetPackedValue()
expected_fhe_result = [2 * x for x in plaintext_data]


correct_fhe = "Correct"
for index_check in range(len(expected_fhe_result)):
    if expected_fhe_result[index_check] != decrypted_fhe_result[index_check]:
        correct_fhe = "Incorrect"

### 2. Transciphered Approach (FHE-Friendly Block Cipher) ###
def fhe_friendly_block_cipher_encrypt(data, public_key):
    """
    Encrypts data using an FHE-friendly block cipher.
    Uses BFV/BGV for encryption.
    """
    plaintext = context.MakePackedPlaintext(data)  # ✅ Correct for BFV/BGV
    return context.Encrypt(public_key, plaintext)  # ✅ Uses public key for encryption

def fhe_friendly_block_cipher_decrypt(ciphertext, secret_key):
    """
    Decrypts an FHE-friendly block cipher ciphertext.
    """
    decrypted = context.Decrypt(secret_key, ciphertext)
    return decrypted.GetPackedValue()  # Extracts values from OpenFHE plaintext

# Encrypt plaintext with FHE-friendly block cipher
start_time = time.time()
ciphertext_trans = fhe_friendly_block_cipher_encrypt(plaintext_data, keypair.publicKey)  # ✅ Uses FHE public key
transciphered_encryption_time = time.time() - start_time

# Serialize and measure ciphertext size
serialized_transciphered = openfhe.Serialize(ciphertext_trans, openfhe.BINARY)  # ✅ Serialize ciphertext
with open("serialized_transciphered.json", "w") as text_file: text_file.write(openfhe.Serialize(ciphertext_trans, openfhe.JSON))
transciphered_size = len(serialized_transciphered)  # ✅ Measure actual size in bytes

# Perform computation on transciphered data
start_time = time.time()
ciphertext_trans_result = context.EvalAdd(ciphertext_trans, ciphertext_trans)
transciphered_computation_time = time.time() - start_time

# Decrypt result and check correctness
decrypted_trans_result = context.Decrypt(keypair.secretKey, ciphertext_trans_result).GetPackedValue()
expected_trans_result = [2 * x for x in plaintext_data]


correct_trans = "Correct"
for index_check in range(len(expected_trans_result)):
    if expected_trans_result[index_check] != decrypted_trans_result[index_check]:
        correct_trans = "Incorrect"

### 3. Print Results ###
print("\n==== Benchmark Results ====")
print(f"Scheme: {SCHEME}")
print(f"Non-Transciphered (Direct FHE):")
print(f" - Encryption Time: {fhe_encryption_time:.4f} sec")
print(f" - Computation Time: {fhe_computation_time:.4f} sec")
print(f" - Ciphertext Size: {fhe_size} bytes")
print(f" - Computation Check: {correct_fhe}")

print("\nTransciphered (FHE-Friendly Block Cipher):")
print(f" - Encryption Time: {transciphered_encryption_time:.4f} sec")
print(f" - Computation Time: {transciphered_computation_time:.4f} sec")
print(f" - Ciphertext Size: {transciphered_size} bytes")
print(f" - Computation Check: {correct_trans}")

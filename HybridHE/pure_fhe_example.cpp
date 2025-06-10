#include <iostream>
#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // 1. Initialize BFV/BGV FHE Context
    CCParams<CryptoContextBFVRNS> parameters;
    parameters.SetPlaintextModulus(65537);
    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    // Enable FHE Features
    cc->Enable(PKESchemeFeature::PKE);
    cc->Enable(PKESchemeFeature::LEVELEDSHE);

    // 2. Key Generation
    auto keyPair = cc->KeyGen();
    cc->EvalMultKeyGen(keyPair.secretKey);
    cc->EvalSumKeyGen(keyPair.secretKey);

    // 3. Encrypt Plaintext
    std::vector<int64_t> data = {5, 10, 15, 20};  // Example data
    Plaintext plaintext = cc->MakePackedPlaintext(data);
    auto ciphertext = cc->Encrypt(keyPair.publicKey, plaintext);

    // 4. Perform Computation (Homomorphic Addition)
    auto ciphertext_result = cc->EvalAdd(ciphertext, ciphertext);

    // 5. Decrypt & Output
    Plaintext decrypted_result;
    cc->Decrypt(keyPair.secretKey, ciphertext_result, &decrypted_result);

    std::cout << "Decrypted Result: ";
    for (auto val : decrypted_result->GetPackedValue()) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}

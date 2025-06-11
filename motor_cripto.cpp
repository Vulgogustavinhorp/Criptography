#include <iostream>
#include <string>
#include <vector>

std::string xor_cipher(const std::string& input, const std::string& key) {
    std::string output = input;
    for (size_t i = 0; i < input.length(); ++i) {
        output[i] = input[i] ^ key[i % key.length()];
    }
    return output;
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        return 1;
    }

    std::string action = argv[1];
    std::string key = argv[2];
    std::string text = argv[3];

    if (action == "encrypt" || action == "decrypt") {
        std::cout << xor_cipher(text, key);
    } else {
        return 1;
    }

    return 0;
}
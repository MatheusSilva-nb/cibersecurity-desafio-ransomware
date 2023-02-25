import os
import pyaes

# Definir o nome do arquivo a ser criptografado
file_name = "arquivo.txt"

# Abrir o arquivo em modo de leitura binária
with open(file_name, "rb") as file:
    file_data = file.read()

# Gerar uma chave de criptografia
key = b"minhachavedecriptografia"

# Criar um objeto AESModeOfOperationCTR com a chave gerada
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o conteúdo do arquivo
crypto_data = aes.encrypt(file_data)

# Definir o nome do arquivo criptografado
encrypted_file_name = file_name + ".criptografado"

# Salvar o arquivo criptografado
with open(encrypted_file_name, "wb") as encrypted_file:
    encrypted_file.write(crypto_data)

# Remover o arquivo original
os.remove(file_name)

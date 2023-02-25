import os
import pyaes

# Definir o nome do arquivo criptografado
file_name = "arquivo.txt.criptografado"

# Abrir o arquivo criptografado em modo de leitura binária
with open(file_name, "rb") as file:
    encrypted_data = file.read()

# Gerar a mesma chave de criptografia usada no script de criptografia
key = b"minhachavedecriptografia"

# Criar um objeto AESModeOfOperationCTR com a chave gerada
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar o conteúdo do arquivo criptografado
decrypted_data = aes.decrypt(encrypted_data)

# Definir o nome do arquivo descriptografado
decrypted_file_name = file_name.replace(".criptografado", "")

# Salvar o arquivo descriptografado
with open(decrypted_file_name, "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

# Remover o arquivo criptografado
os.remove(file_name)

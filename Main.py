from ChaCha import ChaCha
import argparse
import os, sys

def run(args):
    input_path = args.input
    output_path = args.output
    key_path = args.key

    if not os.path.isfile(input_path):
        print('The Input path does not exist!!')
        sys.exit()

    # if not os.path.isfile(output_path):
        # print('The Output path does not exist!!')
        # sys.exit()
        
    if not os.path.isfile(key_path):
        print('The Key file path does not exist!!')
        sys.exit()

    with open(key_path) as f:
        key = f.readline()
        nonce = f.readline()

    key = key.encode('utf-8')
    nonce = nonce.encode('utf-8')

    encryptor = ChaCha.ChaCha(key, nonce)

    if args.encrypt:
        with open(input_path) as f:
            message = f.readlines()

        print(type(message[0]))
        plaintext = message[0].encode('utf-8')
        print(plaintext)
        ciphertext = encryptor.encrypt(plaintext)
        print(ciphertext)
        ciphertext = bytes(ciphertext)
        print(ciphertext)

        with open(output_path,"wb") as f:
            # cipher = ciphertext.decode('utf-8') 
            # print(cipher)
            f.write(ciphertext)

        print("Encrypted Successfully!!")
        sys.exit()

    elif args.decrypt:
        with open(input_path, 'rb') as f:
            ciphertext = f.read()

        # ciphertext = message.encode('utf-8')
        plaintext  = encryptor.decrypt(ciphertext)
        print(plaintext)

        with open(output_path,"w") as f:
            message = plaintext.decode('utf-8')
            print(message)
            f.write(message)

        print("Decrypted Successfully!!")
        sys.exit()


def main():
    parser = argparse.ArgumentParser(description="Encrypts and Decrypts text and image files using the ChaCha20 encryption algorithm", epilog="Enjoy the program! :)")
    parser.add_argument("-i","--in", help="Input file path", dest="input", type=str, required=True)
    parser.add_argument("-o","--out", help="Output file path", dest="output", type=str, required=True)
    parser.add_argument("-k","--key", help="Key file path", dest="key", type=str, required=True)
    parser.add_argument("-e","--encrypt", help="For encrypting the file", dest="encrypt", action='store_true')
    parser.add_argument("-d","--decrypt", help="For decrypting the file", dest="decrypt", action='store_true')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

main()
    




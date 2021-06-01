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

    if not os.path.isfile(output_path):
        print('The Output path does not exist!!')
        sys.exit()
        
    if not os.path.isfile(key_path):
        print('The Key file path does not exist!!')
        sys.exit()


def main():
    parser = argparse.ArgumentParser(description="Encrypts and Decrypts text and image files using the ChaCha20 encryption algorithm", epilog="Enjoy the program! :)")
    parser.add_argument("-i","--in", help="Input file path", dest="input", type=str, required=True)
    parser.add_argument("-o","--out", help="Output file path", dest="output", type=str, required=True)
    parser.add_argument("-k","--key", help="Key file path", dest="key", type=str, required=True)
    parser.add_argument("-e","--encrypt", help="For encrypting the file", action='store_true')
    parser.add_argument("-d","--decrypt", help="For decrypting the file", action='store_true')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

main()
    




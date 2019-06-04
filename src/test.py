import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o','--open-file', help='Description', required=False)
parser.add_argument('-s','--save-file', help='Description', required=False)

args = parser.parse_args()

print(args.open_file)
print(args.save_file)
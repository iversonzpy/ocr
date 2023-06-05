import easyocr
import argparse

def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("--path", action="store", default='root', help="path for pic")
    return parser.parse_args()

if __name__ == '__main__':

    args = get_args()

    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext(args.path, detail = 0)
    print(result)



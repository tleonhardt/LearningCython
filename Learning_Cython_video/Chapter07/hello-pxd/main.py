import sys, os
from scipy import misc

# Make black and white images
import bwlib  # Cython


def main(filename):
    # Writes new data to stdout
    data = misc.imread(
            filename
            )
    bwlib.makegrey(data)
    misc.imsave(sys.stdout, data)


if __name__ == '__main__':
    params = sys.argv[1:]
    if not params:
        print('Need an image!')
    elif not os.path.exists(
            params[0]
            )
        print('File missing!')
    else:
        main(params[0])

from os import rename
from glob import glob


def main():
    
    """
    Rename unactive photos for 
    """
    
    for n in glob('*.jpg'):
        
        rename(n, n[:10] + '' + '.jpg')
        
if __name__ == "__main__":
    main()
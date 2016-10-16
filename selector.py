from os import rename
from glob import glob


def main():
    """
    Renames unactive photos for TM Alicja
    """
    rearticle_pos = ['8383014', '8383018', '8383021', '8383031', '8383033', '8383037', '8383045', '8383049', '8383068', '8383076', '8383103', '8383104', '8383105', '8383106', '8383122', '8383137', '8383138', '8383141', '8383157', '8383176', '8383177', '8383178', '8383179', '8383181', '8383182', '8383184', '8383185', '8383186', '8383201', '8383202', '8383206', '8383208', '8383213', '8383214', '8383215', '8383217', '8383221', '8383223', '8383224']
    
    for n in glob('*.jpg'):
        
        if n[:7] in rearticle_pos:
            rename(n, n[:-4] + '_rearticle_' + '.jpg')
        
if __name__ == "__main__":
    main()
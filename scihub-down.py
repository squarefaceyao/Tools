from scidownl.scihub import *

DOI = '10.1155/2017/5958321'

out = './1015-imitate-paper'

if __name__ == '__main__':
    sci = SciHub(DOI,out).download(choose_scihub_url_index=1)

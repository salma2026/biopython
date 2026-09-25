from Bio import SeqIO
from Bio.SeqUtils import GC
import os

def main():
   file = input("file:")
   name, ending = os.path.splitext(file)
   e = ending.strip(".")
   with open(file) as handle:
       for record in SeqIO.parse(handle, e):
           print(record.id , record.seq , len(record.seq))
           GC(record)






if __name__ == "__main__":
    main()

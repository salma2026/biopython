from Bio import SeqIO
import os

def main():
   file = input("file:")
   name, ending = os.path.splitext(file)
   for record in seqIO.parse(name, ending):
       print(record.id)






if __name__ == "__main__":
    main()

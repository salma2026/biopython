from Bio import SeqIO
import os

def main():
   file = input("file:")
   name, ending = os.path.splitext(file)
   e = ending.strip(".")
   
   for record in SeqIO.parse(name, e):
       print(record.id)






if __name__ == "__main__":
    main()

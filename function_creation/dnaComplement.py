def dnaComplement(DNA_seq):
    complement=[]
    complement[:0]=DNA_seq
    for i in range(len(complement)):
        if complement[i]=='A':
            complement[i]='T'
        elif complement[i]=='T':
            complement[i]='A'
        elif complement[i]=='G':
            complement[i]='C'
        elif complement[i]=='C':
            complement[i]='G'
    return complement

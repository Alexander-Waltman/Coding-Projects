def CodonToPeptide(codon_str: str) -> str:
    """
    Translates a codon into a peptide

    Parameters:
    codon_str (type: string) - 3 characters that make up a codon

    Output:
    (type: string) - the single letter that corresponds to the amino acid/peptide of the input codon
    """

    base1 = codon_str[0].upper()
    base2 = codon_str[1].upper()
    base3 = codon_str[2].upper()

    reading_frame1 = ""
    reading_frame2 = ""
    reading_frame3 = ""

    if base1 == "G":
        if base2 == "G":
            return "G"
        elif base2 == "A":
            if base3 == "G" or base3 == "A":
                return "E"
            else:
                return "D"
        elif base2 == "C":
            return "A"
        elif base2 == "U":
            return "V"


    elif base1 == "A":
        if base2 == "G":
            if base3 == "G" or base3 == "A":
                return "R"
            else:
                return "S"
        elif base2 == "A":
            if base3 == "G" or base3 == "A":
                return "K"
            else:
                return "N"
        elif base2 == "C":
            return "T"
        elif base2 == "U":
            if base3 == "G":
                return "M"
            else: return "I"


    elif base1 == "C":
        if base2 == "G":
            return "R"
        elif base2 == "A":
            if base3 == "G" or base3 == "A":
                return "Q"
            else:
                return "H"
        elif base2 == "C":
            return "P"
        elif base2 == "U":
            return "L"


    elif base1 == "U":
        if base2 == "U":
            if base3 == "U" or base3 == "C":
                return "F"
            else:
                return "L"
        elif base2 == "C":
            return "S"
        elif base2 == "A":
            if base3 == "U" or base3 == "C":
                return "Y"
            else:
                return "Stop"
        elif base2 == "G":
            if base3 == "U" or base3 == "C":
                return "C"
            elif base3 == "A":
                return "Stop"
            else:
                return "W"

def RNAToPolypep(mrna_seq: str, del_meth = True) -> str:
    """
    Translates an mRNA sequence into the polypeptide sequence

    Parameters:
    mrna_seq (type: string) - the mrna sequence to be translated
    optional: del_meth (type: bool) - whether or not methianine should be deleted off the protein
    """

    frame1 = ""
    frame2 = ""
    frame3 = ""

    found_start1 = False
    found_start2 = False
    found_start3 = False

    found_stop1 = False
    found_stop2 = False
    found_stop3 = False

    codon = mrna_seq[:3]
    for i in range(2, len(mrna_seq) - 1):
        # define our current reading frame and what codon we're looking at
        current_frame = ((i-2) % 3) + 1
        codon = codon[:2] + codon[i]

        amino_acid = CodonToPeptide(codon)

    # going through frame 1
    if current_frame == 1 and found_stop1 == False:
        # translating as normal
        if found_start1 == True and found_stop1 == False:
            frame1 += amino_acid
        # found first methianine
        elif found_start1 == False and amino_acid == "M":
            found_start1 = True
            frame1 += amino_acid
        # found stop codon
        elif found_start1 == True and amino_acid == "Stop":
            found_stop1 = True

    # going through frame 2
    if current_frame == 2 and found_stop2 == False:
        # translating as normal
        if found_start2 == True and found_stop2 == False:
            frame2 += amino_acid
        # found first methianine
        elif found_start2 == False and amino_acid == "M":
            found_start2 = True
            frame2 += amino_acid
        # found stop codon
        elif found_start2 == True and amino_acid == "Stop":
            found_stop2 = True

    # going through frame 3
    if current_frame == 3 and found_stop3 == False:
        # translating as normal
        if found_start3 == True and found_stop3 == False:
            frame3 += amino_acid
        # found first methianine
        elif found_start3 == False and amino_acid == "M":
            found_start3 = True
            frame3 += amino_acid
        # found stop codon
        elif found_start3 == True and amino_acid == "Stop":
            found_stop3 = True

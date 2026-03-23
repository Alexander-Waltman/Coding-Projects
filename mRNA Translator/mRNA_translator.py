def CodonToPeptide(codon_str: str) -> str:
    """
    Translates a codon into a peptide

    Parameters:
    codon_str (type: string) - 3 characters that make up a codon

    Output:
    (type: string) - the single letter that corresponds to the amino acid/peptide of the input codon
    """

    # input validation
    for char in codon_str:
        if char.upper() not in ["A", "C", "U", "G"]:
            raise ValueError(f"Invalid base inputted into CodonToPeptide: {char}")

    base1 = codon_str[0].upper()
    base2 = codon_str[1].upper()
    base3 = codon_str[2].upper()

    reading_frame1 = ""
    reading_frame2 = ""
    reading_frame3 = ""

    match (base1, base2, base3):
        case("G", "G", _):
            return "G"
        case("G", "A", "G" | "A"):
            return "E"
        case("G", "C", _):
            return "A"
        case("G", "U", _):
            return "V"
        
        case("A", "G", "G" | "A"):
            return "R"
        case("A", "G", "C" | "U"):
            return "S"
        case("A", "A", "G" | "A"):
            return "K"
        case("A", "A", "C" | "U"):
            return "N"
        case("A", "C", _):
            return "T"
        case("A", "U", "G"):
            return "M"
        case("A", "U", "A" | "C" | "U"):
            return "I"
        
        case("C", "G", _):
            return "R"
        case("C", "A", "G" | "A"):
            return "Q"
        case("C", "A", "T" | "U"):
            return "H"
        case("C", "C", _):
            return "P"
        case("C", "U", _):
            return "L"

        case("U", "U", "U" | "C"):
            return "F"
        case("U", "U", "A" | "G"):
            return "L"
        case("U", "C", _):
            return "S"
        case("U", "A", "U" | "C"):
            return "Y"
        case("U", "A", "A" | "G"):
            return "Stop"
        case("U", "G", "U" | "C"):
            return "C"
        case("U", "G", "A"):
            return "Stop"
        case("U", "G", "G"):
            return "W"



def RNAToPolypep(mrna_seq: str, del_meth: bool = True) -> str:
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


example_genotype = "AaBBccDdEE"

def validate_genotype(genotype):
    assert len(genotype) % 2 == 0
    for i in range(0, len(genotype)-1, 2):
        assert genotype[i].lower() == genotype[i+1].lower()


def create_gametes(genotype):
    validate_genotype(genotype)
    

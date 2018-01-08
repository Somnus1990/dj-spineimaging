import datajoint as dj

schema = dj.schema('boazmohar_animal', locals())


@schema
class AnimalSource(dj.Lookup):
    definition = """
    animal_source       : varchar(30)
    """
    contents = zip(['unknown', 'JAX'])


@schema
class Species(dj.Lookup):
    definition = """
    species   : varchar(60)
    """
    contents = zip(['mus musculus'])


@schema
class Strain(dj.Lookup):
    definition = """
    # Mouse strain
    strain              : varchar(30)             # mouse strain
    """
    contents = zip(['Syt17 (NO14)', 'Chrna2 OE25', 'wt'])


@schema
class GeneModification(dj.Lookup):
    definition = """
    gene_modification   : varchar(60)
    """
    contents = zip(['Syt17-cre', 'ACTB-tTa', 'Chrna2-cre', 'CamK2a-tTA', 'TITL-GCaMP6f'])


@schema
class Subject(dj.Manual):
    definition = """
    subject_id          : int                     # institution animal ID
    ---
    -> Species 
    date_of_birth       : date
    date_of_surgery     : date
    sex                 : enum('M','F','Unknown')
    
    ->  [nullable]   AnimalSource
    """

    class GeneModification(dj.Part):
        definition = """
        # Subject gene modifications
        -> Subject
        -> GeneModification
        """

    class Strain(dj.Part):
        definition = """
        -> Subject
        -> Strain
        """

@schema
class WaterRestriction(dj.Manual):
    definition = """
    -> Subject
    water_restriction_number    : varchar(16)   # WR number
    ---
    wr_start_date               : date
    wr_start_weight             : Decimal(2,3)
    """


@schema
class Surgery(dj.Manual):
    definition = """
    -> Subject
    surgery_id          : int                     # surgery number
    ---
    date_of_surgery     : date
    
    """

    class VirusInjection(dj.Part):
        definition = """
        # Subject gene modifications
        -> Surgery
        injection_id : int
        """

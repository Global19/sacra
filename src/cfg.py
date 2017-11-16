# TODO, This needs to be reformatted to be more user friendly
from old_cleaning_functions import *

### Acceptable parameters ###
pathogens = [ 'seasonal_flu' ]
subtypes = { 'seasonal_flu': [ 'h3n2', 'h1n1pdm', 'vic', 'yam' ] }
datatypes = [ 'titer', 'sequence', 'pathogen' ]
filetypes = [ 'fasta' ]

### Cleaning functions for different datatypes ###
# Functions should be defined in cleaning_functions.py
pathogen_clean = []
sequence_clean = [ fix_accession, fix_sequence, fix_locus, fix_strain, remove_isolate_id, fix_passage, fix_submitting_lab, fix_age, determine_passage_category ]

### Mappings used by sacra ###
# Lists sources from which different datatypes come from
sources = { 'sequence' : [ 'gisaid', 'fauna', 'vipr' ],
            'titer' : [ 'crick', 'cdc' ] }
##### strain_sample from https://github.com/nextstrain/sacra/blob/schema/schema/schema_zika.json#L100
# For each sequence source, the default order of fields in the fasta header
fasta_headers = { 'gisaid' : [ 'accession', 'strain', 'isolate_id', 'locus', 'passage', 'submitting_lab' ],
                  'fauna' : [ 'strain', 'pathogen', 'accession', 'collection_date', 'region', 'country', 'division', 'location', 'passage', 'source', 'age' ],
                  'vipr': [ 'accession', 'strain', 'locus', 'date', 'host', 'country', 'subtype', 'pathogen' ] }

metadata_fields = set( [ 'isolate_id', 'subtype', 'submitting_lab', 'passage_history', 'location', 'collection_date' ] )
required_fields = { 'sequence' : { 'strain', 'date', 'accession', 'source', 'locus', 'sequence', 'isolate_id' } }
optional_fields = { 'sequence': { 'strain', 'date', 'passage_category', 'source', 'submitting_lab',
                                  'accession', 'host_age', 'locus', 'sequence', 'isolate_id' } }


### Mappings used by cleaning functions ###
# Used in strain name formatting
strain_fix_fname = { 'seasonal_flu' : 'source-data/flu_strain_name_fix.tsv' }
label_fix_fname = { 'seasonal_flu' : 'source-data/flu_fix_location_label.tsv' }

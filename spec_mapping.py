# When running reshape, figure out which fields belong in which table
# Lifted from schema/schema_zika.json
mapping  = {
    'dbinfo' : ['pathogen'],
    'strain' : [
        'strain_id',
        'strain_name',
        'strain_owner',
        'host_species',
        'host_age',
        'host_sex',
        'symptom_onset_date',
        'symptoms',
        'genotype',
        'pregnancy_status',
        'pregnancy_week',
        'microcephaly_status',
        'usvi_doh_patient_id'
    ],
    'sample' : [
        'sample_id',
        'sample_name',
        'sample_owner',
        'collection_date',
        'country',
        'division',
        'subdivision',
        'gps',
        'collecting_lab',
        'passage',
        'tissue',
        'ct',
        'usvi_doh_sample_id',
        'sample_strain_name'
        'region'
    ],
    'sequence' : [
        'sequence_id',
        'accession',
        'sequence_sample_name',
        'sequence_owner',
        'segment',
        'sequence_type',
        'sequencing_lab',
        'sharing',
        'sequence_url',
        'attribution',
        'sequence',
        'sample_id'
    ],
    'attribution' : [
        'attribution_id',
        'attribution_owner',
        'attribution_source',
        'publication_status',
        'attribution_date',
        'attribution_title',
        'attribution_journal',
        'attribution_url',
        'authors',
        'pubmed_id'
    ]
}

seqrecord2spec = {

}

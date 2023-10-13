def create_data_set():
    mix = ['Mix']
    plant = ['Usinas']

    type_binder = ['Tipo Binder']
    binder = ['Binder']
    performances = ['P.G']
    rap = ['RAP']

    type_binder_additive = ['Tipo Binder Additive']
    binder_additive = ['Binder Additive']
    type_mix_additive = ['Tipo Mix Additive']
    mix_additive = ['Mix Additive']

    gradations = ['Granulometria']
    type_mix = ['Processo Produtivo']
    temperatures = ['Temperaturas']

    aggregate_lime = ['Teor de cal']
    aggregate_portland = ['Cimento Portland']
    aggregate_ras = ['Recycled Asphalt Shingles']
    aggregate_crusher = ['Crusher fines']

    CO2material = ['CO2 - Material']
    CO2transport = ['CO2 - Transporte']
    CO2production = ['CO2 - Produção']
    CO2total = ['CO2 - Total']

    NRPRfuel_mat = ['NRPR Fuel - Material']
    NRPRfuel_tra = ['NRPR Fuel - Transporte']
    NRPRfuel_pro = ['NRPR Fuel - Produção']
    NRPRfuel_total = ['NRPR Fuel - Total']

    NRPRmat_mat = ['NRPR Mat - Material']
    NRPRmat_tra = ['NRPR Mat - Transporte']
    NRPRmat_pro = ['NRPR Mat - Produção']
    NRPRmat_total = ['NRPR Mat - Total']

    SM_mat = ['SM - Material']
    SM_tra = ['SM - Transporte']
    SM_pro = ['SM - Produção']
    SM_total = ['SM - Total']

    urls = ['URLS']

    data_set = [
        mix,
        plant,

        type_binder,
        binder,
        performances,
        rap,

        type_binder_additive,
        binder_additive,
        type_mix_additive,
        mix_additive,

        gradations,
        type_mix,
        temperatures,

        aggregate_lime,
        aggregate_portland,
        aggregate_ras,
        aggregate_crusher,

        CO2material,
        CO2transport,
        CO2production,
        CO2total,

        NRPRfuel_mat,
        NRPRfuel_tra,
        NRPRfuel_pro,
        NRPRfuel_total,

        NRPRmat_mat,
        NRPRmat_tra,
        NRPRmat_pro,
        NRPRmat_total,

        SM_mat,
        SM_tra,
        SM_pro,
        SM_total,

        urls,
    ]

    return data_set

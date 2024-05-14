def clean_cpf_or_cnpj(value) -> str | None:
    if value:
        value =value.replace('.', '').replace('-', '').replace('/', '')
    return value
def clean_cpf_or_cnpj(value) -> str:
    return value.replace('.', '').replace('-', '').replace('/', '')
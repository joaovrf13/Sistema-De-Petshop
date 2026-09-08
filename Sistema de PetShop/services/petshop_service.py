from repositories.dados import Clientes, Pets, Servicos_Disponiveis


def _texto_obrigatorio(valor, campo):
    texto = str(valor or "").strip()
    if not texto:
        raise ValueError(f"O campo {campo} é obrigatório.")
    return texto


def cadastrar_cliente(nome, documento, telefone, endereco):
    nome = _texto_obrigatorio(nome, "nome")
    documento = _texto_obrigatorio(documento, "documento")
    telefone = _texto_obrigatorio(telefone, "telefone")
    endereco = _texto_obrigatorio(endereco, "endereço")

    if any(cliente["Documento"] == documento for cliente in Clientes):
        raise ValueError("Já existe um cliente com esse documento.")

    cliente = {
        "Nome": nome,
        "Documento": documento,
        "Telefone": telefone,
        "Endereco": endereco,
    }
    Clientes.append(cliente)
    return cliente


def cadastrar_pet(documento_dono, nome_pet, tipo_pet, servico_id=None):
    documento_dono = _texto_obrigatorio(documento_dono, "documento")
    nome_pet = _texto_obrigatorio(nome_pet, "nome do pet")
    tipo_pet = _texto_obrigatorio(tipo_pet, "tipo do pet")

    if not any(cliente["Documento"] == documento_dono for cliente in Clientes):
        raise ValueError("Cadastre o responsável antes de cadastrar o pet.")

    if any(
        pet["DocumentoDono"] == documento_dono
        and pet["NomePet"].casefold() == nome_pet.casefold()
        for pet in Pets
    ):
        raise ValueError("Esse pet já está cadastrado para o responsável.")

    servicos = []
    if str(servico_id or "").strip():
        try:
            servico = Servicos_Disponiveis[int(servico_id)]
        except (KeyError, ValueError):
            raise ValueError("Selecione um serviço válido.") from None
        servicos.append(servico.copy())

    pet = {
        "NomePet": nome_pet,
        "TipoPet": tipo_pet,
        "DocumentoDono": documento_dono,
        "Servicos": servicos,
    }
    Pets.append(pet)
    return pet


def cadastrar_cliente_com_pet(
    nome,
    documento,
    telefone,
    endereco,
    nome_pet,
    tipo_pet,
    servico_id=None,
):
    documento_limpo = _texto_obrigatorio(documento, "documento")

    if any(cliente["Documento"] == documento_limpo for cliente in Clientes):
        raise ValueError("Já existe um cliente com esse documento.")

    cliente = cadastrar_cliente(nome, documento_limpo, telefone, endereco)
    try:
        pet = cadastrar_pet(
            documento_limpo,
            nome_pet,
            tipo_pet,
            servico_id,
        )
    except ValueError:
        Clientes.remove(cliente)
        raise

    return cliente, pet


def clientes_com_pets():
    resultado = []
    for cliente in Clientes:
        pets_do_cliente = [
            pet for pet in Pets
            if pet["DocumentoDono"] == cliente["Documento"]
        ]
        resultado.append({**cliente, "Pets": pets_do_cliente})
    return resultado


def obter_resumo():
    faturamento = sum(
        servico["preco"]
        for pet in Pets
        for servico in pet["Servicos"]
    )
    atendimentos = sum(len(pet["Servicos"]) for pet in Pets)

    return {
        "clientes": len(Clientes),
        "pets": len(Pets),
        "atendimentos": atendimentos,
        "faturamento": faturamento,
    }


# Compatibilidade temporária com nomes usados na versão de console.
Cadastrar_Clientes = cadastrar_cliente
Cadastrar_Pets = cadastrar_pet


def Cadastrar_Servicos():
    raise RuntimeError("Use a interface web para registrar serviços.")


def Buscar_Pet():
    raise RuntimeError("Use a busca da interface web.")


def Relatorio():
    return clientes_com_pets()


def Faturamento():
    return obter_resumo()["faturamento"]

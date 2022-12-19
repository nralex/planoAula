'''Criador de Plano de Aula'''
import json



# Abrir JSON com currículo
with open("CB22.json", encoding='utf-8') as documento:
    cb22 = json.load(documento)

# Encontrar objeto do conhecimento desejado
def objeto():
    """Encontra um objeto do conhecimento

    Returns:
        int: número do objeto do conhecimento
    """
    serie = int(input('Insira o Nº da Série: '))
    bimestre = int(input('Insira o Nº da Bimestre: '))
    # Localiza o objeto desejado
    for desejado , i in enumerate(cb22):
        com = cb22[desejado]['COMPONENTE CURRICULAR']
        sem = cb22[desejado]['SÉRIE']
        bim = cb22[desejado]['BIMESTRE']
        if com == 'QUÍMICA' and sem == f'{serie}ª SÉRIE' and bim == f'{bimestre}° BIMESTRE':
            print(f'{desejado} - {i["OBJETO DO CONHECIMENTO"]}')
        else:
            pass
    # Guarda as variáveis escolhidas
    conteudo = int(input('Digite o Nº do Objeto do Conhecimento: '))
    return conteudo


# Formatar página
# Inserir cabeçalho
# Inserir dados
# Formatar dados
# Colocar quebra de página
# Repetir
# TESTE
for n in range(int(input('Nº de Semanas '))):
    aula = objeto()
    print(f'''
COMPONENTE CURRICULAR: {cb22[aula]['COMPONENTE CURRICULAR']}
SÉRIE: {cb22[aula]['SÉRIE']}
BIMESTRE: {cb22[aula]['BIMESTRE']}
OBJETO DO CONHECIMENTO: {cb22[aula]['OBJETO DO CONHECIMENTO']}
UNIDADE TEMÁTICA: {cb22[aula]['UNIDADE TEMÁTICA']}
COMPETENCIA ESPECÍFICA {cb22[aula]['COMPETENCIA ESPECÍFICA']}
HABILIDADE:  {cb22[aula]['HABILIDADE']}
OBJETIVOS DE APRENDIZAGEM: 
{cb22[aula]['OBJETIVOS DE APRENDIZAGEM']}
''')

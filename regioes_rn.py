import csv

# Januário Cicco é boa saúde
agreste = [
    "Bento Fernandes", "Jandaíra", "João Câmara", "Parazinho", "Poço Branco", 
    "Barcelona", "Campo Redondo", "Coronel Ezequiel", "Jaçanã", "Japi", 
    "Lagoa de Velhos", "Lajes Pintadas", "Monte das Gameleiras", "Ruy Barbosa", 
    "Santa Cruz", "São Bento do Trairí", "São José do Campestre", "São Tomé", 
    "Serra de São Bento", "Sítio Novo", "Tangará", "Januário Cicco", "Bom Jesus", 
    "Brejinho", "Ielmo Marinho", "Jundiá", "Lagoa d'Anta", "Lagoa de Pedras", 
    "Lagoa Salgada", "Monte Alegre", "Nova Cruz", "Passa e Fica", "Passagem", 
    "Riachuelo", "Santa Maria", "Santo Antônio", "São Paulo do Potengi", 
    "São Pedro", "Senador Elói de Souza", "Serra Caiada", "Serrinha", "Várzea", 
    "Vera Cruz"
]

leste = [
    "Maxaranguape", "Pedra Grande", "Pureza", "Rio do Fogo", "São Miguel do Gostoso", 
    "Taipu", "Touros", "Ceará-Mirim", "Macaíba", "Nísia Floresta", 
    "São Gonçalo do Amarante", "São José de Mipibu", "Extremoz", "Natal", 
    "Parnamirim", "Arês", "Baía Formosa", "Canguaretama", "Espírito Santo", 
    "Goianinha", "Montanhas", "Pedro Velho", "Senador Georgino Avelino", 
    "Tibau do Sul", "Vila Flor"
]

oeste = [
    "Areia Branca", "Baraúna", "Grossos", "Mossoró", "Serra do Mel", 
    "Tibau", "Apodi", "Caraúbas", "Felipe Guerra", "Governador Dix-Sept Rosado", 
    "Campo Grande", "Janduís", "Messias Targino", "Paraú", "Triunfo Potiguar", 
    "Upanema", "Alto do Rodrigues", "Açu", "Carnaubais", "Ipanguaçu", 
    "Itajá", "Jucurutu", "Pendências", "Porto do Mangue", "São Rafael", 
    "Água Nova", "Coronel João Pessoa", "Doutor Severiano", "Encanto", 
    "Luís Gomes", "Major Sales", "Riacho de Santana", "São Miguel", 
    "Venha-Ver", "Alexandria", "Francisco Dantas", "Itaú", "José da Penha", 
    "Marcelino Vieira", "Paraná", "Pau dos Ferros", "Pilões", "Portalegre", 
    "Rafael Fernandes", "Riacho da Cruz", "Rodolfo Fernandes", "São Francisco do Oeste", 
    "Severiano Melo", "Taboleiro Grande", "Tenente Ananias", "Viçosa", 
    "Almino Afonso", "Antônio Martins", "Frutuoso Gomes", "João Dias", 
    "Lucrécia", "Martins", "Olho d'Água do Borges", "Patu", "Rafael Godeiro", 
    "Serrinha dos Pintos", "Umarizal"
]

central = [
    "Caiçara do Norte", "Galinhos", "Guamaré", "Macau", "São Bento do Norte", 
    "Afonso Bezerra", "Angicos", "Caiçara do Rio do Vento", "Fernando Pedroza", 
    "Jardim de Angicos", "Lajes", "Pedra Preta", "Pedro Avelino", "Bodó", 
    "Cerro Corá", "Florânia", "Lagoa Nova", "Santana do Matos", "São Vicente", 
    "Tenente Laurentino Cruz", "Caicó", "Ipueira", "Jardim de Piranhas", 
    "São Fernando", "São João do Sabugi", "Serra Negra do Norte", 
    "Timbaúba dos Batistas", "Acari", "Carnaúba dos Dantas", "Cruzeta", 
    "Currais Novos", "Equador", "Jardim do Seridó", "Ouro Branco", "Parelhas", 
    "Santana do Seridó", "São José do Seridó"
]

todas = agreste + leste + oeste + central

with open("Ideb municipios RN - 2007.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["cidade"] not in todas:
            print(row["cidade"])
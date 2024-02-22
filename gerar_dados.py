from faker import Faker
from random import choice

fake = Faker('pt_BR')

city = [fake.city() for _ in range(1000)]
names = [fake.name() for _ in range(1000)]
state = [fake.state() for _ in range(26)]


def organizar(lista):
    for x in range(0, len(lista)):
        for y in range(x + 1, len(lista)):
            if lista[x][0] > lista[y][0]:
                z = lista[x]
                lista[x] = lista[y]
                lista[y] = z
    return lista

def nomes(quant=1):
    return organizar([fake.name() for _ in range(quant)]) if quant > 1 else choice(names)

def cidades(quant=1):
    return organizar([fake.city() for _ in range(quant)]) if quant > 1 else choice(city)

def estados(quant=1):
    return organizar([fake.state() for _ in range(quant)]) if quant > 1 else choice(state)

def criar_email(nome):
    provedor = fake.free_email_domain()
    return f"{nome.lower().replace(' ', '_')}@{provedor}"

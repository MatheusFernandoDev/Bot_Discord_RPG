

import discord
import random
import pandas as pd
from discord.ext import commands
from classes import prob_classes

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)




nomes = pd.read_csv("bot/arquivos/nomes_rpg.csv")
nomes_oriental = pd.read_csv("bot/arquivos/nomes_oriental_rpg.csv")
nomes_alemaes = pd.read_csv("bot/arquivos/nomes_alemaes.csv")
nomes_elficos_t = pd.read_csv("bot/arquivos/nomes_elficos_t.csv")
nomes_escocesos = pd.read_csv("bot/arquivos/nomes_escocesos.csv")
nomes_franceses = pd.read_csv("bot/arquivos/nomes_franceses.csv")
nomes_inuites = pd.read_csv("bot/arquivos/nomes_inuites.csv")
nomes_mesopotamicos = pd.read_csv("bot/arquivos/nomes_mesopotamicos.csv")
nomes_polinesios = pd.read_csv("bot/arquivos/nomes_polinesios.csv")
nomes_indiano_rpg = pd.read_csv("bot/arquivos/nomes_indiano_rpg.csv")
nomes_africanos = pd.read_csv("bot/arquivos/nomes_africanos.csv")
nomes_nordicos = pd.read_csv("bot/arquivos/nomes_nordicos.csv")
nomes_italo_continental = pd.read_csv("bot/arquivos/nomes_italo_continental.csv")
nomes_micronesios = pd.read_csv("bot/arquivos/nomes_micronesios.csv")
nomes_celticos = pd.read_csv("bot/arquivos/nomes_celticos.csv")
nomes_amerindios = pd.read_csv("bot/arquivos/nomes_amerindios.csv")
nomes_britanicos = pd.read_csv("bot/arquivos/nomes_britanicos.csv")
nomes_chineses = pd.read_csv("bot/arquivos/nomes_chineses.csv")
nomes_arabes = pd.read_csv("bot/arquivos/nomes_arabes.csv")
nomes_mongolicos = pd.read_csv("bot/arquivos/nomes_mongolicos.csv")
nomes_centro_americanos = pd.read_csv("bot/arquivos/nomes_centro_americanos.csv")
nomes_eslavos = pd.read_csv("bot/arquivos/nomes_eslavos.csv")
nomes_abisal = pd.read_csv("bot/arquivos/nomes_abisal.csv")
nomes_romanos = pd.read_csv("bot/arquivos/nomes_romanos.csv")


@bot.event
async def on_ready():
    print(f"{bot.user} está online")

# Rolagem mercenario
@bot.command()
async def mercenario(ctx):

    # Rolando os atributos
        
    arc =  random.randint(1,8)
    vig =  random.randint(1,8)
    des =  random.randint(1,8)
    sab = random.randint(1,8)
    forç = random.randint(1,8)
    atl = random.randint(1,8)
    eva = random.randint(1,8)
    car = random.randint(1,8)

    racas = [
        "Vampirico", "Arqueonte", "Elfo", "Símio", "Orc", "Magmamir", "Anão", "Voidling", "Troll", "Lupínico","Taurus", "Leonine", "Felínio", "Chacálico", "Javálion", "Reptilio", "Ursárion", "Tritão","Denkomu", "Aládico", "Nivólio", "Humano"
        ]
    
    
    
    raç = random.choice(racas)
    

    if raç == "Vampirico":

        nome = random.choice(nomes_alemaes['Personagem'])

        forç += random.randint(1,3)
        arc += random.randint(1,3) 
        
        # classe preferida = cavaleiro
        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Cavaleiro", maior)
    elif raç == "Arqueonte":
        # variado
        nome = random.choice(nomes['Personagem'])

        sab += random.randint(1,3)
        sab += random.randint(1,3)
        
        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Sentinela", maior)
    elif raç == "Elfo":

        nome = random.choice(nomes_polinesios['Personagem'])

        des += random.randint(1,3)
        sab += random.randint(1,3)
        
        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Sentinela", maior)
    elif raç == "Símio":
        

        nome = random.choice(nomes_indiano_rpg['Personagem'])

        forç += random.randint(1,3)
        des += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Rufião", maior)
    elif raç == "Orc":
        

        nome = random.choice(nomes_africanos['Personagem'])

        forç += random.randint(1,3)
        vig += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Lanceiro", maior)
    elif raç == "Magmamir":
        # A arrumar
        nome = random.choice(nomes['Personagem'])

        arc += random.randint(1,3)
        vig += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Cavaleiro", maior)
    elif raç == "Anão":

        nome = random.choice(nomes_nordicos['Personagem'])

        forç += random.randint(1,3)
        sab += random.randint(1,3)
        
        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Lanceiro", maior)
    elif raç == "Voidling":

        nome = random.choice(nomes_italo_continental['Personagem'])

        eva += random.randint(1,3)
        des += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Ladino", maior)
    elif raç == "Troll":

        nome = random.choice(nomes_micronesios['Personagem'])

        arc += random.randint(1,3)
        arc += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Sentinela", maior)
    elif raç == "Lupínico": 

        nome = random.choice(nomes_celticos['Personagem'])

        atl += random.randint(1,3)
        eva += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Ladino", maior)
    elif raç == "Taurus":

        nome = random.choice(nomes_amerindios['Personagem'])

        atl += random.randint(1,3)
        vig += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Lanceiro", maior)
    elif raç == "Leonine":

        nome = random.choice(nomes_britanicos['Personagem'])

        forç += random.randint(1,3)
        atl += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Cavaleiro", maior)
    elif raç == "Felínio":

        nome = random.choice(nomes_chineses['Personagem'])

        des += random.randint(1,3)
        des += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Ladino", maior)
    elif raç == "Chacálico":

        nome = random.choice(nomes_arabes['Personagem'])

        forç += random.randint(1,3)
        eva += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Sentinela", maior)
    elif raç == "Javálion":

        nome = random.choice(nomes_mongolicos['Personagem'])

        vig += random.randint(1,3)
        vig += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Lanceiro", maior)
    elif raç == "Reptilio":
        

        nome = random.choice(nomes_centro_americanos['Personagem'])

        eva += random.randint(1,3)
        vig += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Ladino", maior)
    elif raç == "Ursárion":

        nome = random.choice(nomes_eslavos['Personagem'])

        forç += random.randint(1,3)
        forç += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Rufião", maior)
    elif raç == "Denkomu":

        nome = random.choice(nomes_abisal['Personagem'])

        des += random.randint(1,3)
        vig += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Cavaleiro", maior)
    elif raç == "Aládico":

        nome = random.choice(nomes_romanos['Personagem'])

        atl += random.randint(1,3)
        atl += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Lanceiro", maior)
    elif raç == "Nivólio":

        nome = random.choice(nomes_abisal['Personagem'])

        eva += random.randint(1,3)
        arc += random.randint(1,3)

        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Sentinela", maior)
    elif raç == "Humano":
        #Variado
        nome = random.choice(nomes['Personagem'])

        arc += 1
        forç += 1
        sab += 1
        eva += 1
        car += 1
        atl += 1
        des += 1
        vig += 1
        
        atributos = {"arc": arc, "vig": vig, "des": des, "sab": sab, "for": forç, "atl": atl, "eva": eva, "car": car}
        maior = max(atributos, key=atributos.get)

        classe = prob_classes("Sentinela", maior)
        
    pc = ((arc+ vig + des + sab + forç + atl + eva + car) / 40)
        
    pesadatorço = ("Brúnea de Bronze do Cavaleiro (d. 15/15- AP) (5/5) slots – extremidades completas com ombreiras (- 3 EVA e -3 DES) 8uP.")

    mediastorço = ("Corselete de Malha (d. 7/7- AM) (4/4) slots. – todo Torso S. e I. (-1 DES); 6uP.")

    levetorço = ["Cota de Anéis (d. 8/8- AL) (4/4) slots – cobre Ombros e todo o Torso I. e S.; 4 uP.", 
                 "Colete de Couro e Peles (d. 5/5- AL) (3/3) slots – Torso S. e I., não protege Ombros; 3 uP."]

    armaduraspesadas = ["Elmo da Guarnição (d. 7/7 – AP) (4/4) slots. – Cabeça completa; visão e percepção reduzidos ((-3) na rolagem de auscultação e (-1) de modificador ocular); 2 uP.", 
    "Botas Metálicas (d. 8/8- AP) (2/2) slots – microrregiões dos pés até joelho; 2uP por pé; 1uP/pé", "Kilt de Bronze Simples (d. 12/12- AP) (3/3) slots – toda a parte inferior até os pés (-1 EVA); 4uP." ]        
        

    porcentagem = 0

    while porcentagem <= 69:

        porcentagem = random.randint(0, 100)
        if porcentagem >= 70 and porcentagem <= 79:
            Proteçao = (random.choice(levetorço))
        if porcentagem >= 80 and porcentagem <= 89:
            Proteçao = mediastorço
        if porcentagem >= 90 and porcentagem <= 94:
            Proteçao = pesadatorço
        if porcentagem >= 95:
            Proteçao = pesadatorço
            Proteçao2 = random.choice(armaduraspesadas)
       
     

    channel = (ctx.channel)
    
    await ctx.message.delete()
    

    await channel.send(f'{ctx.author.mention} \nNome: {nome:<10} Raça: {raç:<10} PC: {pc:.2f} Classe:  {classe}\n'
      f"ARC: {arc:<4} VIG: {vig:<4} DES: {des:<4} SAB: {sab:<4}\n"
      f"FOR: {forç:<4} ATL: {atl:<4} EVA: {eva:<4} CAR: {car:<4}\n"
      f"\nProteção: \n{Proteçao:<4}")
    if porcentagem >= 95:
        await channel.send(f"{Proteçao2}")
       
#  Rolagem Vampirico
@bot.command()
async def vampirico(ctx):   
    
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()

    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Vampirico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Arqueonte
@bot.command()
async def arqueonte(ctx):   

    channel = (ctx.channel)    
    
    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Arqueonte   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Elfo
@bot.command()
async def elfo(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10) + random.randint(1, 6)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()

    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Elfo   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Simio
@bot.command()
async def simio(ctx):   
    
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Símio   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Orc
@bot.command()
async def orc(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Orc   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Magmamir
@bot.command()
async def magmamir(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Magmamir   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Anão
@bot.command()
async def anao(ctx):
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10) + random.randint(1, 6)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Anão   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

#  Rolagem Voidling
@bot.command()
async def voidling(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Voidling   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Troll
@bot.command()
async def troll(ctx):   

    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Troll   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Lupínico
@bot.command()
async def lupinico(ctx):   

    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Lupínico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

#Rolagem Taurus
@bot.command()
async def taurus(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Taurus   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Leonine
@bot.command()
async def leonine(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Leonine   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Felínio
@bot.command()
async def felinio(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    sab = random.randint(1,10) 
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Felínio   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Chacálico
@bot.command()
async def chacalico(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Chacálico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Javálion
@bot.command()
async def javalion(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Javálion   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Reptilio
@bot.command()
async def reptilio(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Repitilio   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Ursárion
@bot.command()
async def ursarion(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()    
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Ursarion   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Tritão
@bot.command()
async def tritao(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Tritão   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Denkomu
@bot.command()
async def denkomu(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10) + random.randint(1, 6)
    des = random.randint(1,10) + random.randint(1, 6)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Denkomu   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Aládico
@bot.command()
async def aladico(ctx):   
   
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10) + random.randint(1, 6) + random.randint(1, 6)
    eva = random.randint(1,10)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Aládico   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Nivólio
@bot.command()
async def nivolio(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + random.randint(1, 6)
    vig = random.randint(1,10)
    des = random.randint(1,10)
    sab = random.randint(1,10)
    forç = random.randint(1,10)
    atl = random.randint(1,10)
    eva = random.randint(1,10) + random.randint(1, 6)
    car = random.randint(1,10)

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Arqueonte   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

# Rolagem Humano
@bot.command()
async def humano(ctx):   
    
    channel = (ctx.channel)

    nome = random.choice(nomes['Personagem'])

    arc = random.randint(1,10) + 1
    vig = random.randint(1,10) + 1
    des = random.randint(1,10) + 1
    sab = random.randint(1,10) + 1
    forç = random.randint(1,10) + 1
    atl = random.randint(1,10) + 1
    eva = random.randint(1,10) + 1
    car = random.randint(1,10) + 1

    pc = (arc + vig + des + sab + forç + atl + eva + car) / 40

    await ctx.message.delete()
        
    await channel.send(f'{ctx.author.mention}  \nNome: {nome}      Raça: Humano   PC: {pc:.2f}\nARC: {arc}  VIG: {vig}  DES: {des}  SAB: {sab}\nFOR: {forç}  ATL: {atl}  EVA: {eva}  CAR: {car}')

bot.run("")
from enum import Enum

class Categories(Enum):
    kobiety = "kobiety"
    bluzki_damskie = f"{kobiety}/bluzki"
    marynarki_damskie = f"{kobiety}/marynarki"
    swetry_damskie = f"{kobiety}/swetry"
    spodnice = f"{kobiety}/spodnice"
    spodnie_damskie = f"{kobiety}/spodnie"
    sukienki = f"{kobiety}/sukienki" # sukienki i kombinezony
    okrycia_damskie = f"{kobiety}/okrycia"
    bielizna_damska = f"{kobiety}/bielizna"
    obuwie_damskie = f"{kobiety}/obuwie"

    mezczyzni = "mezczyzni"
    koszule_meskie = f"{mezczyzni}/koszule"
    marynarki_meskie = f"{mezczyzni}/marynarki"
    swetry_meskie = f"{mezczyzni}/swetry" # Swetry i bluzy
    spodnie_meskie = f"{mezczyzni}/spodnie"
    okrycia_meskie = f"{mezczyzni}/okrycia"
    bielizna_meska = f"{mezczyzni}/bielizna"
    obuwie = f"{mezczyzni}/obuwie"

    dzieci = "dzieci"
    bluzki_dzieciece = f"{dzieci}/bluzki"
    swetry_dzieciece = f"{dzieci}/swetry" # Swetry i bluzy
    spodnice_dzieciece = f"{dzieci}/spodnice"
    spodnie_dzieciece = f"{dzieci}/spodnie" # "Spodnie i kombinezony"
    sukienki_dzieciece = f"{dzieci}/sukienki"
    okrycia_dzieciece = f"{dzieci}/okrycia"
    bielizna_dziecieca = f"{dzieci}/bielizna"
    obuwie_dzieciece = f"{dzieci}/obuwie"

    akcesoria = "akcesoria"
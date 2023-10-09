from uagents import Agent, Context,Bureau
import requests
bureau=Bureau()
from Main.utils import *

Pranetha = Agent(name="Pranetha", seed="Pranetha recovery phrase")

@Pranetha.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "USD", "to": "INR", "q": "1.0"}

    headers = {
        "X-RapidAPI-Key": "2be85388b9msh873d41f7f0cb2c7p127ef4jsn34f1e34ec9c2",
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 81.00)
    ctx.storage.set("min_value", 80.00)
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_Pranetha():
    Pranetha.run()
bureau.add(Pranetha)

abcd = Agent(name="abcd", seed="abcd recovery phrase")

@abcd.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "USD", "to": "INR", "q": "1.0"}

    headers = {
        "X-RapidAPI-Key": "2be85388b9msh873d41f7f0cb2c7p127ef4jsn34f1e34ec9c2",
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 84.00)
    ctx.storage.set("min_value", 82.00)
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_abcd():
    abcd.run()
bureau.add(abcd)

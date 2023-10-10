from uagents import Agent, Context,Bureau
import requests
bureau=Bureau()
from Main.utils import *
from django.conf import settings

a = Agent(name="a", seed="a recovery phrase")

@a.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "SGD", "to": "CAD", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 43.00)
    ctx.storage.set("min_value", 463.00)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("a@gmail.com","Your agent a has found out that the value of SGD has is not in between 463.00CAD and 43.00CAD")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_a():
    a.run()
bureau.add(a)

w = Agent(name="w", seed="w recovery phrase")

@w.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "EUR", "to": "HKD", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 124)
    ctx.storage.set("min_value", 124)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("a@gmail.com","Your agent w has found out that the value of EUR has is not in between 124HKD and 124HKD")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_w():
    w.run()
bureau.add(w)

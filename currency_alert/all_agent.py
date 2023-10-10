from uagents import Agent, Context,Bureau
import requests
bureau=Bureau()
from Main.utils import *
from django.conf import settings

b = Agent(name="b", seed="b recovery phrase")

@b.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "CNH", "to": "HKD", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 90.00)
    ctx.storage.set("min_value", 80.00)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("anuraagbv1@gmail.com","Your agent b has found out that the value of USD has is not in between 80.00INR and 90.00INR")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_b():
    b.run()
bureau.add(b)

wqdg = Agent(name="wqdg", seed="wqdg recovery phrase")

@wqdg.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "CNH", "to": "HKD", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 1245.00)
    ctx.storage.set("min_value", 900.00)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("anuraagbv1@gmail.com","Your agent wqdg has found out that the value of USD has is not in between 900.00INR and 1245.00INR")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_wqdg():
    wqdg.run()
bureau.add(wqdg)

from uagents import Agent, Context,Bureau
import requests
bureau=Bureau()
from Main.utils import *
from django.conf import settings

Pranetha = Agent(name="Pranetha", seed="Pranetha recovery phrase")

@Pranetha.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "AUD", "to": "USD", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 34.00)
    ctx.storage.set("min_value", 23.00)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("qwerty@gmail.com","Your agent Pranetha has found out that the value of AUD has is not in between 23.00USD and 34.00USD")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_Pranetha():
    Pranetha.run()
bureau.add(Pranetha)

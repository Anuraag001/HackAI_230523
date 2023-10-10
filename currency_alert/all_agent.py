from uagents import Agent, Context,Bureau
import requests
bureau=Bureau()
from Main.utils import *
from django.conf import settings

fdas = Agent(name="fdas", seed="fdas recovery phrase")

@fdas.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "AUD", "to": "CNH", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 234324)
    ctx.storage.set("min_value", 5432)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("bangaloreameen@gmail.com","Your agent fdas has found out that the value of AUD has is not in between 5432CNH and 234324CNH")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_fdas():
    fdas.run()
bureau.add(fdas)

fdas = Agent(name="fdas", seed="fdas recovery phrase")

@fdas.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "AUD", "to": "CNH", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 234324)
    ctx.storage.set("min_value", 5432)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("bangaloreameen@gmail.com","Your agent fdas has found out that the value of AUD has is not in between 5432CNH and 234324CNH")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_fdas():
    fdas.run()
bureau.add(fdas)

fdas = Agent(name="fdas", seed="fdas recovery phrase")

@fdas.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "AUD", "to": "CNH", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 234324)
    ctx.storage.set("min_value", 5432)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("bangaloreameen@gmail.com","Your agent fdas has found out that the value of AUD has is not in between 5432CNH and 234324CNH")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_fdas():
    fdas.run()
bureau.add(fdas)

dsf = Agent(name="dsf", seed="dsf recovery phrase")

@dsf.on_interval(period=2.0)
async def say_hello(ctx: Context):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "HKD", "to": "HKD", "q": "1.0"}

    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
    'X-RapidAPI-Host': settings.RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)
    ctx.storage.set("present", response.json())
    ctx.storage.set("max_value", 23425)
    ctx.storage.set("min_value", 43)
    boolean=ctx.storage.get("value") or False
    if ctx.storage.get("present")>ctx.storage.get("max_value") or ctx.storage.get("present")<ctx.storage.get("min_value"):
        ctx.logger.info(f'\033[91mNot in range\033[0m')
        if not boolean:
            agent_mail("bangaloreameen@gmail.com","Your agent dsf has found out that the value of HKD has is not in between 43HKD and 23425HKD")
            ctx.logger.info(f'\033[93mMail sent out of range\033[0m')

            ctx.storage.set("value",True)
            boolean=ctx.storage.get("value")
    else:
        ctx.logger.info(f'\033[94mIn range\033[0m')

def run_dsf():
    dsf.run()
bureau.add(dsf)

from uagents import Agent, Context,Bureau
bureau=Bureau()
Pranetha = Agent(name="Pranetha", seed="Pranetha recovery phrase")

@Pranetha.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')

def run_Pranetha():
    Pranetha.run()
bureau.add(Pranetha)

abcd = Agent(name="abcd", seed="abcd recovery phrase")

@abcd.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')

def run_abcd():
    abcd.run()
bureau.add(abcd)

qwer = Agent(name="qwer", seed="qwer recovery phrase")

@qwer.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')

def run_qwer():
    qwer.run()
bureau.add(qwer)

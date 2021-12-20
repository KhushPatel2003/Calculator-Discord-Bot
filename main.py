import math
from discord.ext import commands
import discord
import random


#Setting the prefix
client = commands.Bot(command_prefix='!', help_command = None)


#Creating functions for basic math expressions (will be easier to use later on)
def sub(x: float, y: float): 
    minus = (x - y)
    return minus

def add(x: float, y: float):
    addition = (x + y)
    return addition 

def mul(x: float, y: float):
    multi = (x * y)
    return multi

def div(x: float, y: float):
    divis = (x / y)
    return divis  

def rand(x: int, y: int):
    randomize = random.randint(x, y)
    return randomize

def sqrt(x: float):
    root = math.sqrt(x)
    return root

def power2(x: float):
    square = (x*x)
    return square

def power3(x: float):
    cube = (x*x*x)
    return cube

def top6(a: float, b: float, c: float, d: float, e: float, f: float):
    average = ((a+b+c+d+e+f)/6)
    return average


#   Using made functions on bot commands, when you do !math_add or any other command in the server, 
#   it will take the inputs and push them through the functions made above.
@client.command()
async def math_add(ctx, x: float, y: float):
    result = add(x, y)
    await ctx.send(result)

@client.command()
async def math_sub(ctx, x: float, y: float):
    result = sub(x, y)
    await ctx.send(result)

@client.command()
async def math_multi(ctx, x: float, y: float):
    result = mul(x, y)
    await ctx.send(result)

@client.command()
async def math_div(ctx, x: float, y: float):
    result = div(x, y)
    await ctx.send(result)

@client.command()
async def math_sqrt(ctx, x: float):
    result = sqrt(x)
    await ctx.send(result)

@client.command()
async def math_random(ctx, x: int, y: int):
    result = rand(x, y)
    await ctx.send(result)

@client.command()
async def math_power2(ctx, x: float):
    result = power2(x)
    await ctx.send(result)

@client.command()
async def math_power3(ctx, x: float):
    result = power3(x)
    await ctx.send(result)

@client.command()
async def math_top6(ctx, a: float, b: float, c: float, d: float, e: float, f: float):
    result = top6(a, b, c, d, e, f)
    await ctx.send(result)


#Bot token to run the code
client.run('your token')

#           THE FINAL COMMANDS
# ADDITION =                !math_add
# SUBTRACTION =             !math_sub
# MULTIPLICATION =          !math_multi
# DIVISION =                !math_div
# SQUARE ROOTING =          !math_sqrt
# PICKING RANDOM NUMBER =   !math_random
# SQUARING =                !math_power2
# CUBING =                  !math_top6
# FIND TOP 6 AVERAGE =      !math_top6
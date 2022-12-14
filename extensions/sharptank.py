import datetime
from random import randint
from random import choice
from ssl import Options
from typing import Optional
from art import text2art

import hikari
import lightbulb
import random

plugin = lightbulb.Plugin('Sharptank')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    pass


# ---ECHO COMMAND---

@plugin.command
@lightbulb.option("text", "text to repeat")
@lightbulb.command("echo", "repeats the given text")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    await ctx.respond(ctx.options.text)

# ---PING COMMAND---

@plugin.command
@lightbulb.command("ping", "🏓 Pong!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f'🏓 Pong! This took {round(plugin.bot.heartbeat_latency * 1000)}ms')


# ---ADDITION COMMAND---

@plugin.command
@lightbulb.option("num2", "number 2", int)
@lightbulb.option("num1", "number 1", int)
@lightbulb.command("add", "Does very complex maths")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


# ---ROLL A DICE COMMAND---
@plugin.command
@lightbulb.command("dice", "Rolls a dice🎲")
@lightbulb.implements(lightbulb.SlashCommand)
async def dice(ctx):
    await ctx.respond(f"U rolled {randint(1, 6)} 🎲")


# ---COINFLIP---

@plugin.command
@lightbulb.command("coinflip", "Flips a coin🪙")
@lightbulb.implements(lightbulb.SlashCommand)
async def coinflip(ctx):
    await ctx.respond(choice(["Heads", "Tails"]))


# ---TEXTART COMMAND---

@plugin.command
@lightbulb.option("text", "enter text to convert into text-art", str)
@lightbulb.command("textart", "converts text into very beautiful art")
@lightbulb.implements(lightbulb.SlashCommand)
async def textart(ctx):
    await ctx.respond(f"```{text2art(ctx.options.text)}```")


# ---EXPONENT COMMAND---
@plugin.command
@lightbulb.option("num2", "exponent ", int)
@lightbulb.option("num1", "base", int)
@lightbulb.command("power", "raises the base number by given power")
@lightbulb.implements(lightbulb.SlashCommand)
async def power(ctx):
    await ctx.respond(ctx.options.num1 ** ctx.options.num2)


# --- QUIZ COMMAND ---

@plugin.command
@lightbulb.command("quiz", "Starts a quiz session")
@lightbulb.implements(lightbulb.SlashCommand)
async def quiz(ctx):
    embed = hikari.Embed(title="Choose subject", color=hikari.Color(0x00FF00))
    embed.add_field(":regional_indicator_p: Physics", "** \n **")
    embed.add_field(":regional_indicator_c: Chemistry", "** \n **")
    embed.add_field(":regional_indicator_m: Maths", "** **")
    res = await ctx.respond(embed)
    msg = await res.message()
    await msg.add_reaction("🇵")
    await msg.add_reaction("🇨")
    await msg.add_reaction("🇲")


# ---USER PRAISE COMMAND ---

praisesentences = [" is op!", " is such a pro!", " is cool!", " is a genius!", " you look so good!"]


@plugin.command
@lightbulb.option("username", "username", hikari.User)
@lightbulb.command("praiseuser", "praises a user")
@lightbulb.implements(lightbulb.SlashCommand)
async def praise(ctx):
    await ctx.respond(f'{ctx.options.username.mention} {random.choice(praisesentences)}')


# ---ASKMODS COMMAND---

@plugin.command
@lightbulb.option("question", "enter the question")
@lightbulb.command("askmods", "ask questions to mods")
@lightbulb.implements(lightbulb.SlashCommand)
async def create_message(ctx):
    await ctx.bot.rest.create_message(952517784896684114,
                                      f'**{ctx.author.mention} says, "{ctx.options.question}"** \n This person needs some help. Dear mods, please give them a lyf.')
    await ctx.respond(f'{ctx.author.mention}, your message was sent. Mods are reviewing it.')


# ------SPAM COMMAND- PLEASE DON'T UNCOMMENT LOL------
# @plugin.command
# @lightbulb.option("spamtext", "what to spam?")
# @lightbulb.option("nrepeat", "number of repetitions", int)
# @lightbulb.command("spam", "spams a username")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def spam(ctx):
#     nrepeat = ctx.options.nrepeat
#     spamtext = ctx.options.spamtext
#     if nrepeat<=20:
#         for i in range(nrepeat):
#             await ctx.respond(f'{spamtext}')
#         await ctx.respond(f'Done :sunglasses:')
#     else:
#         await ctx.respond(f'Lol, it went outta milky way :joy3d:')


# ----CHOOSER COMMAND-----

@plugin.command
@lightbulb.option("choice10", "enter the choice", required=False)
@lightbulb.option("choice9", "enter the choice", required=False)
@lightbulb.option("choice8", "enter the choice", required=False)
@lightbulb.option("choice7", "enter the choice", required=False)
@lightbulb.option("choice6", "enter the choice", required=False)
@lightbulb.option("choice5", "enter the choice", required=False)
@lightbulb.option("choice4", "enter the choice", required=False)
@lightbulb.option("choice3", "enter the choice", required=False)
@lightbulb.option("choice2", "enter the choice")
@lightbulb.option("choice1", "enter the choice")
@lightbulb.command("choose", "get help making a choice")
@lightbulb.implements(lightbulb.SlashCommand)
async def choose(ctx):
    options = [opt for opt in ctx.options._options.values() if opt is not None]
    res = f'Out of\n'
    c = 1
    for opt in options:
        res += f'\n{c}. {opt},'
        c += 1
    ch = random.choice(options)
    i = options.index(ch)
    m = i + 1
    res += f'\n\n{m}. **{ch}** stood out.'

    await ctx.respond(res)


# ---PURGE COMMAND---
# bulk_delete_limit = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=14)
# iterator = (
#     bot.rest.fetch_messages(channel_id)
#     .take_while(lambda message: message.created_at > bulk_delete_limit)
#     .filter(lambda message: ...)
#     .limit(500)  # remember to set a reasonable limit to avoid ratelimits
# ) 
# @plugin.command
# @lightbulb.add_checks(lightbulb.checks.has_roles(974386535266943016, 947448905367433296, 960092506920480768, 1000446934290550814, any))
# @lightbulb.option("number", "number of messages to delete")
# @lightbulb.command("purge", "deletes messages in bulk")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def purge(ctx):
#     async for messages in iterator.chunk(100):
#         await bot.rest.delete_messages(channel_id, messages)

# ---Ban Command---
# @plugin.command
# @lightbulb.option("reason", "Ban reason")
# @lightbulb.option("member", "Member to Ban", type=hikari.Member)
# @lightbulb.command("ban",  "Ban a user")
# @lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
# async def ban(context):
#     hikari.GuildBan(context.options.member, context.options.reason)
#     embed = (hikari.Embed(title=f"Successfully Banned User!")
#     .add_field(f'{context.options.member}', " was successfully banned!")
#     .add_field("Reason", f'{context.options.reason}'))
#     await context.respond(embed)

# ---banned words command---
@plugin.listener(hikari.MessageCreateEvent)
async def delbanwords(event):
    if event.content is not None:
        if 'mai' in event.content.lower() or 'maai' in event.content.lower() or 'maaai' in event.content.lower() or 'maii' in event.content.lower() or 'maaii' in event.content.lower() or 'maaaii' in event.content.lower() or 'maaaiii' in event.content.lower():
            if 'bur' in event.content.lower() or 'boor' in event.content.lower() or 'buur' in event.content.lower() or 'booor' in event.content.lower():
                await event.message.respond(f'Please be polite')
                await event.app.rest.delete_message(event.message.channel_id, event.message.id)
                # member = plugin.bot.cache.get_member(event.guild_id, event.author.id)
                # await member.edit(communication_disabled_until=datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=10, hours=0, weeks=0))



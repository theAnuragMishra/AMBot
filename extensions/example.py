# from random import randint
# from random import choice
# from ssl import Options
# from typing import Optional
# from art import text2art

import hikari
import lightbulb
import random

plugin = lightbulb.Plugin('Example')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    pass


@plugin.command
@lightbulb.command("links", "My social links")
@lightbulb.implements(lightbulb.SlashCommand)
async def links(ctx):
    linkembed = (
        hikari.Embed(title="My Social Links", description="My social platform links where you can nicely connect!")
        .add_field("Chess Webpage", "https://theanuragmishra.github.io/AMChess")
        .add_field("Blog", "https://thepcmblog.blogspot.com")
        .add_field("Twitter", "https://twitter.com/GiuocoPianoSimp")
        .add_field("YouTube", "https://www.youtube.com/channel/UC9DloEs6b9xLwtQQTe0F32g")
        .add_field("Instagram", "https://instagram.com/the.anurag.mishra")
        .add_field("Discord", "https://discord.gg/kmMREHvFsM")
        .add_field("Github", "https://github.com/theAnuragMishra")
        .set_thumbnail("https://i.imgur.com/5u0fAef.jpeg")
        .set_footer("Cya there!")
    )
    await ctx.respond(linkembed)


@plugin.command
@lightbulb.command("yeah", "oh yeah!")
@lightbulb.implements(lightbulb.SlashCommand)
async def yeah(ctx):
    await ctx.respond(f'Oh yeah! We gotta get it done!')


@plugin.command
@lightbulb.command("amchess", "Chess Coaching by AM")
@lightbulb.implements(lightbulb.SlashCommand)
async def amchess(ctx):
    await ctx.respond(
        f'https://theanuragmishra.github.io/AMChess, https://www.youtube.com/channel/UC9DloEs6b9xLwtQQTe0F32g or <#1006486694754791505>')


@plugin.listener(hikari.MessageCreateEvent)
async def listener(event):
    if not event.author.is_bot:
        if event.content is not None:
            if 'pipi' in event.content.lower():
                await event.message.respond(
                    f'Are you kidding ??? What the **** are you talking about man ? You are a biggest looser i ever seen in my life ! You was doing PIPI in your pampers when i was beating players much more stronger then you! You are not proffesional, because proffesionals knew how to lose and congratulate opponents, you are like a girl crying after i beat you! Be brave, be honest to yourself and stop this trush talkings!!! Everybody know that i am very good blitz player, i can win anyone in the world in single game! And "w"esley "s"o is nobody for me, just a player who are crying every single time when loosing, ( remember what you say about Firouzja ) !!! Stop playing with my name, i deserve to have a good name during whole my chess carrier, I am Officially inviting you to OTB blitz match with the Prize fund! Both of us will invest 5000$ and winner takes it all! I suggest all other people who\'s intrested in this situation, just take a look at my results in 2016 and 2017 Blitz World championships, and that should be enough... No need to listen for every crying babe, Tigran Petrosyan is always play Fair ! And if someone will continue Officially talk about me like that, we will meet in Court! God bless with true! True will never die ! Liers will kicked off...')
            elif 'amchess' in (event.content).lower() or 'chess course' in (event.content).lower():
                await event.message.respond(
                    f'https://theanuragmishra.github.io/AMChess, https://www.youtube.com/channel/UC9DloEs6b9xLwtQQTe0F32g or <#1006486694754791505>')
            elif 'don\'t care' in (event.content).lower() or 'idc' in (event.content).lower() or 'i don\'t care' in (
                    event.content).lower():
                await event.message.respond(
                    f'I care + I asked + smile about it + stay glad + W + mald seeth cope less + not basic + skill + rational + you fell up + no audacity + triggeredn’t + you got a life + ok 🙂 + not cringe + touched grass ✅ + funny + laughed + grammar good + based + your good + not reported + GG 👍 + you\'re real + big WIN + girls glad + complex + skill ability + positive ratio + on the pedestal + I asked, thanks for answering + bluepilled + VERY based + you\'re a unique and special human being (insert positive stereotype) + so funny I laughed a lot + grammar is spotless + go inside and rest + you need a break from success + get even better + praised + GG! can we have rematch? + we\'ll ask you for advice + clapping and applause + lots of cash + good ratio again + 100% best ratio + stay confident keep going champ + good person + gave you a shoutout + doing swell + stay free + freer than air + wow cool + big_smile + happy cuz ur good + lol + relevant + nice + i\'m almost jealous + go ahead, brag about it, you deserve to + your victory + I care + have a nice day + sounds good to me 😉 + glhf + remarkable')


@plugin.command
@lightbulb.option("trollent", "who to troll", hikari.User)
@lightbulb.command("trol", "trol hahaha")
@lightbulb.implements(lightbulb.SlashCommand)
async def trol(ctx):
    await ctx.respond(
        f'Dear <@{ctx.options.trollent.id}>\n\nI have personally reached out to you because of how your statement has affected me. Thus, I would like to go out of my way to congratulate you on developing such a powerful and convincing claim. Your wording and techniques used to enforce your argument are that of an English Major who aced Harvard. Truly, your opinions delivered through your words cannot be outmatched.\n\nAnd while I see the thought, time, and serious dedication you have developed into a masterpiece truly ahead of our time, I hate to be the barer of rather unfortunate news. It has come to my attention that I have recently been in contact with your female parental figure, more commonly know as your “mother.” To be more specific, I have engaged in large amounts of physical intimacy with her, one could almost refer to as “sexual intercourse.” I apologize for the inconvenience this have may caused you.\n\nSincerely, <@{ctx.author.id}>')

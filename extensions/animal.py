import random

import hikari
import lightbulb
import asyncio
import requests

plugin = lightbulb.Plugin('animal')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command("fun", "All the entertainment commands you'll ever need!")
@lightbulb.implements(lightbulb.PrefixCommandGroup, lightbulb.SlashCommandGroup)
async def fun_group(ctx: lightbulb.Context) -> None:
    pass  # as slash commands cannot have their top-level command ran, we simply pass here


ANIMALS = {
    "Dog": "🐶",
    "Cat": "🐱",
    # "Panda": "🐼",
    # "Fox": "🦊",
    # "Red Panda": "🐼",
    # "Koala": "🐨",
    # "Bird": "🐦",
    # "Racoon": "🦝",
    # "Kangaroo": "🦘",
    "Others": "🏡"
}


@fun_group.child
@lightbulb.command("animal", "Get a fact + picture of a cute animal :3")
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def animal_subcommand(ctx: lightbulb.Context) -> None:
    select_menu = (
        ctx.bot.rest.build_action_row()
        .add_select_menu("animal_select")
        .set_placeholder("Pick an animal")
    )

    for name, emoji in ANIMALS.items():
        select_menu.add_option(
            name,  # the label, which users see
            name.lower().replace(" ", "_"),  # the value, which is used by us later
        ).set_emoji(emoji).add_to_menu()

    resp = await ctx.respond(
        "Pick an animal from the dropdown :3",
        component=select_menu.add_to_container(),
    )
    msg = await resp.message()

    try:
        event = await ctx.bot.wait_for(
            hikari.InteractionCreateEvent,
            timeout=60,
            predicate=lambda e: isinstance(e.interaction, hikari.ComponentInteraction)
                                and e.interaction.user.id == ctx.author.id
                                and e.interaction.message.id == msg.id
                                and e.interaction.component_type == hikari.ComponentType.SELECT_MENU,
        )
    except asyncio.TimeoutError:
        await msg.edit("The menu timed out :c", components=[])

    else:

        x = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 218, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 463, 561, 520, 521, 522, 523, 524, 525, 526, 527, 530, 498, 419, 440, 449, 450, 444, 494, 495, 496, 497, 499, 420]

        embed = hikari.Embed(colour=0x3B9DFF)
        animal = event.interaction.values[0]
        animal = animal.replace("_", " ")
        if animal.lower() == "cat":
            embed.set_image(f"https://httpcats.com/{random.choice(x)}.jpg")
            await msg.edit(
                f"Here's a {animal} for you! :3", embed=embed, components=[]
            )
        elif animal.lower() == "dog":
            embed.set_image(f"https://http.dog/{random.choice(x)}.jpg")
            await msg.edit(
                f"Here's a {animal} for you! :3", embed=embed, components=[]
            )
        else:
            embed.set_image(f"https://http.garden/{random.choice(x)}.jpg")
            await msg.edit(
                f"Here's something from the garden for you! :3", embed=embed, components=[]
            )

import discord
from discord.ext import commands
import json
from collections import OrderedDict
import asyncio
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= "%", intents = intents)

user_reactions = {}
reaction_lock = asyncio.Lock()  # 添加鎖對象



@bot.command()
async def 目錄(ctx):
    await ctx.send(jdata['menu'], ephemeral=True)

@bot.command()
async def T6主坦(ctx):
    await ctx.send(jdata['T6AVAtank'], ephemeral=True)

@bot.command()
async def T6主奶(ctx):
    await ctx.send(jdata['T6AVAhealm'], ephemeral=True)
                   
@bot.command()
async def T6副奶(ctx):
    await ctx.send(jdata['T6AVAheals'], ephemeral=True)    
                   
@bot.command()
async def T6沉默(ctx):
    await ctx.send(jdata['T6AVAsilence'], ephemeral=True)

@bot.command()
async def T6時停(ctx):
    await ctx.send(jdata['T6AVAarcane'], ephemeral=True)

@bot.command()
async def T6工具(ctx):
    await ctx.send(jdata['T6AVAtool'], ephemeral=True)

@bot.command()
async def T6十字弓(ctx):
    await ctx.send(jdata['T6AVAxbow'], ephemeral=True)

@bot.command()
async def T6火法(ctx):
    await ctx.send(jdata['T6AVAfire'], ephemeral=True)

@bot.command()
async def T6喚影(ctx):
    await ctx.send(jdata['T6AVAcaller'], ephemeral=True)

@bot.command()
async def T6小惡魔(ctx):
    await ctx.send(jdata['T6AVAdevil'], ephemeral=True)

@bot.command()
async def T6冰法(ctx):
    await ctx.send(jdata['T6AVAice'], ephemeral=True)

@bot.command()
async def T8主坦(ctx):
    await ctx.send(jdata['T8AVAtank'], ephemeral=True)

@bot.command()
async def T8主奶(ctx):
    await ctx.send(jdata['T8AVAhealm'], ephemeral=True)
                   
@bot.command()
async def T8副奶(ctx):
    await ctx.send(jdata['T8AVAheals'], ephemeral=True)    
                   
@bot.command()
async def T8沉默(ctx):
    await ctx.send(jdata['T8AVAsilence'], ephemeral=True)

@bot.command()
async def T8時停(ctx):
    await ctx.send(jdata['T8AVAarcane'], ephemeral=True)

@bot.command()
async def T8工具(ctx):
    await ctx.send(jdata['T8AVAtool'], ephemeral=True)

@bot.command()
async def T8十字弓(ctx):
    await ctx.send(jdata['T8AVAxbow'], ephemeral=True)

@bot.command()
async def T8火法(ctx):
    await ctx.send(jdata['T8AVAfire'], ephemeral=True)

@bot.command()
async def T8喚影(ctx):
    await ctx.send(jdata['T8AVAcaller'], ephemeral=True)

@bot.command()
async def T8小惡魔(ctx):
    await ctx.send(jdata['T8AVAdevil'], ephemeral=True)

@bot.command()
async def T8冰法(ctx):
    await ctx.send(jdata['T8AVAice'], ephemeral=True)

@bot.command()
async def 藍洞(ctx):
    responses = ["揪團揪起來", "聽說會出五層金", "裝在手;跟他走"]
    response = random.choice(responses)
    await ctx.send(f"@everyone {ctx.author} 想打藍洞，{response}")

@bot.command()
async def 固藍(ctx):
    responses = ["來陪陪他吧", "但好像有點孤單", "來幾個人一起吧"]
    response = random.choice(responses)
    await ctx.send(f"@everyone {ctx.author} 想打固藍，{response}")

@bot.command()
async def 大媽(ctx):
    responses = ["有人缺專精嗎", "但一個人有點頂不住", "聽說打贏就可以當四皇了"]
    response = random.choice(responses)
    await ctx.send(f"@everyone {ctx.author} 想打大媽，{response}")

@bot.command()
async def 金洞(ctx, date: str, time: str, tier: str):
    # 清空使用者反應字典
    user_reactions.clear()

    # 發送消息並建立 Embed
    await ctx.send(f"@everyone 想開金箱的跟上{ctx.author}的腳步")
    embed = discord.Embed(title="我想開金洞", color=0xfff700)
    embed.add_field(name="日期", value=date, inline=True)
    embed.add_field(name="時間", value=time, inline=True)
    embed.add_field(name="人數", value="10", inline=False)
    embed.add_field(name="難度", value=tier, inline=False)
    embed.add_field(name="主坦", value="none", inline=True)
    embed.add_field(name="主奶", value="none", inline=True)
    embed.add_field(name="副奶", value="none", inline=True)
    embed.add_field(name="沉默", value="none", inline=True)
    embed.add_field(name="時停", value="none", inline=True)
    embed.add_field(name="工具冰", value="none", inline=True)
    embed.add_field(name="十字弩", value="none", inline=True)
    embed.add_field(name="小惡魔", value="none", inline=True)
    embed.add_field(name="火法", value="none", inline=True)
    embed.add_field(name="冰法", value="none", inline=True)
    embed.add_field(name="喚影", value="none", inline=True)
    embed.add_field(name="眼", value="none", inline=False)
    embed.add_field(name="後補席", value="none", inline=False)  # 加入後補席字段
    embed.add_field(name="報名順序", value=" ", inline=False)  # 加入報名順序字段

    # 發送 Embed 並添加反應
    message = await ctx.send(embed=embed)
    reactions = [
        "<:__:1236323284870500415>", "<:__:1236323393629061140>",
        "<:__:1236323491272462356>", "<:__:1236323660697174067>",
        "<:__:1236323731882774580>", "🛠️",
        "<:__:1236323835276689408>", "<:__:1236323922786385951>",
        "<:__:1236324081272619028>", "<:__:1236325141844201572>",
        "<:__:1236324171194306671>", "👁️",
        "❓"  # 加入後補席的 emoji
    ]
    for reaction in reactions:
        await message.add_reaction(reaction)


# 更新 Embed 的函數
async def update_embed(message, embed):
    for field in embed.fields:
        if field.name == "報名順序":
            users_list = field.value.split(", ")
            if "" in users_list:
                users_list.remove("")
            unique_users = list(set(users_list))  # 去除重複的使用者
            ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(unique_users))
            ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
            embed.set_field_at(index=[field.name for field in embed.fields].index("報名順序"), name="報名順序", value=ordered_users_str, inline=False)

    await message.edit(embed=embed)

# 處理使用者添加反應的事件
@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = await bot.fetch_user(payload.user_id)

    if user.bot:
        return

    if payload.user_id in user_reactions:
        await message.remove_reaction(payload.emoji, user)
        return

    embed = message.embeds[0]
    reaction_user = user.display_name

    # 在限制時間內不接受新的反應
    await asyncio.sleep(2)

    reactions_dict = {
        "<:__:1236323284870500415>": ("主坦", 4),
        "<:__:1236323393629061140>": ("主奶", 5),
        "<:__:1236323491272462356>": ("副奶", 6),
        "<:__:1236323660697174067>": ("沉默", 7),
        "<:__:1236323731882774580>": ("時停", 8),
        "🛠️": ("工具冰", 9),
        "<:__:1236323835276689408>": ("十字弩", 10),
        "<:__:1236323922786385951>": ("小惡魔", 11),
        "<:__:1236324081272619028>": ("火法", 12),
        "<:__:1236325141844201572>": ("冰法", 13),
        "<:__:1236324171194306671>": ("喚影", 14),
        "👁️": ("眼", 15),
        "❓": ("後補席", -1)  # 後補席
    }

    if str(payload.emoji) in reactions_dict:
        field_name, field_index = reactions_dict[str(payload.emoji)]
        users_field = embed.fields[field_index]

        if reaction_user in users_field.value:
            await message.remove_reaction(payload.emoji, user)
            return

        if users_field.value == "none":
            users_field.value = reaction_user
        else:
            await message.remove_reaction(payload.emoji, user)

        embed.set_field_at(index=field_index, name=field_name, value=users_field.value, inline=True)

        if field_name == "後補席":  # 檢查是否後補席字段
            await update_embed(message, embed)
            user_reactions[payload.user_id] = True
            return  # 結束處理

        users_list = [field.value for field in embed.fields if field.name == "報名順序"][0].split(", ")
        if "" in users_list:
            users_list.remove("")
        users_list.append(reaction_user)
        ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(users_list))
        ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
        embed.set_field_at(index=[field.name for field in embed.fields].index("報名順序"), name="報名順序", value=ordered_users_str, inline=False)

        await update_embed(message, embed)
        user_reactions[payload.user_id] = True
    elif str(payload.emoji) == "<:__:1236323835276689408>":  # 十字弩的 emoji
        users_field = embed.fields[10]

        if reaction_user in users_field.value:
            await message.remove_reaction(payload.emoji, user)
            return

        if users_field.value == "none":
            users_field.value = reaction_user
        else:
            await message.remove_reaction(payload.emoji, user)

        embed.set_field_at(index=10, name="十字弩", value=users_field.value, inline=True)

        users_list = [field.value for field in embed.fields if field.name == "十字弩順序"][0].split(", ")
        if "" in users_list:
            users_list.remove("")
        users_list.append(reaction_user)
        ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(users_list))
        ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
        embed.set_field_at(index=[field.name for field in embed.fields].index("十字弩順序"), name="十字弩順序", value=ordered_users_str, inline=False)

        await update_embed(message, embed)
        user_reactions[payload.user_id] = True
    elif str(payload.emoji) == "❓":  # 後補席的 emoji
        users_field = embed.fields[-1]

        if reaction_user in users_field.value:
            await message.remove_reaction(payload.emoji, user)
            return

        if users_field.value == "none":
            users_field.value = reaction_user
        else:
            await message.remove_reaction(payload.emoji, user)

        embed.set_field_at(index=len(embed.fields) - 1, name="後補席", value=users_field.value, inline=True)

        users_list = [field.value for field in embed.fields if field.name == "後補席"][0].split(", ")
        if "" in users_list:
            users_list.remove("")
        users_list.append(reaction_user)
        ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(users_list))
        ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
        embed.set_field_at(index=[field.name for field in embed.fields].index("後補席"), name="後補席", value=ordered_users_str, inline=False)

        await update_embed(message, embed)
        user_reactions[payload.user_id] = True

# 處理使用者移除反應的事件
@bot.event
async def on_raw_reaction_remove(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = await bot.fetch_user(payload.user_id)

    if user.bot:
        return

    if payload.user_id in user_reactions:
        del user_reactions[payload.user_id]

    embed = message.embeds[0]
    reaction_user = user.display_name

    reactions_dict = {
        "<:__:1236323284870500415>": ("主坦", 4),
        "<:__:1236323393629061140>": ("主奶", 5),
        "<:__:1236323491272462356>": ("副奶", 6),
        "<:__:1236323660697174067>": ("沉默", 7),
        "<:__:1236323731882774580>": ("時停", 8),
        "🛠️": ("工具冰", 9),
        "<:__:1236323835276689408>": ("十字弩", 10),
        "<:__:1236323922786385951>": ("小惡魔", 11),
        "<:__:1236324081272619028>": ("火法", 12),
        "<:__:1236325141844201572>": ("冰法", 13),
        "<:__:1236324171194306671>": ("喚影", 14),
        "👁️": ("眼", 15),
        "❓": ("後補席", -1)  # 後補席
    }

    if str(payload.emoji) in reactions_dict:
        field_name, field_index = reactions_dict[str(payload.emoji)]
        users_field = embed.fields[field_index]

        if reaction_user in users_field.value:
            users_list = users_field.value.split(", ")
            users_list.remove(reaction_user)
            users_field.value = ", ".join(users_list) if users_list else "none"

            embed.set_field_at(index=field_index, name=field_name, value=users_field.value, inline=True)

            if field_name == "後補席":  # 檢查是否後補席字段
                await message.edit(embed=embed)
                return  # 結束處理

            users_list = [field.value for field in embed.fields if field.name == "報名順序"][0].split(", ")
            if "" in users_list:
                users_list.remove("")
            users_list.remove(reaction_user)
            ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(users_list))
            ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
            embed.set_field_at(index=[field.name for field in embed.fields].index("報名順序"), name="報名順序", value=ordered_users_str, inline=False)

            await message.edit(embed=embed)
    elif str(payload.emoji) == "<:__:1236323835276689408>":  # 十字弩的 emoji
        field_index = 10
        users_field = embed.fields[field_index]

        if reaction_user in users_field.value:
            users_list = users_field.value.split(", ")
            users_list.remove(reaction_user)
            users_field.value = ", ".join(users_list) if users_list else "none"

            embed.set_field_at(index=10, name="十字弩", value=users_field.value, inline=True)

            users_list = [field.value for field in embed.fields if field.name == "十字弩順序"][0].split(", ")
            if "" in users_list:
                users_list.remove("")
            users_list.remove(reaction_user)
            ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(users_list))
            ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
            embed.set_field_at(index=[field.name for field in embed.fields].index("十字弩順序"), name="十字弩順序", value=ordered_users_str, inline=False)

            await message.edit(embed=embed)
    elif str(payload.emoji) == "❓":  # 後補席的 emoji
        users_field = embed.fields[-1]

        if reaction_user in users_field.value:
            users_list = users_field.value.split(", ")
            users_list.remove(reaction_user)
            users_field.value = ", ".join(users_list) if users_list else "none"

            embed.set_field_at(index=len(embed.fields) - 1, name="後補席", value=users_field.value, inline=True)

            users_list = [field.value for field in embed.fields if field.name == "後補席"][0].split(", ")
            if "" in users_list:
                users_list.remove("")
            users_list.remove(reaction_user)
            ordered_users = OrderedDict((user_name, idx + 1) for idx, user_name in enumerate(users_list))
            ordered_users_str = ", ".join(f"{user_name}" for user_name in ordered_users.keys())
            embed.set_field_at(index=[field.name for field in embed.fields].index("後補席"), name="後補席", value=ordered_users_str, inline=False)

            await message.edit(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "%" in message.content:
        # 如果訊息中含有 "%"，則將訊息刪除
        await message.delete()

    await bot.process_commands(message)


bot.run(jdata['token'])
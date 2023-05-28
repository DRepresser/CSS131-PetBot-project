import asyncio
import discord
from discord.ext import commands
from datetime import datetime
import item
from pet import Pet
import database


class Petbot(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.run_date = datetime.now()
        self.item_list = []


    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has connected to Discord!')
        database.create_table()
        item.load_item()


    #Commands
    @commands.command(name='create')
    async def create_pet(self, ctx, name: str, specie: str):
        pet_species = ['Crow', 'Pot', 'Manotham']
        if specie not in pet_species:
            embed = discord.Embed(title=f'{specie} not avaliable', color=0xffc0cb)
            await ctx.send(embed=embed)
            return

        player = database.get_player(ctx.author.id)
        if player is None:
            database.insert_player(ctx.author.id, ctx.author.name)
        if database.get_pet(ctx.author.id) is not None:
            embed = discord.Embed(title='You already have a pet!', color=0xffc0cb)
            await ctx.send(embed=embed)
            return
        pet = Pet(name=name, species=specie, owner_id=player)
        pet.owner_id = ctx.author.id
        pet.birthdate = datetime.now()
        database.insert_pet(pet)
        embed = discord.Embed(title=f'Congratulations {ctx.author.name}, you have a new pet named {pet.name}!')
        await ctx.send(embed=embed)


    @commands.command(name='status')
    async def status(self, ctx):
        pet = database.get_pet(ctx.author.id)
        if pet is None:
            embed = discord.Embed(title='You don\'t have a pet!', color=0xffc0cb)
            await ctx.send(embed=embed)
            return
        database.update_pet(pet)
        embed = discord.Embed(title=f'{pet.name} - Status', description='Your pet\'s current status:', color=0xffc0cb)

        if pet.species == 'Manotham':
            pic = discord.File(f'assets/pet/{pet.species}/defult.gif', filename='defult.gif')
            embed.set_image(url='attachment://defult.gif')
        else:
            pic = discord.File(f'assets/pet/{pet.species}/defult.jpg', filename='defult.jpg')
            embed.set_image(url='attachment://defult.jpg')

        embed.add_field(name='Species', value=pet.species, inline=False)

        hunger = round(pet.hunger, 2)
        energy = round(pet.energy, 2)
        mood = round(pet.mood, 2)
        embed.add_field(name='Hunger', value=hunger, inline=True)
        embed.add_field(name='Energy', value=energy, inline=True)
        embed.add_field(name='Mood', value=mood, inline=True)

        embed.add_field(name='Age', value=pet.age, inline=True)
        birth = pet.birthdate.strftime('%x')
        embed.add_field(name='Birthdate', value=birth, inline=True)
        await ctx.send(file=pic, embed=embed)


    @commands.command(name='feed')
    async def feed(self, ctx, *, name: str):
        player = database.get_player(ctx.author.id)
        pet = database.get_pet(ctx.author.id)

        item_name_list = []
        for item in self.item_list:
            item_name_list.append(item.name)

        if name in item_name_list:
            item_index = item_name_list.index(name)
            re_item = self.item_list[item_index]

            if pet is None:
                embed = discord.Embed(title='You don\'t have a pet!', color=0xffc0cb)
                await ctx.send(embed=embed)
                return

            if player.credits < re_item.cost:
                embed = discord.Embed(title='You don\'t have enough credits to feed your pet!', color=0xffc0cb)
                await ctx.send(embed=embed)
                return
            
            if pet.hunger > 90:
                embed = discord.Embed(title='Your pet is too full to eat more', color=0xffc0cb)
                await ctx.send(embed=embed)
                return
        
            player.credits -= re_item.cost
            pet.feed(re_item)
            database.update_pet(pet)
            database.update_player_credits(ctx.author.id, player.credits)
            embed = discord.Embed(title=f'{pet.name} has been fed! Your balance is now {player.credits} credits.', color=0xffc0cb)
            await ctx.send(embed=embed)

            pet = database.get_pet(ctx.author.id)
            if pet is None:
                embed = discord.Embed(title='You don\'t have a pet!', color=0xffc0cb)
                await ctx.send(embed=embed)
                return
            database.update_pet(pet)
            embed = discord.Embed(title=f'{pet.name} - Status', description='Your pet\'s current status:', color=0xffc0cb)

            if pet.species == 'Manotham':
                pic = discord.File(f'assets/pet/{pet.species}/feed.jpg', filename='feed.jpg')
                embed.set_image(url='attachment://feed.jpg')
            else:
                pic = discord.File(f'assets/pet/{pet.species}/feed.jpg', filename='feed.jpg')
                embed.set_image(url='attachment://feed.jpg')

            embed.add_field(name='Species', value=pet.species, inline=False)

            hunger = round(pet.hunger, 2)
            energy = round(pet.energy, 2)
            mood = round(pet.mood, 2)
            embed.add_field(name='Hunger', value=hunger, inline=True)
            embed.add_field(name='Energy', value=energy, inline=True)
            embed.add_field(name='Mood', value=mood, inline=True)

            embed.add_field(name='Age', value=pet.age, inline=True)
            birth = pet.birthdate.strftime('%x')
            embed.add_field(name='Birthdate', value=birth, inline=True)
            await ctx.send(file=pic, embed=embed)

        else:
            embed = discord.Embed(title='Item not found!', color=0xffc0cb)
            await ctx.send(embed=embed)


    @commands.command(name='balance')
    async def credits(self, ctx):
        player = database.get_player(ctx.author.id)
        if player is None:
            database.insert_player(ctx.author.id, ctx.author.name)
        embed = discord.Embed(title=f'{player.name}, you currently have {player.credits} credits.', color=0xffc0cb)
        await ctx.send(embed=embed)


    @commands.command(name='earn')
    async def getcredit(self, ctx):
        player = database.get_player(ctx.author.id)
        if player is None:
            database.insert_player(ctx.author.id, ctx.author.name)
        player.credits += 10000
        database.update_player_credits(ctx.author.id, player.credits)
        await ctx.send(f'{ctx.author.name}, you currently have {player.credits} credits.')


    @commands.command(name='shop')
    async def shop(self, ctx):
        s = discord.Embed(title='Shop')
        await ctx.send(embed=s)

        if not self.item_list:
            self.item_list = database.random_shop()
        elif (self.run_date - datetime.now()).days >= 1:
            self.item_list = database.random_shop()

        for item in self.item_list:
            embed = discord.Embed(title=f'{item.name}', color=0xffc0cb)
            embed.add_field(name=f'Cost: {item.cost}', value='', inline=False)
            embed.add_field(name=f'Hunger: {item.hunger}', value='', inline=True)
            embed.add_field(name=f'Energy: {item.energy}', value='', inline=True)
            embed.add_field(name=f'Mood: {item.mood}', value='', inline=True)
            pic = discord.File(f'assets/fruit/{item.file}', filename=f'{item.file}')
            embed.set_thumbnail(url=f'attachment://{item.file}')
            await ctx.send(file=pic, embed=embed)


    @commands.command(name='work')
    async def earn(self, ctx, time: float):
        embed = discord.Embed(title=f'{ctx.author.name} has start study for {time} hours.', color=0xffc0cb)
        await ctx.send(embed=embed)
        await asyncio.sleep(time * 60 * 60)

        player = database.get_player(ctx.author.id)
        if player is None:
            database.insert_player(ctx.author.id, ctx.author.name)
        gain = 70 * time
        player.credits += gain
        database.update_player_credits(ctx.author.id, player.credits)
        embed = discord.Embed(title=f'{ctx.author.name} has finish study for {time} hours.', color=0xffc0cb)
        embed.add_field(name=f'{ctx.author.name}, you gain {gain} credits.', value='', inline=False)
        embed.add_field(name=f'{ctx.author.name}, you currently have {player.credits} credits.', value='', inline=False)
        await ctx.send(embed=embed)


    @commands.command(name='play')
    async def play(self, ctx):
        player = database.get_player(ctx.author.id)
        pet = database.get_pet(ctx.author.id)
        if pet is None:
            embed = discord.Embed(title='You don\'t have a pet!', color=0xffc0cb)
            await ctx.send(embed=embed)
            return
        if pet.energy < 30:
            embed = discord.Embed(title='Your pet is very tried and not ready to play with you.', color=0xffc0cb)
            await ctx.send(embed=embed)
            return
        pet.update()
        player.credits -= 40
        pet.hunger -= 10
        pet.energy -= 25
        pet.mood += 10
        pet.update()
        database.update_pet(pet)
        database.update_player_credits(ctx.author.id, player.credits)

        if pet.mood >= 100:
            pet.mood = 100
            embed = discord.Embed(title='', color=0xffc0cb)
            if pet.species == 'Manotham':
                pic = discord.File(f'assets/pet/{pet.species}/play.gif', filename='play.gif')
                embed.set_image(url='attachment://play.gif')
            else:
                pic = discord.File(f'assets/pet/{pet.species}/play.jpg', filename='play.jpg')
                embed.set_image(url='attachment://play.jpg')
        elif pet.mood == 0:
            embed = discord.Embed(title='', color=0xffc0cb)
            if pet.species == 'Manotham':
                pic = discord.File(f'assets/pet/{pet.species}/sad.gif', filename='sad.gif')
                embed.set_image(url='attachment://sad.gif')
            else:
                pic = discord.File(f'assets/pet/{pet.species}/sad.jpg', filename='sad.jpg')
                embed.set_image(url='attachment://sad.jpg')
        else:
            embed = discord.Embed(title='', color=0xffc0cb)
            if pet.species == 'Manotham':
                pic = discord.File(f'assets/pet/{pet.species}/defult.gif', filename='defult.gif')
                embed.set_image(url='attachment://defult.gif')
            else:
                pic = discord.File(f'assets/pet/{pet.species}/defult.jpg', filename='defult.jpg')
                embed.set_image(url='attachment://defult.jpg')
        
        embed.add_field(name='Species', value=pet.species, inline=False)

        hunger = round(pet.hunger, 2)
        energy = round(pet.energy, 2)
        mood = round(pet.mood, 2)
        embed.add_field(name='Hunger', value=hunger, inline=True)
        embed.add_field(name='Energy', value=energy, inline=True)
        embed.add_field(name='Mood', value=mood, inline=True)

        embed.add_field(name='Age', value=pet.age, inline=True)
        birth = pet.birthdate.strftime('%x')
        embed.add_field(name='Birthdate', value=birth, inline=True)
        await ctx.send(file=pic, embed=embed)


    @commands.command(name='release')
    async def release(self, ctx):
        player = database.get_player(ctx.author.id)
        pet = database.get_pet(ctx.author.id)
        if pet is None:
            embed = discord.Embed(title='You don\'t have a pet!', color=0xffc0cb    )
            await ctx.send(embed=embed)
            return

        pet.owner_id = 0
        database.update_pet(pet)
        embed = discord.Embed(title=f'{player.name} pet\'s has been release.', color=0xffc0cb)
        await ctx.send(embed=embed)


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Command List', color=0xffc0cb)
        embed.add_field(name='create', value='Creates your own pet', inline=False)
        embed.add_field(name='status', value='Displays the status of your pet.', inline=False)
        embed.add_field(name='balance', value='Shows your current balance of credits.', inline=False)
        embed.add_field(name='shop', value='Open daily shop.', inline=False)
        embed.add_field(name='feed', value='Feed your pet.', inline=False)
        embed.add_field(name='play', value='Spend 40 credits to play with pet.', inline=False)
        embed.add_field(name='study', value='Study to earn credit.', inline=False)
        embed.add_field(name='release', value='Release your pet.', inline=False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Petbot(client))
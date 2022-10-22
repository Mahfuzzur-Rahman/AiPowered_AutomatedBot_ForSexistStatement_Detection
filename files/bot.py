# Importing modules/libraries
import discord
import main
 
# Creating client instance - this will be used to interact with the Discord API (connection to Discord)
client = discord.Client()
 
# Private token
token = "MTAzMDg4MjMxOTQzMjY5MTc1Mw.Go2wMj.R7Swaq8e1TGJlYCWxJY23jFJ-AaLCzHMaphUdI"
 
 
@client.event
async def on_ready():
   
    print(f"Bot logged in as {client.user}") # Printing the bot's name when it comes online
 
 
@client.event
async def on_message_edit(before, after):
    await  before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content} \n'
        f'After: {after.content} \n'
    )
 
warning_list=[]
exist=False
exist_row=-1
# The on_message event happens when a message gets sent on the server
@client.event
async def on_message(message):
    global warning_list
    global exist
    global exist_row
    if message.author != client.user: # If the message wasn't sent by the bot
       
        #check_msg= bot_help.bot_create(message.content)
        returned_msg = main.main_bot(message.content)
 
        if returned_msg=="Warning":
            for i in range (len(warning_list)):
                if warning_list[i][0] == message.author.id:
                    exist=True
                    exist_row= i
           
            if exist==False:
                warning_list.append([(message.author.id),0])
                exist_row=len(warning_list)-1
                print(f'The user: {message.author} existance in warning list is {exist}. Now, added in row {exist_row} and column 1 with warning count {warning_list[exist_row][1]}.')
 
            else:
                warning_list[exist_row][1]+=1
                print(f'The user: {message.author} existance in warning list is {exist} in row {exist_row} and column 1. Updated with warning count {warning_list[exist_row][1]}.')
 
 
            if warning_list[exist_row][1] < 2:
                await message.add_reaction('\U000026A0') #warning
                print("Warning...") # This will be printed if the bot warns the user
   
            elif warning_list[exist_row][1] >= 2:    
                await message.channel.send("This kind of sexist message should be avoided.") # Print the quation
                print("Deleting...") # This will be printed if the bot deletes a message
                await message.delete() # Deletes the message
               
                #await message.author.ban() # Ban the author from the discord server
                warning_list[exist_row][1]=-1
 
                return
               
        else:
            print("Safe... ") # This will be printed if the bot doesn't delete a message
            return
 
 
 
client.run(token) # Running the bot

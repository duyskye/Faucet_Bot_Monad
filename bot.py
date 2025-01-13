import discord
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv
import json
from web3 import Web3



# Tải biến môi trường từ file .env
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
main_add = os.getenv('main_add') 
main_pk = os.getenv('main_pk') 
# print(bot_token)


### Web3 setup

rpc = 'https://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
web3 = Web3(Web3.HTTPProvider(rpc))
explorer = "https://XXXXXXXXXXXXXXXXXXXXXXXXXXXX/"


def checkStatus(tx_hash):
    # 0 is fail , 1 success
    check = web3.eth.wait_for_transaction_receipt(tx_hash)
    return check['status']

def transfer_eth(sender_address, private_key, receiver_address,  input_eth):
    sender_address = web3.to_checksum_address(sender_address)
    receiver_address = web3.to_checksum_address(receiver_address)

    nonce = web3.eth.get_transaction_count(sender_address)

    value = web3.to_wei(input_eth, 'ether')

    chain_id = web3.eth.chain_id
    gas_price = web3.eth.gas_price


    print(web3.eth.chain_id)
    # Tạo giao dịch
    transaction = {
        'nonce': nonce,
        'to': receiver_address,
        'value': value,
        'gas': 26000,  # Default gas for ETH transfers
        'gasPrice': gas_price,
        'chainId': chain_id,  
    }

    # Sign the transaction with the private key
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

    # Send transaction and get hash
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Đã chuyển ", tx_hash.hex())
    Status = checkStatus(tx_hash)
    if Status == 1:
        sts = 'Successful'
        print(sts)
    else:
        sts = 'Failed'
        print(sts)
    print("====================")

    return tx_hash.hex()





### Discord Setup
# Fixed guild you want the bot to work with
MY_GUILD_ID = 0000000000

# ID of the user allowed to use the bot
AUTHORIZED_USER_ID = 0000000000

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.guild_messages = True
intents.message_content = True  # Allow reading message content

bot = commands.Bot(command_prefix=['!', '/'], intents=intents)


@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng trên guild ID: {MY_GUILD_ID}')


@bot.command(name='ping')
async def ping(ctx):
    # Check if the user does not have permission to call the command

    if ctx.author.id != AUTHORIZED_USER_ID:
        await ctx.send("You do not have permission to use this command.")
        return
    
    if ctx.guild is None:
        await ctx.send("This command can only be used in the specified server (guild).")
    else:
        await ctx.send(f"Pong! Guild: {ctx.guild.name}, Channel: {ctx.channel}, User: {ctx.author}")






@bot.command(name='faucet')
async def faucet(ctx, address: str = None):
    # Check if user does not provide address
    if address is None:
        await ctx.send("Please provide valid wallet address. Ex : `!faucet 0x123456789abcdef`")
        return

    # Check if the user calling the command has the "full access" role
    role_name = "full access"
    member = ctx.author
    has_role = discord.utils.get(member.roles, name=role_name)

    if not has_role:
        await ctx.send(f"You don't has role to faucet.")
        return

    # Đọc dữ liệu từ file JSON
    file_path = "faucet_logs.json"
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Create an empty list if the file does not exist or cannot be read.



    # Find user information
    user_id = member.id
    now = int(datetime.utcnow().timestamp())  # Current time (Unix timestamp)
    user_record = next((entry for entry in data if entry["userId"] == user_id), None)


    if user_record:
        # Users who have used Faucet, check the time
        last_faucet_time = user_record["timeFaucet"]
        elapsed_time = now - last_faucet_time

        if elapsed_time < 86400:  # Less than 24 hours
            remaining_time = 86400 - elapsed_time
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            await ctx.send(
                f"You can't faucet now, try again after {int(hours)} h {int(minutes)} m {int(seconds)} s."
            )
            return

    # Accept faucet
    time_faucet = now
    if user_record:
        # Update time faucet
        user_record["timeFaucet"] = time_faucet
    else:
        # Record new user faucet
        data.append({"userId": user_id, "timeFaucet": time_faucet})

    # Write to file JSON
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


    address = web3.to_checksum_address(address)
    tx_transfer = transfer_eth(main_add, main_pk, address, 0.1)
    await ctx.send(f"Faucet success\nTX: {explorer}tx/{tx_transfer}")

# Run bot with token
bot.run(bot_token)

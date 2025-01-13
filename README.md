# Discord Bot with Web3 Integration

This project is a Discord bot built using Python. It integrates Web3 functionality for interacting with the blockchain, specifically enabling ETH transfers and managing a faucet feature.

---

## Features

### Web3 Functions
- **ETH Transfer**: Send ETH to specified wallet addresses.
- **Transaction Status**: Check the status of blockchain transactions.

### Discord Bot Commands
- `/ping`: Responds with "Pong!" and information about the server, channel, and user.
- `/faucet <wallet_address>`: Allows users to request a fixed amount of ETH once every 24 hours if they have the required role.

---

## Installation

### Prerequisites
- Python 3.8+
- [Web3.py](https://web3py.readthedocs.io/)
- [discord.py](https://discordpy.readthedocs.io/)
- dotenv for environment variable management

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/duyskye/Faucet_Bot_Monad.git
   cd Faucet_Bot_Monad
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following content:
   ```env
   BOT_TOKEN=<your_discord_bot_token>
   main_add=<your_wallet_address>
   main_pk=<your_private_key>
   ```

4. Set up permissions in Discord:
   - Ensure the bot has the necessary permissions to manage roles and read messages.
   - Add the bot to your server using the appropriate OAuth2 URL with the necessary scopes.

5. Run the bot:
   ```bash
   python bot.py
   ```

---

## Configuration

### Environment Variables
- `BOT_TOKEN`: Discord bot token.
- `main_add`: Main wallet address used for ETH transactions.
- `main_pk`: Private key for the wallet address.

### Constants
- `rpc`: RPC URL for the blockchain network.
- `MY_GUILD_ID`: The Discord guild (server) ID where the bot will operate.
- `AUTHORIZED_USER_ID`: Discord user ID with permission to use restricted commands.
- `explorer`: Block explorer base URL for transaction lookup.

---

## Usage

### Commands
#### General
- `/ping`
  - **Description**: Check if the bot is online.
  - **Usage**: `!ping`


#### Faucet
- `/faucet`
  - **Description**: Request a fixed amount of ETH once every 24 hours.
  - **Usage**: `!faucet <wallet_address>`
  - **Restrictions**: Only users with the `full access` role can use this command.

---

## File Structure
```
.
├── bot.py                 # Main bot script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not included in repo)
├── faucet_logs.json       # Faucet usage logs
└── README.md              # Documentation
```

---

## Security Notes
- **Private Keys**: Ensure the `.env` file is not exposed or committed to the repository.
- **Permissions**: Grant the bot only the necessary permissions to function properly.

---

## Dependencies
- [discord.py](https://discordpy.readthedocs.io/)
- [Web3.py](https://web3py.readthedocs.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Feel free to submit issues or pull requests. All contributions are welcome!

---

## Troubleshooting
- **Invalid Wallet Address**: Ensure the wallet address is checksummed before using it.
- **Command Issues**: Verify the bot has the necessary permissions in the Discord server.
- **RPC Issues**: Double-check the RPC URL is valid and accessible.

---

## Contact
For any inquiries or support, contact the repository owner through GitHub.


Telegram : https://t.me/LeLyThiTun


Twitter  : https://x.com/wiza_panda

Discord  : .dskye

## Demo
https://discord.com/channels/1263596865233096714/1323416493383225405/1328405506062159933

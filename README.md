# 🤖 Telegram Wallet Balance Checker Bot

A serverless Telegram bot deployed on Vercel that checks wallet balances for Ethereum Mainnet and Base Network using free public RPC endpoints.

![Bot Status](https://img.shields.io/badge/Bot-Online-brightgreen) ![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black) ![License](https://img.shields.io/badge/License-MIT-blue)

## ✨ Features

- 🟦 **Ethereum Mainnet** - Check ETH balances
- 🔵 **Base Network** - Check ETH balances  
- 🔍 **Multiple Addresses** - Support for comma-separated addresses
- ⚡ **No API Keys** - Uses free public RPC endpoints
- 📊 **Index Numbering** - Numbered results for easy reference
- 🚀 **Serverless** - Deployed on Vercel with auto-scaling
- 💬 **User-Friendly** - Simple command interface

## 🚀 Quick Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/telegram-wallet-bot&env=BOT_TOKEN&envDescription=Your%20Telegram%20bot%20token%20from%20@BotFather)

### 1. Get Your Bot Token
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` and follow instructions
3. Copy your bot token

### 2. Deploy to Vercel
1. Click the "Deploy with Vercel" button above
2. Connect your GitHub account
3. Set the `BOT_TOKEN` environment variable
4. Deploy!

### 3. Set Webhook
After deployment, set your webhook URL:
```bash
curl -F "url=https://your-project.vercel.app/api/webhook" \
     https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook
```

## 📁 Project Structure

```
├── api/
│   ├── webhook.py      # Main bot logic (Vercel function)
│   └── index.py        # Status page handler
├── index.html          # Bot status dashboard
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Usage

1. **Start the bot**: Send `/start` to your bot
2. **Enter addresses**: Paste wallet addresses (single or multiple)
   ```
   Single: 0x742d35Cc6037Cc532831d4f21b72573A6ec5f35f
   Multiple: 0x123..., 0x456..., 0x789...
   ```
3. **Get results**: Receive formatted balance information

### Example Output
```
💰 Wallet Balance Information

#1 🌐 Ethereum Mainnet
📍 Address: 0x742d35...c5f35f
💎 Balance: 1.234567 ETH

#2 🌐 Base Network
📍 Address: 0x742d35...c5f35f
💎 Balance: 0.567890 ETH
```

## 🔧 Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/telegram-wallet-bot.git
   cd telegram-wallet-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variable**:
   ```bash
   export BOT_TOKEN="your_bot_token_here"
   ```

4. **Run locally** (for testing):
   ```bash
   vercel dev
   ```

## 🌐 Status Dashboard

Visit your Vercel URL to see a beautiful status dashboard that shows:
- ✅ Real-time bot status
- 🔗 Direct link to Telegram bot
- 📊 API endpoint information
- 🎨 Responsive design with animations

## 🔒 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your Telegram bot token from @BotFather | ✅ Yes |

## 🛠️ API Endpoints

- `GET /` - Status dashboard (HTML page)
- `GET /api/webhook` - Bot health check (JSON)
- `POST /api/webhook` - Telegram webhook handler

## 🔍 Supported Networks & Addresses

### Networks
- **Ethereum Mainnet** - Native ETH balances
- **Base Network** - Native ETH balances

### Address Format
- Must start with `0x`
- Must be 42 characters long
- Hexadecimal characters only (0-9, a-f, A-F)

## ⚡ Performance & Reliability

- **Serverless Architecture** - Auto-scaling with zero downtime
- **Multiple RPC Endpoints** - Automatic fallback for reliability
- **Error Handling** - Graceful handling of network issues
- **Free Tier Friendly** - Optimized for Vercel's free limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for the Telegram bot framework
- [Vercel](https://vercel.com) for free serverless hosting
- Public RPC providers for free blockchain data access

## 📞 Support

- 🐛 **Bug Reports**: Open an issue on GitHub
- 💡 **Feature Requests**: Open an issue with the "enhancement" label
- 📧 **Contact**: [Your contact information]

---

**Built with ❤️ for the crypto community**
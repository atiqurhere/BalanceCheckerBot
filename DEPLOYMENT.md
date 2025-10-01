# 🚀 GitHub to Vercel Deployment Guide

## Quick Setup (3 steps)

### 1. 📁 Upload to GitHub
1. Create a new repository on GitHub
2. Upload all files from this project
3. Make repository public (for free Vercel deployment)

### 2. 🌐 Deploy to Vercel
1. Go to [vercel.com](https://vercel.com) and sign up
2. Click "New Project" 
3. Import your GitHub repository
4. Set environment variable: `BOT_TOKEN` = your telegram bot token
5. Click "Deploy"

### 3. 🔗 Set Webhook
After deployment, run this command (replace with your details):
```bash
curl -F "url=https://your-project.vercel.app/api/webhook" \
     https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook
```

## ✅ Verify Deployment

1. **Check Status**: Visit your Vercel URL - you should see a beautiful status page
2. **Test Bot**: Message your bot on Telegram with `/start`
3. **Test Balance**: Send a wallet address like `0x742d35Cc6037Cc532831d4f21b72573A6ec5f35f`

## 🔧 Environment Variables

In Vercel dashboard, set these environment variables:
- `BOT_TOKEN`: Your bot token from @BotFather

## 📊 What You'll Get

- **Status Dashboard**: Beautiful webpage showing bot status at your Vercel URL
- **Automatic Scaling**: Handles any number of users
- **Free Hosting**: Vercel free tier is sufficient for this bot
- **Real-time Updates**: Bot responds instantly to messages
- **Health Monitoring**: Built-in status checks and error handling

## 🎯 Bot Features

- ✅ Check Ethereum mainnet balances
- ✅ Check Base network balances  
- ✅ Support multiple addresses (comma-separated)
- ✅ No API keys required (uses free public RPC)
- ✅ Index numbering for results
- ✅ Professional error handling
- ✅ Responsive status dashboard

## 🛠️ Troubleshooting

**Bot not responding?**
- Check webhook is set correctly
- Verify BOT_TOKEN environment variable in Vercel
- Check Vercel function logs

**Status page not loading?**
- Verify deployment succeeded
- Check Vercel project dashboard

**Balance checking fails?**
- RPC endpoints may be temporarily down
- Bot automatically tries backup endpoints
- Check function logs in Vercel dashboard

## 🎉 You're Done!

Your bot is now running 24/7 on Vercel with a professional status page. Share your Vercel URL to show the status dashboard!
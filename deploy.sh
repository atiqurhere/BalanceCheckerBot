#!/bin/bash

# Telegram Wallet Balance Checker Bot - Deployment Script
# This script helps you deploy the bot to Vercel

echo "🤖 Telegram Wallet Balance Checker Bot - Vercel Deployment"
echo "========================================================="

# Check if BOT_TOKEN is provided
if [ -z "$1" ]; then
    echo "❌ Error: Bot token is required!"
    echo ""
    echo "Usage: ./deploy.sh YOUR_BOT_TOKEN"
    echo ""
    echo "To get your bot token:"
    echo "1. Message @BotFather on Telegram"
    echo "2. Send /newbot and follow instructions"
    echo "3. Copy the token and run this script"
    exit 1
fi

BOT_TOKEN=$1

echo "✅ Bot token provided"
echo "📦 Installing Vercel CLI..."

# Install Vercel CLI if not already installed
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm i -g vercel
else
    echo "✅ Vercel CLI already installed"
fi

echo "🚀 Deploying to Vercel..."

# Deploy to Vercel
vercel --prod

echo ""
echo "🔧 Setting up environment variable..."

# Set environment variable
vercel env add BOT_TOKEN production "$BOT_TOKEN"

echo ""
echo "✅ Deployment completed!"
echo ""
echo "Next steps:"
echo "1. Copy your Vercel URL from the deployment output above"
echo "2. Set up webhook with this command:"
echo ""
echo "curl -F \"url=https://YOUR-PROJECT.vercel.app/api/webhook\" \\"
echo "     https://api.telegram.org/bot$BOT_TOKEN/setWebhook"
echo ""
echo "3. Test your bot by messaging it on Telegram"
echo "4. Visit your Vercel URL to see the status dashboard"
echo ""
echo "🎉 Your bot is ready!"
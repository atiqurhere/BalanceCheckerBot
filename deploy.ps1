# Telegram Wallet Balance Checker Bot - Windows Deployment Script

param(
    [Parameter(Mandatory=$true)]
    [string]$BotToken
)

Write-Host "🤖 Telegram Wallet Balance Checker Bot - Vercel Deployment" -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

if ([string]::IsNullOrEmpty($BotToken)) {
    Write-Host "❌ Error: Bot token is required!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Usage: .\deploy.ps1 -BotToken YOUR_BOT_TOKEN"
    Write-Host ""
    Write-Host "To get your bot token:"
    Write-Host "1. Message @BotFather on Telegram"
    Write-Host "2. Send /newbot and follow instructions"
    Write-Host "3. Copy the token and run this script"
    exit 1
}

Write-Host "✅ Bot token provided" -ForegroundColor Green
Write-Host "📦 Checking Vercel CLI..." -ForegroundColor Yellow

# Check if Vercel CLI is installed
try {
    $vercelVersion = vercel --version
    Write-Host "✅ Vercel CLI already installed: $vercelVersion" -ForegroundColor Green
}
catch {
    Write-Host "Installing Vercel CLI..." -ForegroundColor Yellow
    npm i -g vercel
}

Write-Host "🚀 Deploying to Vercel..." -ForegroundColor Cyan

# Deploy to Vercel
vercel --prod

Write-Host ""
Write-Host "🔧 Setting up environment variable..." -ForegroundColor Yellow

# Set environment variable
vercel env add BOT_TOKEN production $BotToken

Write-Host ""
Write-Host "✅ Deployment completed!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Copy your Vercel URL from the deployment output above"
Write-Host "2. Set up webhook with this command:" -ForegroundColor Yellow
Write-Host ""
Write-Host "curl -F `"url=https://YOUR-PROJECT.vercel.app/api/webhook`" \" -ForegroundColor White
Write-Host "     https://api.telegram.org/bot$BotToken/setWebhook" -ForegroundColor White
Write-Host ""
Write-Host "3. Test your bot by messaging it on Telegram"
Write-Host "4. Visit your Vercel URL to see the status dashboard"
Write-Host ""
Write-Host "🎉 Your bot is ready!" -ForegroundColor Green
import telebot
import requests
import json
import re
import os
from typing import List, Dict, Optional

# Bot configuration - Vercel will use environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")

bot = telebot.TeleBot(BOT_TOKEN)

# Public RPC endpoints (no API keys required)
ETHEREUM_RPC_URL = "https://ethereum.publicnode.com"
BASE_RPC_URL = "https://base.publicnode.com"

# Alternative free RPC endpoints (backup options)
ETHEREUM_RPC_BACKUP = "https://rpc.ankr.com/eth"
BASE_RPC_BACKUP = "https://mainnet.base.org"

# User states to track conversation flow
user_states = {}

class UserState:
    WAITING_FOR_ADDRESSES = "waiting_for_addresses"

def is_valid_ethereum_address(address: str) -> bool:
    """Validate Ethereum wallet address format"""
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address.strip()))

def parse_wallet_addresses(text: str) -> List[str]:
    """Parse comma-separated wallet addresses from user input"""
    addresses = [addr.strip() for addr in text.split(',')]
    return [addr for addr in addresses if is_valid_ethereum_address(addr)]

def get_ethereum_balance(address: str) -> Optional[Dict]:
    """Get balance for Ethereum mainnet using RPC"""
    rpc_endpoints = [ETHEREUM_RPC_URL, ETHEREUM_RPC_BACKUP]
    
    for i, rpc_url in enumerate(rpc_endpoints):
        try:
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getBalance",
                "params": [address, "latest"],
                "id": 1
            }
            
            headers = {'Content-Type': 'application/json'}
            response = requests.post(rpc_url, json=payload, headers=headers, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            if 'result' in data and data['result']:
                balance_wei = int(data['result'], 16)
                balance_eth = balance_wei / 10**18
                return {
                    'network': 'Ethereum Mainnet',
                    'address': address,
                    'balance': balance_eth,
                    'symbol': 'ETH'
                }
            elif 'error' in data:
                print(f"RPC Error for Ethereum {address}: {data['error']}")
                continue
                
        except Exception as e:
            print(f"Error with Ethereum RPC {i+1} for {address}: {e}")
            continue
    
    return None

def get_base_balance(address: str) -> Optional[Dict]:
    """Get balance for Base network using RPC"""
    rpc_endpoints = [BASE_RPC_URL, BASE_RPC_BACKUP]
    
    for i, rpc_url in enumerate(rpc_endpoints):
        try:
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getBalance",
                "params": [address, "latest"],
                "id": 1
            }
            
            headers = {'Content-Type': 'application/json'}
            response = requests.post(rpc_url, json=payload, headers=headers, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            if 'result' in data and data['result']:
                balance_wei = int(data['result'], 16)
                balance_eth = balance_wei / 10**18
                return {
                    'network': 'Base Network',
                    'address': address,
                    'balance': balance_eth,
                    'symbol': 'ETH'
                }
            elif 'error' in data:
                print(f"RPC Error for Base {address}: {data['error']}")
                continue
                
        except Exception as e:
            print(f"Error with Base RPC {i+1} for {address}: {e}")
            continue
    
    return None

def format_balance_message(balances: List[Dict]) -> str:
    """Format balance information for display"""
    if not balances:
        return "❌ Unable to fetch balance information for any of the provided addresses."
    
    message = "💰 *Wallet Balance Information*\n\n"
    
    for index, balance_info in enumerate(balances, 1):
        if balance_info:
            message += f"#{index} 🌐 *{balance_info['network']}*\n"
            message += f"📍 Address: `{balance_info['address'][:10]}...{balance_info['address'][-8:]}`\n"
            message += f"💎 Balance: *{balance_info['balance']:.6f} {balance_info['symbol']}*\n\n"
    
    return message

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Handle /start command"""
    user_id = message.from_user.id
    user_states[user_id] = UserState.WAITING_FOR_ADDRESSES
    
    welcome_text = """
🚀 *Welcome to Wallet Balance Checker Bot!*

I can help you check wallet balances on:
• 🟦 Ethereum Mainnet
• 🔵 Base Network

📝 *Supported address format:*
• Single: `0x742d35Cc6037Cc532831d4f21b72573A6ec5f35f`
• Multiple: `address1, address2, address3` (comma-separated)

Enter your wallet address(es) below to get started!
    """
    
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_wallet_addresses(message):
    """Handle wallet address input"""
    user_id = message.from_user.id
    
    if user_id not in user_states or user_states[user_id] != UserState.WAITING_FOR_ADDRESSES:
        bot.reply_to(message, "Please use /start to begin checking wallet balances.")
        return
    
    addresses = parse_wallet_addresses(message.text)
    
    if not addresses:
        bot.reply_to(message, 
            "❌ No valid wallet addresses found. Please ensure your addresses:\n"
            "• Start with '0x'\n"
            "• Are 42 characters long\n"
            "• Contain only hexadecimal characters\n\n"
            "Try again or use /start to restart.")
        return
    
    processing_msg = bot.reply_to(message, f"🔍 Processing {len(addresses)} address(es)...")
    
    try:
        all_balances = []
        failed_addresses = []
        
        for i, address in enumerate(addresses):
            if len(addresses) > 1:
                try:
                    bot.edit_message_text(f"🔍 Processing address {i+1}/{len(addresses)}...",
                                        chat_id=processing_msg.chat.id,
                                        message_id=processing_msg.message_id)
                except:
                    pass
            
            eth_balance = get_ethereum_balance(address)
            base_balance = get_base_balance(address)
            
            if eth_balance:
                all_balances.append(eth_balance)
            if base_balance:
                all_balances.append(base_balance)
            
            if not eth_balance and not base_balance:
                failed_addresses.append(address)
        
        result_message = format_balance_message(all_balances)
        
        if failed_addresses:
            result_message += f"\n⚠️ Could not fetch data for {len(failed_addresses)} address(es) due to network issues."
        
        bot.edit_message_text(result_message, 
                            chat_id=processing_msg.chat.id, 
                            message_id=processing_msg.message_id,
                            parse_mode='Markdown')
        
        user_states[user_id] = UserState.WAITING_FOR_ADDRESSES
        bot.send_message(message.chat.id, 
            "Would you like to check more addresses? Just paste them, or use /start to restart.")
        
    except Exception as e:
        error_msg = f"❌ An error occurred while processing your request.\n\n"
        error_msg += "This might be due to:\n"
        error_msg += "• Network connectivity issues\n"
        error_msg += "• RPC endpoint unavailability\n"
        error_msg += "• Temporary server problems\n\n"
        error_msg += "Please try again in a few moments."
        
        try:
            bot.edit_message_text(error_msg, 
                                chat_id=processing_msg.chat.id, 
                                message_id=processing_msg.message_id)
        except:
            bot.send_message(message.chat.id, error_msg)
            
        print(f"Error in handle_wallet_addresses: {e}")

@bot.message_handler(commands=['help'])
def send_help(message):
    """Handle /help command"""
    help_text = """
🤖 *Wallet Balance Checker Bot Help*

*Commands:*
• `/start` - Start checking wallet balances
• `/help` - Show this help message

*Supported Networks:*
• 🟦 Ethereum Mainnet
• 🔵 Base Network

*Address Format:*
• Must start with `0x`
• Must be 42 characters long
• Example: `0x742d35Cc6037Cc532831d4f21b72573A6ec5f35f`

*Multiple Addresses:*
Separate with commas:
`address1, address2, address3`

*Note:* No API keys required! Uses free public RPC endpoints.
    """
    
    bot.reply_to(message, help_text, parse_mode='Markdown')

# Vercel serverless function handler
from http.server import BaseHTTPRequestHandler
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Handle POST requests from Telegram webhook"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                post_data = self.rfile.read(content_length)
                json_data = json.loads(post_data.decode('utf-8'))
                
                # Process Telegram update
                update = telebot.types.Update.de_json(json_data)
                bot.process_new_updates([update])
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = json.dumps({"ok": True, "status": "processed"})
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_error(400, "No data received")
                
        except Exception as e:
            print(f"Error processing webhook: {str(e)}")
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_response = json.dumps({"error": str(e), "ok": False})
            self.wfile.write(error_response.encode('utf-8'))

    def do_GET(self):
        """Handle GET requests for health check"""
        try:
            bot_info = bot.get_me()
            response_data = {
                "status": "Bot is running",
                "bot_info": "Wallet Balance Checker Bot",
                "bot_username": f"@{bot_info.username}",
                "networks": ["Ethereum Mainnet", "Base Network"],
                "features": [
                    "Multiple wallet addresses support",
                    "No API keys required", 
                    "Free public RPC endpoints",
                    "Real-time balance checking"
                ],
                "endpoints": {
                    "webhook": "/api/webhook (POST)",
                    "status": "/api/webhook (GET)",
                    "dashboard": "/ (GET)"
                }
            }
        except Exception as e:
            response_data = {
                "status": "Bot configuration error",
                "error": str(e),
                "networks": ["Ethereum Mainnet", "Base Network"]
            }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps(response_data)
        self.wfile.write(response.encode('utf-8'))
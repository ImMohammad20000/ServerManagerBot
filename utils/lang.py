from enum import Enum

class KeyboardText(str, Enum):
    Update = '🔄 Update Servers List'
    PowerOn = '🟢 Power On'
    PowerOff = '🔴 Power Off'
    Reboot = '🔄 Reboot'
    ResetPassword = '🔑 Reset Password'
    Delete = '🗑️ Delete'
    Back = '⬅️ Back'
    Confirm = '✅ Confirm'
    Cancel = '❌ Cancel'
    Rebuild = '🔧 Rebuild'
    UpdateServer = '🔄 Update Info'
    Reset = '🔄 Reset'

class MessageText(str, Enum):
    Start = '👋 Welcome to ServerManagerBot\nDevelop and Design by @ErfJabs'
    ServerList = '🖥️ Here are your servers:'
    ServersIsUpdated = '🔄 All servers have been updated!'
    ServerIsUpdated = '✅ Server is updated!'
    ServerInfo = (
        '<b>{status_emoji} Name:</b> <code>{name}</code> [<code>{status}</code>]\n'
        '<b>🔗 IP:</b> <code>{ip}</code> [<code>{country}, {city}</code>]\n'
        '<b>⚙️ Cpu:</b> <code>{cpu} Core</code>\n'
        '<b>🗂️ Ram:</b> <code>{ram} GB</code>\n'
        '<b>🗃️ Disk:</b> <code>{disk} GB</code>\n'
        '<b>🎟️ Image:</b> <code>{image}</code>\n'
        '<b>📅 Created:</b> <code>{created}</code> [<code>{created_day} days ago</code>]\n'
        '<b>🔑 Password:</b> <code>{password}</code>'
    )
    ServerNotFound = '❗ Server not found!'
    TryAgain = '⚠️ Oops! An error occurred, please try again...'
    CheckLogs = '⚠️ Oops! An error occurred, please check the logs.'
    ConfirmAction = 'Are you sure you want to <b>{action}</b> this server?'
    ImagesList = '🖼️ Select your image:'
    Wait = '⏳ Please wait...'

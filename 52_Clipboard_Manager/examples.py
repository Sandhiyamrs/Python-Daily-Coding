from file1_clipboard_manager import ClipboardManager

cb = ClipboardManager()

cb.copy("Important API Key")
print("Clipboard history:", cb.get_history())

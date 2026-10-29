# Spotify Ad Muter (Windows)

A small background tool that automatically mutes the Spotify desktop app while an ad plays and unmutes it when your music returns.

> **Unofficial.** Not affiliated with or endorsed by Spotify. It does not block ads; it only mutes Spotify's audio during them. For personal use. Check Spotify's terms of service yourself.

## How it works

During ads, Spotify's window title is not "Artist - Song" (for example it shows `Listen to music, ad-free.`). The script checks the title every half second. If it matches a known ad title, it mutes Spotify's own audio session through the Windows audio API. Your system volume is never changed, so there is nothing to restore afterwards.

## Requirements

- Windows 10 or 11
- Spotify **desktop app** (not the web player)
- Python 3 from [python.org](https://www.python.org/downloads/) (tick **Add Python to PATH** during install)

## Install

1. Install the libraries:
   ```
   py -m pip install -r requirements.txt
   ```
2. Test it in a console:
   ```
   py spotify_mute.py
   ```
   Play Spotify. The console prints a `Title:` line each time the title changes. Pausing should mute Spotify, and playing should unmute it.

## Run automatically at startup

1. Press `Win + R`, type `shell:startup`, press Enter.
2. Copy `spotify_mute.py` into that folder.
3. Rename the copy to `spotify_mute.pyw` (the `.pyw` ending runs it with no console window). Turn on **View > File name extensions** in File Explorer if you can't see the ending.
4. Double-click it once to start it now. It will start with Windows from then on.

To stop it, open Task Manager (`Ctrl + Shift + Esc`) and end the **Python** process.

## If an ad is not muted

Ad titles can vary. Run `py spotify_mute.py` in a console, wait for an ad, and read the last `Title:` line. Add that text, in lowercase, to `AD_TITLES` at the top of the script.

This version is tested with English-language Spotify only.

## Limitations

- Windows only. A macOS version is planned.
- Pausing Spotify also mutes it (the paused title matches), which is harmless.
- Relies on Spotify's window titles, which Spotify may change.

## License

MIT

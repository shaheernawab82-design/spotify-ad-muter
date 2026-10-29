"""Spotify Ad Muter (Windows)

Watches the Spotify desktop app's window title. During ads the title is
not "Artist - Song", so the script mutes Spotify, then unmutes it when a
real song starts. Only Spotify is muted; your system volume is untouched.
"""
import time

import psutil
import win32gui
import win32process
from pycaw.pycaw import AudioUtilities

# Window titles (lowercase) that mean "an ad is playing, or nothing is".
# If an ad slips through, run spotify_mute.py in a console, read the
# "Title:" line it prints during the ad, and add it here in lowercase.
AD_TITLES = {
    "advertisement",
    "spotify",
    "spotify free",
    "listen to music, ad-free.",
}

CHECK_INTERVAL = 0.5  # seconds between checks


def spotify_title():
    """Return the title of Spotify's main window, or "" if not open."""
    found = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                if psutil.Process(pid).name().lower() == "spotify.exe":
                    title = win32gui.GetWindowText(hwnd)
                    if title:
                        found.append(title)
            except psutil.Error:
                pass

    win32gui.EnumWindows(callback, None)
    return found[0] if found else ""


def set_mute(muted):
    """Mute or unmute only Spotify's audio session."""
    for session in AudioUtilities.GetAllSessions():
        if session.Process and session.Process.name().lower() == "spotify.exe":
            session.SimpleAudioVolume.SetMute(muted, None)


def main():
    last_title = None
    while True:
        try:
            title = spotify_title()
            if title != last_title:
                print("Title:", title)  # visible only when run with python
                last_title = title
            set_mute(title.lower() in AD_TITLES)
        except Exception as error:
            print("Error:", error)
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()

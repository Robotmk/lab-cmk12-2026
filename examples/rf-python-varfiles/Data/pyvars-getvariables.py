chrome = {
    'BROWSER': 'chrome',
    'HEADLESS': False,
    'WINDOW_WIDTH': 1920,
    'WINDOW_HEIGHT': 1080,
    'LIST__DOWNLOAD_DIRS': ['/tmp/chrome-downloads', '/tmp/chrome-cache'],
}

firefox = {
    'BROWSER': 'firefox',
    'HEADLESS': True,
    'WINDOW_WIDTH': 1280,
    'WINDOW_HEIGHT': 800,
    'LIST__DOWNLOAD_DIRS': ['/tmp/firefox-downloads', '/tmp/firefox-cache'],
}

def get_variables(browser):
    """Return browser-specific configuration variables.

    Usage in suite:  Variables  Data/pyvars-getvariables.py  chrome
                     Variables  Data/pyvars-getvariables.py  firefox
    """
    profiles = {'chrome': chrome, 'firefox': firefox}
    if browser not in profiles:
        raise ValueError(f"Unknown browser '{browser}'. Choose from: {list(profiles)}")
    return profiles[browser]
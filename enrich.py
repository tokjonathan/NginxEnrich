from user_agents import parse


# Add browser, OS and device based on user_agent in entry
def enrich_user_agent(entry_dict) -> dict:
    ua_string = entry_dict.get("user_agent", "")
    ua = parse(ua_string)

    # Browser information (e.g. Mobile Safari, 5.1)
    entry_dict["browser"] = ua.browser.family or "Unknown"
    entry_dict["browser_version"] = ua.browser.version_string or []

    # Operating Sys information (e.g. IOS 5.1)
    entry_dict["os"] = ua.os.family or "Unknown"
    entry_dict["os_version"] = ua.os.version_string or []

    # Device used (e.g. Galaxy Samsung)
    entry_dict["device"] = ua.device.family or "Unknown"
    entry_dict["device_brand"] = ua.device.brand or "Unknown"

    # Popular device/platform identifiers
    entry_dict["is_mobile"] = ua.is_mobile
    entry_dict["is_tablet"] = ua.is_tablet
    entry_dict["is_pc"] = ua.is_pc
    entry_dict["is_bot"] = ua.is_bot

    return entry_dict



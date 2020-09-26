from datetime import datetime
import pytz


def area(location):
    location = format_location(location)
    for areas in pytz.all_timezones:
        if location.lower() in areas.lower():
            location = areas
            tz = pytz.timezone(location)
            date_now = datetime.now(tz)
            formatted_date = date_now.strftime("%B %d, %Y %H:%M:%S")
            print(f"{location} time: ", formatted_date)
            break

    else:
        print("This location isn't on the tz database on Wikipedia")


def area_zone(zone):
    try:
        zone = daylight_saving(zone)
        tz = pytz.timezone(zone)
        date_now = datetime.now(tz)
        formatted_date = date_now.strftime("%B %d, %Y %H:%M:%S")
        print(f"{zone} time: ", formatted_date)

    except Exception:
        print("Timezone is not on the list. Consider using location instead.")


def daylight_saving(zone):
    """This function is used to handle situations of Daylight Saving Time that the standard library can't recognize."""
    if zone == "PDT":
        return "PST8PDT"
    if zone == "MDT":
        return "MST7MDT"
    if zone == "EDT":
        return "EST5EDT"
    if zone == "CDT":
        return "CST6CDT"
    if zone == "WAT":
        return "Etc/GMT+1"

    return zone


def format_location(location):
    location = location.replace(" ", "_")
    return location

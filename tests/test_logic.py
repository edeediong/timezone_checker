# import subprocess
# import pytz

# from src.logic import area, area_zone, timezones, format_location


# def capture(command):
#     proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
#     out, err = proc.communicate()
#     return out, err, proc.returncode


# def test_timezones():
#     assert timezones("PDT") == "PST8PDT"
#     assert timezones("WAT") == "Etc/GMT+1"
#     assert timezones("CDT") == "CST6CDT"
#     assert timezones("HST") == "HST"


# def test_format_location():
#     assert format_location("Pago Pago") == "Pago_Pago"
#     assert format_location("New York") == "New_York"
#     assert format_location("St Helena") == "St_Helena"


# def test_area():
#     command = ["python", "src/main.py", "--location", "New York"]
#     out, err, exitcode = capture(command)
#     assert exitcode == 0
#     assert out == area("New York")
#     assert err == b""

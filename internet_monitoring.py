import speedtest
import datetime
import subprocess
import platform
#

class colors:
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'


def speed_ul_dl(time_now):
    speed = speedtest.Speedtest()
    download = speed.download()
    upload = speed.upload()
    download, upload = megabits_pet_sec(download, upload,time_now)
    return download, upload

def get_time():
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    return time_now

def megabits_pet_sec(download, upload, time_now):
    downspeed = (round(download / 1048576),2)
    upspeed = (round(upload / 1048576), 2)
    downspeed = downspeed[0]
    upspeed = upspeed[0]
    print(f"Time: {time_now}, Downspeed: {downspeed} Mb/s, Upspeed: {upspeed} Mb/s")
    return (downspeed,upspeed)

def ping():
    speed = speedtest.Speedtest()
    speed.get_best_server()

    operating_sys = platform.system()
    ip = '192.168.1.1'
    ping_command = ['ping', ip, '-n', '1'] if operating_sys == 'Windows' else ['ping', ip, '-c 1']
    shell_needed = True if operating_sys == 'Windows' else False

    ping_output = subprocess.run(ping_command,shell=shell_needed,stdout=subprocess.PIPE)
    success = ping_output.returncode

    # and then check the response...
    if success == 0:
        print(colors.blue + "Connect To Router" + colors.reset)
        ping = speed.results.ping
        print(f"{ping} ms")
    else:
        print(colors.red + "Internet Error"+ colors.reset)



if __name__ == "__main__":

    while True:
        sever = ping()
        try:
            print(colors.yellow + "------------------------Internet speed test has started--------------------------------" + colors.reset)
            time_now = get_time()
            download, upload = speed_ul_dl(time_now)
        except:
            print(colors.red + "Error"+ colors.reset)




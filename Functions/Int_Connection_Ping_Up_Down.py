import speedtest

myst= speedtest.Speedtest()

user_option=int(input('''What would you like to know:
    1) upload
    2) download
    3) ping '''))

if user_option == 1:
    print(myst.upload())
elif user_option == 2:
    print(myst.download())
elif user_option == 3:
    #defining the server
    aserver=[]
    myst.get_servers(aserver)
    print(myst.results.ping)
else:
    print("Invalid Selection")

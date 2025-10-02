a = str(input("Open sesame ? : "))

match a:
    case 'open sesame':
        print('access granted')
    case 'will you open, you goddamn !@&/°':
        print('access fucking granted')
    case _:
        print('permission denied')
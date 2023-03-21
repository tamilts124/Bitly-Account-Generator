import requests, optparse

parser =optparse.OptionParser()

def help():
    parser.add_option('-u', '--username', dest='username', type='string', help='Account Username [Required]')
    parser.add_option('-p', '--password', dest='password', type='string', help='Account Password [Required]')
    parser.add_option('-e', '--email', dest='email', type='string', help='Email id For Account [Required]')

def find_all():
    if option.username and option.password and option.email:return True
    else:return False

def request_resourse(url, data={}, headers={}, method='GET', cookies={}):
    if method.upper()=='POST': response =requests.post(url, data=data, headers=headers, cookies=cookies)
    else: response =requests.get(url, data=data, headers=headers, cookies=cookies)
    return response

def create_account(username, password, email):
    _xsrf =request_resourse('https://bitly.com/').cookies['_xsrf']
    account_result =request_resourse('https://bitly.com/a/sign_up', {'username':username, 'email':email, 'password':password}, {'X-Xsrftoken':_xsrf, 'X-Requested-With':'XMLHttpRequest', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}, 'POST', {'_xsrf':_xsrf})
    return account_result.json()

def Main():
    global option
    option =parser.parse_args()[0]
    if not find_all():parser.print_help();return
    print()
    account =create_account(option.username, option.password, option.email)
    if account['status_txt']=='OK':print(' Account Created, Success!')
    else:
        for error in account['data']['errors']:print(f"> {error}: {account['data']['errors'][error]}")

if __name__ == '__main__':
    help();Main()
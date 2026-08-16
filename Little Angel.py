import httpx

print("="*60)
print('Little Angel is a shy and kind servant who lives to help you')
print("="*60)
print('\nYes.Come here,please')
print('No.Not now,sorry...')

while(True):

    ask= (input("\nCall Little Angel?: "))
  

    if ask.lower() == 'yes':
        url= input("\nLittle Angel asks for your petition: ").strip()

        if not url.startswith(("http://","https://")):
            url= f"https://{url}"

        with httpx.Client(follow_redirects=True, timeout=5.0) as client:
            try:
                response= client.get(url)
                print("Little Angel is giving you what you want!!\n")
                print(f"Status: {response.status_code}")
                print(f"Forwarded: {response.headers.get('x-forwarded-for','Sorry...')}")
                print(f"Referer: {response.headers.get('referer','Sorry...')}")
                print(f"Technology(X-Generator): {response.headers.get('x-generator', 'Sorry...')}")
                print(f"WAF(Server): {response.headers.get('server','Sorry...')}")
                print(f"XSS protection: {response.headers.get('x-xss-protection','Sorry...')}")

            
            except httpx.RequestError:
                print('Sorry,your URL is not valid or reachable...')

    elif ask.lower() == 'no':
        print("Bye!!")
        break

    else:
        print("Tell me Yes or No!")


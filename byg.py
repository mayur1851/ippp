import requests,threading
import random,time,base64
from concurrent.futures import ThreadPoolExecutor
use ="qwertyuiopazsdfgjxnczkznha"
file = 'tokenss1.txt'#input('Enter Your Idlist : ')
yourpk = '52730695704'#input("Enter Your Userid : ")
youruser = 'gamer_ka_id'#input("Enter Your UserName : ")
ko = 0
def ashu(Lo):
			X = Lo.split(':')[1]
			tokens = Lo.split(':')[0]
	
			user = str("".join(random.choice(use)for i in range(8)))
			
			try:
				message2 = user
				message_bytes2 = message2.encode('ascii')
				base64_bytes2 = base64.b64encode(message_bytes2)
				base64_message2= base64_bytes2.decode('ascii')
				print('\n'+X)
				print('NamasteHackers')
				re = requests.post(f"https://hash.mayur690018.repl.co?usname={user}&usid={X}&submit=submit").text
			#print(re)
#print(re)
				uns = re.split('un:')[1]
				un = uns.split(':un')[0]
			#print(un)
#print(un)
				uhlogin = re.split('uhlogin:')[1]
				uhlog = uhlogin.split(':uhlogin')[0]
			#print(uhlog)


				keys = re.split('key:')[1]
				key = keys.split(':key')[0]
			#print(key)

#print(key)


				uhs = re.split('uh:')[1]
				uh = uhs.split(':uh')[0]

#print(uh)

				ahs= re.split('ah:')[1]
				ah = ahs.split(':ah')[0]

#print(ah)

				aks= re.split('ak:')[1]
				ak = aks.split(':ak')[0]

#print(ak)

				uis= re.split('ui:')[1]
				ui = uis.split(':ui')[0]
			#print(ui)

#print(ak)
#________--_____________-________________
				un1= re.split('un1:')[1]
				un1 = un1.split(':un1')[0]

#print(un1)

				uh1= re.split('uh1:')[1]
				uh1 = uh1.split(':uh1')[0]
#print(uh1)

				ak1= re.split('ak1:')[1]
				ak1 = ak1.split(':ak1')[0]
#print(ak1)

				ah1= re.split('ah1:')[1]
				ah1 = ah1.split(':ah1')[0]
#print(ah1)
				un2= re.split('un2:')[1]
				un2 = un2.split(':un')[0]
	#print(un2)
				ah2= re.split('ah2:')[1]
				ah2 = ah2.split(':ah2')[0]
	#print(ah2)
				ak2= re.split('ak2:')[1]
				ak2 = ak2.split(':ak2')[0]
	#print(ak2)
			except  :
				pass
			try:
				headers = {
    'Host': 'asiafollower.com',
    'token': tokens,
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '830',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}
				data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un1+"\u003d",
  "u_h": uh,
  "a_h": ah1+"\u003d",
  "a_k": ak1+"\u003d",
  "username": 'hdjdjd'
}
				res = requests.post('https://asiafollower.com/api/v5/getUserInfo', headers=headers,json=data).text
			#print(res)
				ccs = res.split('"follow_coin":')[1]
				cccs = ccs.split(',')[0]
			
				print('follow coin ' +cccs)
			
				ors = int(cccs)//2
				if int(cccs)>400:
					idjj = '52705887246','52705887247','52705887248','52705887249','52705887250','52705887251','52705887252','52705887253','52705887254','52705887255','52705887256','52705887257','52705887258','52705887259','52705887269','52705887261','52705887262','52705887263','52705887264','52705887265','52705887266','52705887267','52705887268','52705887269','52705887270','52705887271','52705887272','52705887273','52705887274','52705887275','52705887276','52705887277','52705887278','52705887279','52705887280','52705887281','52705887282','52705887283','52705887284','52705887285','52705887286','52705887287','52705887288','52705887289','52705887290',
					
					nices = random.choice(idjj)
					data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un2+"\u003d",
  "u_h": uh+"\u003d",
  "a_h": ah2+"\u003d",
  "a_k": ak2+"\u003d",
  "coin": str(cccs),
  "coin_type": "follow",
  "target_id": nices
}
					resm= requests.post('https://asiafollower.com/api/v5/transferCoin', headers=headers,json=data).text
					
					print(resm)
					if '{"id"' in resm:
						#to = ok + cccs
						print(resm)
						#print(to)
						time.sleep(00)
						
					
						
						
					else:
						
						if '{"id"' in resm:
							print(resm)
							time.sleep(0)
							#to= ok + ccs
							#print(to)
						
				else:
					print('lowCoins')
					print(to)
				
			
			except  :
				pass
file = 'tokenss1.txt'#input(f"Enter Proxy List : ")
combos = open(file).read().splitlines()
def main():
    while True:
    	with ThreadPoolExecutor(max_workers=20) as executor:
        	futures = [executor.submit(ashu, Lo) for Lo in combos]
        	executor.shutdown(wait=True)
	
if __name__ == '__main__':
    main()
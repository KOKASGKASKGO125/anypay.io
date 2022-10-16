import requests
import hashlib
import json

API_ID = ""
API_KEY = ""

def getBalance():
	sign = hashlib.sha256(f'balance{API_ID}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/balance/{API_ID}", params={"sign":sign.hexdigest()})
	return responce.text

def getRates():
	sign = hashlib.sha256(f'rates{API_ID}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/rates/{API_ID}", params={"sign":sign.hexdigest()})
	return responce.text

def getCommissions(project_id):
	sign = hashlib.sha256(f'commissions{API_ID}{project_id}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/commissions/{API_ID}?project_id={project_id}", params={"sign":sign.hexdigest()})
	return responce.text

def getCreatePayment(project_id,pay_id,amount,currency,desc,method,email):
	sign = hashlib.sha256(f'create-payment{API_ID}{project_id}{pay_id}{amount}{currency}{desc}{method}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/create-payment/{API_ID}?project_id={project_id}&pay_id={pay_id}&amount={amount}&currency={currency}&desc={desc}&method={method}&email={email}", params={"sign":sign.hexdigest()})
	return responce.text

def getPayments(project_id):
	sign = hashlib.sha256(f'payments{API_ID}{project_id}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/payments/{API_ID}?project_id={project_id}", params={"sign":sign.hexdigest()})
	return responce.text

def getPayout(payout_id,payout_type,amount,wallet):
	sign = hashlib.sha256(f'create-payout{API_ID}{payout_id}{payout_type}{amount}{wallet}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/create-payout/{API_ID}?payout_id={payout_id}&payout_type={payout_type}&amount={amount}&wallet={wallet}", params={"sign":sign.hexdigest()})
	return responce.text

def getPayouts():
	sign = hashlib.sha256(f'payouts{API_ID}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/payouts/{API_ID}", params={"sign":sign.hexdigest()})
	return responce.text

def getIpNotification():
	sign = hashlib.sha256(f'ip-notification{API_ID}{API_KEY}'.encode())
	responce = requests.get(f"https://anypay.io/api/ip-notification/{API_ID}", params={"sign":sign.hexdigest()})
	return responce.text	

def checkPay(project_id,comment):
	
	json_dump = json.loads(getPayments(project_id))
	current_pay = json_dump["result"]["payments"]

	for i in current_pay:
		if current_pay[i]["desc"] == comment:
			return True
	
	return False
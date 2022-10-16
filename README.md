# Anypay.io API

Данные для авторизации

```python 

API_ID = ""
API_KEY = ""

```

<h1>Функции</h1>


Получить данные о балансе
```python

def getBalance() -> json

```

Курсы конвертации валют
```python

def getRates() -> json

```

Комиссии проекта
```python

def getCommissions(project_id) -> json

```

Создание платежа
```python

def getCreatePayment(project_id,pay_id,amount,currency,desc,method,email) -> json

```

Проверка платежа (Проверка идет по уникальному комментарию, поиск производится в последних 20 транзакциях)
```python

def checkPay(project_id,comment) -> bool

```

Информация о платежах
```python

def getPayments(project_id) -> json

```

Создание выплаты
```python

def getPayout(payout_id,payout_type,amount,wallet) -> json

```

Информация о выплатах
```python

def getPayouts() -> json

```

IP адреса сервиса
```python

def getIpNotification() -> json

```

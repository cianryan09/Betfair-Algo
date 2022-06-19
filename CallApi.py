from Betfair_Functions import callAping

Application = 'Y7EhzfhOmfOK6RcG'
Authentication = 'hVMGo/c8Awt4lfYmHud2H/5O0GHN37hMJFZavOYkcgY='

URL = url = "https://api.betfair.com/exchange/betting/json-rpc/v1"
Accounts_URL = "https://api.betfair.com/exchange/account/json-rpc/v1"
headers = {'X-Application': Application, 'X-Authentication': Authentication, 'content-type': 'application/json'}

event_type_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEventTypes", "params": {"filter":{}}, "id": 1}'

Api = callAping(url, event_type_req, headers)
print(Api)

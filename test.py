from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

'''
res = tavily_search("Best Hotels in Bengaluru near Selection Centre South")
print(res)
'''

result = search_flights("Plan a 10 days trip to Bali from India")
print(result)


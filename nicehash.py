
from httputil import jsonfetch

class Nicehash:
	ApiUrl = 'https://api.nicehash.com/api'
	toLocation = {
		'0': 'EU',
		'1': 'US',
	}

	def __init__(self, authDb):
		self.id = authDb['nicehash']['id']
		self.key = authDb['nicehash']['key']

	def balance(self):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'balance',
				'id': self.id,
				'key': self.key,
			}
		}
		return jsonfetch(opts)

	def orders(self, algo, location):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'orders.get',
				'location': location,
				'algo': algo,
			}
		}
		return jsonfetch(opts)

	def myOrders(self, algo, location):
		opts = {
			'url': self.ApiUrl,
			'params': {
				'method': 'orders.get',
				'my': 1,
				'location': location,
				'algo': algo,
				'id': self.id,
				'key': self.key,
			}
		}
		return jsonfetch(opts)

	def createOrder(self, params):
		params['method'] = 'orders.create'
		params['id'] = self.id
		params['key'] = self.key
		opts = {
			'url': self.ApiUrl,
			'params': params,
		}
		return jsonfetch(opts)

	def orderPriceDec(self, algo, location, orderId, bestPrice):
		callopts = {
			'method': 'orders.set.price.decrease',
			'id': self.id,
			'key': self.key,
			'location': location,
			'algo': algo,
			'order': orderId,
			# sadly, NH does not take price as input param
		}
		return jsonfetch(opts)

	def orderPriceInc(self, algo, location, orderId, bestPrice):
		callopts = {
			'method': 'orders.set.price',
			'id': self.id,
			'key': self.key,
			'location': location,
			'algo': algo,
			'order': orderId,
			'price': bestPrice,
		}
		return jsonfetch(opts)

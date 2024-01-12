import redis
from config import Config
from uuid import uuid4

from SmartEncoder.helper import TASKS

class Redis:

	def __init__(self, ttl=60) -> None:
		self.client = redis.Redis(
			host=Config.REDIS_HOST,
			port=Config.REDIS_PORT,
			password=Config.REDIS_PASS,
		)

		self.ttl = ttl

	def conn(self):
		self.client.ping()

	def gen_token(self, user_id: int) -> str:

		token = f"{str(uuid4())[0:6]}"
		self.client.set(user_id, token, ex=self.ttl)

		print(token)

		return token

	def check_access(self, user_id: int) -> bool:
		return self.client.get(user_id) != None


	def got_key(self, user_id):
		try:
			return self.client.get(f"acc^{user_id}").decode('utf-8') == '1'
		except:
			return False

	def accessed(self, user_id: int, key: str) -> bool:
		try:

			if self.client.get(user_id).decode('utf-8') == key:
				self.client.set(f"acc^{user_id}", 1, self.ttl)
				return True

			return False
		except: return False

	def g_tok(self, user_id: int) -> str:
		try:
			return self.client.get(user_id)
		except Exception as e:
			# logger.warn(f"Redis error: {e}")
			return None


myDb = Redis(Config.TIMEOUT)

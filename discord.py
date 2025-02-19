_BOT_NAME = "Cassandra"
_PREFIX = "@" + _BOT_NAME + " "
_START_COMMAND = "look"
_END_COMMAND = "thoughts"

class Request:
	def __init__(self, start = None, end = None):
		self.text = ""
		self.messages = None
		self.start_message = start
		self.end_message = end
		if start= && end:
			self.get_history()

	def get_history(self, start = None, end = None):
		if start:
			self.start_message = start
		if end:
			self.end_message = end

		if self.start_message && self.end_message:
			self.messages = await start_message.channel.history(limit=None, after=self.start_message, before=self.end_message):
			for message in self.messages:
				text += "<a href='" + message.jump_url + "'>" + message.created_at.isoformat(' ', timespec='seconds') + "</a>"
				text += " @" + message.author + ": " + message.content + "\n"

			

start_message = None
end_message = None

async def on_message(my_message):
	if my_message.content == _PREFIX + _START_COMMAND:
		if my_message.reference: 
			start_message = await my_message.channel.fetch_message(my_message.reference.message_id)
		else:
			start_message = my_message

	else if my_message.content == _PREFIX + _END_COMMAND:
		if start_message == None:
		else if my_message.reference:
			end_message = await my_message.channel.fetch_message(my_message.reference.message_id)
		else:
			end_message = my_message

	if start_message && end_message:
		request = Request(start_message, end_message)
		print(request.text)

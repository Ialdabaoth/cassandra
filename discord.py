######### import libraries
import discord
import time
import asyncio

######## configuration variables, probably should move this to its own include
_BOT_NAME = "Cassandra"
_PREFIX = "@" + _BOT_NAME + " "
_START_COMMAND = "look"
_START_ACKNOWLEDGE = "👀"
_END_COMMAND = "thoughts"
_END_ACKNOWLEDGE = "🤔"
_ERR_NO_START = "Please tell me where to start looking first?"
_TOKEN = "!!!DISCORD TOKEN GO HERE!!!"

# a Request is a block of channel history.
class Request:
	# a Request is defined between a 'start' message and an 'end' message. 
	# all messages between these two will be concatenated into the request.
	def __init__(self, start = None, end = None):
		self.text = ""
		self.messages = None
		self.start_message = start
		self.end_message = end
		if start= && end:
			self.get_history()
 
	# get_history() actually pulls the messages between 'start' and 'end' from the channel history
	# messages go into a List called .messages, and then get formatted into a single string called .text
	# the .text block is formatted with timestamps and discord URLs to each message in the chat.
	def get_history(self, start = None, end = None):
		if start:
			self.start_message = start
		if end:
			self.end_message = end

		if self.start_message && self.end_message:
			# once a 'start' and 'end' are defined, the chat history between them can be pulled
			if self.start_message.reference: 
				# if the start message quotes another message, start there and include the quoted message
				start_actual = await my_message.channel.fetch_message(self.start_message.reference.message_id)
				include_start = True
			else:
				# if the start message doesn't quote another message, start right after the start message
				start_actual = self.start_message
				include_start = False

			if self.end_message.reference: 
				# if the end message quotes another message, stop there and include the quoted message
				end_actual = await my_message.channel.fetch_message(self.end_message.reference.message_id)
				include_end = True
			else:
				# if the end message doesn't quote another message, stop right before the end message
				end_actual = self.end_message
				include_end = False

			# asynchronously pull all messages from the channel history (might take a little while)
			self.messages = await start_message.channel.history(limit=None, after=start_actual, before=end_actual):

			# append the start and end messages only if we're supposed to include them
			if include_start:
				self.messages.insert(0, start_actual)
			if include_end:
				self.messages.append(end_actual)
				
			# build the formatted .text log out of the .message list
			for message in self.messages:
				text += "<a href='" + message.jump_url + "'>" + message.created_at.isoformat(' ', timespec='seconds') + "</a>"
				text += " @" + message.author + ": " + message.content + "\n"

			

######### basic Discord stuff
client = discord.Client()

######### global variables:
# we have one global start and end message, for building a new request from user input
start_message = None
end_message = None

# listen for messages on the channel
async def on_message(my_message):
	# if the message is the start command, store the requested start and send an acknowledgement
	if my_message.content == _PREFIX + _START_COMMAND:
		start_message = my_message
		await my_message.reply(_START_ACKNOWLEDGE)

	# if the message is the end command, store the requested end and send an acknowledgement
	else if my_message.content == _PREFIX + _END_COMMAND:
		if start_message == None:
			# can't end without a start already designated
			await my_message.reply(_ERR_NO_START)
		else:
			end_message = my_message
			await my_message.reply(_END_ACKNOWLEDGE)

	# as soon as we have a start and an end, we can begin
	if start_message && end_message:
		await request = Request(start = start_message, end = end_message)

		# ###TODO ###: this is where the text would be sent to the LLM; for now, just emit the entire history as a reply
		await end_message.reply(request.text)
		# clear the start and end messages once we've completed the request
		start_message = None
		end_message = None

client.run(token)

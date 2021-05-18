class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

email_data = input()

while not email_data == "Stop":
    sender, receiver, content = email_data.split()
    current_email = Email(sender, receiver, content)
    emails.append(current_email)  # list of emails which are actually instances/objects of the class Email above
    email_data = input()

indexes_mails_to_send = [int(ele) for ele in input().split(", ")]

for index_to_send in indexes_mails_to_send:
    email = emails[index_to_send]
    email.send()
for email in emails:
    print(email.get_info())

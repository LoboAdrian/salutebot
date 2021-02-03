import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to incoming messages that contain "hello"
@app.command("/presentarms")
def message_salute(ack, say, command, message):
    ack()

    # say() sends a message to the channel where the event was triggered
    say(f":salute::salute::salute::salute::salute::salute::salute:\n:salute::salute::salute::salute::salute::salute::salute:\n:salute::salute::salute::salute::salute::salute::salute:\n:salute:")

@app.command("/corgisalute")
def corgi_salute(ack, say, command, message):
    ack()

    say(f":corgi::corgi::corgi::corgi::corgi::corgi::corgi:\n:corgi::corgi::corgi::corgi::corgi::corgi::corgi:\n:corgi::corgi::corgi::corgi::corgi::corgi::corgi:\n:salute:")
    say(f"LONG LIVE THE CORGI STATES")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

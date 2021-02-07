import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.command("/salute")
def salute(ack, say, command):
  ack()

  say(((f"{command['text']} " * 7) + '\n') * 3 + ':salute:')


@app.command("/turtlesalute")
def turtle_salute(ack, say, command, message):
    ack()

    say(f":yay-toitle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle:\n:yay-toitle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle:\n:yay-toitle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle:\n:salute:")
    say(f"LONG LIVE THE TURTLE SQUAD")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

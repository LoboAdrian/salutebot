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

@app.command("/turtlesalute")
def turtle_salute(ack, say, command, message):
    ack()

    say(f":soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle:\n:soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle:\n:soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle: :soviet-turtle:\n:salute:")
    say(f"LONG LIVE THE TURTLE SQUAD")

@app.command("/gophersalute")
def gopher_salute(ack, say, command, message):
    ack()

    say(f":bongo: :gopher: :gopher: :gopher: :gopher: :gopher: :gopher:\n:bongo: :gopher: :gopher: :gopher: :gopher: :gopher: :gopher:\n:bongo: :gopher: :gopher: :gopher: :gopher: :gopher: :gopher:\n:salute:")
    say(f"LONG LIVE THE GOPHER ARMY")


@app.command("/rustsalute")
def rust_salute(ack, say, command, message):
    ack()

    say(f":ferrisbongo: :ferris: :ferris: :ferris: :ferris: :ferris: :ferris:\n:ferrisbongo: :ferris: :ferris: :ferris: :ferris: :ferris: :ferris:\n:ferrisbongo: :ferris: :ferris: :ferris: :ferris: :ferris: :ferris:\n:salute:")
    say(f"LONG LIVE THE RUST ARMY")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

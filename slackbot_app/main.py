from fastapi import FastAPI

app = FastAPI()


@app.post("/slackbot")
def read_root(event: dict):

    challenge_answer = event.get("challenge")

    return {
        'statusCode': 200,
        'body': challenge_answer
    }

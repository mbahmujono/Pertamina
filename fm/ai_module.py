import boto3
import json

def invoke(promp):
    brt = boto3.client(service_name='bedrock-runtime')

    body = json.dumps({
        "prompt": f"Human:\n\n{promp}\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })

    modelId = 'anthropic.claude-instant-v1'
    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    # print(response_body.get('completion'))
    return response_body.get('completion')
if __name__ == '__main__':
    invoke('Human: give analysis for City_A for the next 5 minutes. the sales is 5000 and the forecasted sales is 5000 Assistant:')
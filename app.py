from flask import Flask, request, jsonify
import openai 
openai.api_key = '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'
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def process_comments():
    data = request.get_json()
    
    comments = data.get('comments', [])
    prompt = f"""Give me a sentiment report of the text delimited by triple backticks.
The sentiment report should consist of sentiment score, sentiment label, and the text.
Along with that provide a list of keywords which helped determine the sentiment.

The final output should be a JSON object.
Text: {comments}
"""
    response=get_completion(prompt)
    
    
    
    # for comment in comments:
    #     print(comment)
    
    return jsonify({'message': 'Comments received and processed'})


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1.5, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    app.run(debug=True)
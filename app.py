from flask import Flask, request, jsonify,render_template
import openai 
openai.api_key = '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'
app = Flask(__name__)
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     return render_template('chat.html')
@app.route('/process_comments', methods=['POST', 'GET'])

def process_comments():
    data = request.get_json()
    # print(data)
    comments = data.get('comments', [])
    # print(comments)
    prompt = f"""Give me a sentiment report of the text delimited by triple backticks.
The sentiment report should consist of sentiment score, sentiment label, and the text.
Along with that provide a list of keywords which helped determine the sentiment.

The final output should be a JSON object.
Text: {comments}
"""
    response=get_completion(prompt)
    print(response)
    # return render_template('chat.html', response=response)
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
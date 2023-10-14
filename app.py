from flask import Flask, request, jsonify,render_template
import openai 
openai.api_key = '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'
app = Flask(__name__)
response=None
@app.route('/process_comments', methods=['POST', 'GET'])

def process_comments():
    data = request.get_json()
    # print(data)
    comments = data.get('comments', [])
    # print(comments)
    prompt = f"""
    If the time to analyze a single comment exceeds 30 seconds, then skip the comment and proceed to the next comment.
    All the output you provide is in english only and does not involve any sort of programming languages.
    For the text delimitted by the triple backticks, follow these steps of processing for each comment:
    1. Analyze the sentiment of the text if it does not contain a URL. Print the sentiment of the text.
    2. Print the sentiment score of the text.
    3. Print the keywords that helped determine the sentiment of the text.
    4. Print the text.

Make sure all of the above steps have been followed for each comment. Only then proceed to what is mentioned below.
Finally print the count of positive comments and print the count of negative comments.

The final output should be a JSON object.
Text: ```{comments}```
"""
    global response
    response=get_completion(prompt)
    print(response)
    # return render_template('chat.html', response=response)
    return jsonify({'message': 'Comments received and processed'})

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html',response={"h":response})

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
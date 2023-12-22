from flask import Flask, request
import hard_corder

app = Flask(__name__)


@app.route('/api/gpt', methods=['POST'])
def action():
    data = request.get_json()
    type = data.get('type')
    content = data.get('content')

    result = hard_corder.get_gpt_result(type, content)
    return result.json()


if __name__ == '__main__':
    app.run(debug=True)

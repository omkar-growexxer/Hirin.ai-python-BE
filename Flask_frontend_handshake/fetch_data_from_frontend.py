from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.json

    if not data:
        return jsonify({'error': "No JSON payload provided"}), 400

    required_keys = ['candidate_id', 'questions', 'tab_switch_count', 'exit_full_screen']
    missing_keys = [key for key in required_keys if key not in data]

    if missing_keys:
        return jsonify({"error": f"Missing required fields: {missing_keys}"}), 400

    cid = data.get("candidate_id")
    questions = data.get("questions")
    tab_count = data.get("tab_switch_count")
    exit_fs = data.get("exit_full_screen")

    for question in questions:
        user_video_url = question.get("user_video_url")
        question_text = question.get("question")
        answer = question.get("answer")
        seniority_level = question.get("level_of_seniority")
        role = question.get("role")
        difficulty_level = question.get("difficulty_level")
    
        if not all([user_video_url, question_text, answer]):
            return jsonify({"error": "Each question must have user_video_url, question, and answer"}), 400

    response = {
        "status": "success",
        "candidate_id": cid,
        "questions_received": len(questions),
        "tab_switch_count": tab_count,
        "exit_full_screen": exit_fs,
        "questions": questions
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
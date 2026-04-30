import ollama

def test_gramin_nyaya():
    print("--- Connecting to Gramin-Nyaya Brain... ---")
    
    # We are using Qwen 2.5 because it is great at Hindi
    response = ollama.chat(model='qwen2.5:1.5b', messages=[
        {'role': 'system', 'content': 'You are Gramin-Nyaya, a legal assistant for rural India. Answer in simple Hindi.'},
        {'role': 'user', 'content': 'नमस्ते, मुझे अपनी ज़मीन की रजिस्ट्री करानी है, क्या करूँ?'},
    ])
    
    print("\nAI Response (Hindi):")
    print(response['message']['content'])

if __name__ == "__main__":
    test_gramin_nyaya()
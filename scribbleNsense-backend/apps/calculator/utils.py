import google.generativeai as genai
import json
from PIL import Image
from constants import GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
def analyze_image(img:Image, dict_of_vars:dict):
    dict_of_vars_str = json.dumps(dict_of_vars, ensure_ascii=False)
    prompt = (
        f"You have been given an image with some mathematical expressions, equations, or graphical problems, and you need to solve them. "
        f"Note: Use the PEMDAS rule for solving mathematical expressions. PEMDAS stands for the Priority Order: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right). Parentheses have the highest priority, followed by Exponents, then Multiplication and Division, and lastly Addition and Subtraction. "
        f"For example: "
        f"Q. 2 + 3 * 4 "
        f"(3 * 4) => 12, 2 + 12 = 14. "
        f"Q. 2 + 3 + 5 * 4 - 8 / 2 "
        f"5 * 4 => 20, 8 / 2 => 4, 2 + 3 => 5, 5 + 20 => 25, 25 - 4 => 21. "
        f"YOU CAN HAVE FIVE TYPES OF EQUATIONS/EXPRESSIONS IN THIS IMAGE, AND ONLY ONE CASE SHALL APPLY EVERY TIME: "
        f"Following are the cases: "
        f"1. Simple mathematical expressions like 2 + 2, 3 * 4, 5 / 6, 7 - 8, etc.: In this case, solve and return the answer in the format of a LIST OF ONE DICT [{{'expr': given expression, 'result': calculated answer}}]. "
        f"2. Set of Equations like x^2 + 2x + 1 = 0, 3y + 4x = 0, 5x^2 + 6y + 7 = 12, etc.: In this case, solve for the given variable, and the format should be a COMMA SEPARATED LIST OF DICTS, with dict 1 as {{'expr': 'x', 'result': 2, 'assign': True}} and dict 2 as {{'expr': 'y', 'result': 5, 'assign': True}}. This example assumes x was calculated as 2, and y as 5. Include as many dicts as there are variables. "
        f"3. Assigning values to variables like x = 4, y = 5, z = 6, etc.: In this case, assign values to variables and return another key in the dict called {{'assign': True}}, keeping the variable as 'expr' and the value as 'result' in the original dictionary. RETURN AS A LIST OF DICTS. "
        f"4. Analyzing Graphical Math problems, which are word problems represented in drawing form, such as cars colliding, trigonometric problems, problems on the Pythagorean theorem, adding runs from a cricket wagon wheel, etc. These will have a drawing representing some scenario and accompanying information with the image. PAY CLOSE ATTENTION TO DIFFERENT COLORS FOR THESE PROBLEMS. You need to return the answer in the format of a LIST OF ONE DICT [{{'expr': given expression, 'result': calculated answer}}]. "
        f"5. Detecting Abstract Concepts that a drawing might show, such as love, hate, jealousy, patriotism, or a historic reference to war, invention, discovery, quote, etc. USE THE SAME FORMAT AS OTHERS TO RETURN THE ANSWER, where 'expr' will be the explanation of the drawing, and 'result' will be the abstract concept. "
        f"Analyze the equation or expression in this image and return the answer according to the given rules: "
        f"Make sure to use extra backslashes for escape characters like \\f -> \\\\f, \\n -> \\\\n, etc. "
        f"Here is a dictionary of user-assigned variables. If the given expression has any of these variables, use its actual value from this dictionary accordingly: {dict_of_vars_str}. "
        f"DO NOT USE BACKTICKS OR MARKDOWN FORMATTING. "
        f"RETURN THE RESPONSE AS A PURE JSON LIST OF DICTS, ENSURING ALL KEYS AND STRING VALUES ARE ENCLOSED IN DOUBLE QUOTES. DO NOT INCLUDE ANY OTHER TEXT OR EXPLANATION." # Critical change here
    )
    response = model.generate_content([prompt, img])
    raw_response_text = response.text.strip() # Strip whitespace

    print(raw_response_text)
    answers = []
    try:
        # Improved parsing logic
        parsed_json_str = raw_response_text
        if raw_response_text.startswith('```json'):
            # Extract JSON string if Gemini adds markdown
            try:
                # Find the first and last ````
                start_index = raw_response_text.find('```json')
                end_index = raw_response_text.rfind('```')
                if start_index != -1 and end_index != -1 and end_index > start_index:
                    parsed_json_str = raw_response_text[start_index + len('```json'):end_index].strip()
                else:
                    # Fallback if markdown format is unexpected
                    print(f"Warning: '```json' found but unable to extract cleanly from: {raw_response_text}")
                    parsed_json_str = raw_response_text.replace("```json", "").replace("```", "").strip()
            except Exception as e:
                print(f"Error during markdown extraction: {e}")
                parsed_json_str = raw_response_text.replace("```json", "").replace("```", "").strip()
        
        # Replace single quotes with double quotes for keys and string values
        # This is a heuristic and might fail for complex strings containing both single and double quotes.
        # However, for simple JSON as expected, it should work.
        # A more robust solution would be to use a proper JSON linter/fixer or a regex for keys/values.
        # For this specific error, we're fixing the single quotes for keys.
        parsed_json_str = parsed_json_str.replace("'", '"') # This is the primary fix for your current error
        
        answers = json.loads(parsed_json_str) # Use json.loads

    except json.JSONDecodeError as e:
        print(f"Error in parsing response from Gemini API (JSONDecodeError): {e}")
        print(f"Problematic string: {raw_response_text}") # Log the original problematic string
        print(f"Attempted to parse: {parsed_json_str}") # Log the string after pre-processing
    except Exception as e:
        print(f"Error in parsing response from Gemini API: {e}")
        print(f"Problematic string: {raw_response_text}") # Log the original problematic string
        print(f"Attempted to parse: {parsed_json_str}") # Log the string after pre-processing

    print('returned answer ', answers)
    for answer in answers:
        # This part should be fine as it's modifying a Python dictionary
        if 'assign' in answer:
            answer['assign'] = True
        else:
            answer['assign'] = False
    return answers
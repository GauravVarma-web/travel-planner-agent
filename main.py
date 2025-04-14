# main.py
from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import react_system_prompt
from actions import get_destination_weather, get_flight_info, recommend_attractions
from json_helpers import extract_json

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Available actions mapping
available_actions = {
    "get_destination_weather": get_destination_weather,
    "get_flight_info": get_flight_info,
    "recommend_attractions": recommend_attractions
}

def generate_response(messages):
    """Generate a response from the AI model"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=messages
    )
    return response.choices[0].message.content

def run_travel_agent():
    """Run the travel planner agent"""
    print("Travel Planner AI (Type 'exit' to quit)")
    
    messages = [
        {"role": "system", "content": react_system_prompt}
    ]
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break
        
        messages.append({"role": "user", "content": user_input})
        
        # Agent loop
        turn_count = 1
        max_turns = 5
        
        while turn_count < max_turns:
            print(f"\n[System: Thinking... (Turn {turn_count}/{max_turns})]")
            turn_count += 1
            
            # Get AI response
            ai_response = generate_response(messages)
            print(f"\nAI: {ai_response}")
            
            # Extract function calls
            json_functions = extract_json(ai_response)
            
            if json_functions:
                for func in json_functions:
                    if "function_name" in func and "function_parms" in func:
                        function_name = func["function_name"]
                        function_parms = func["function_parms"]
                        
                        if function_name in available_actions:
                            print(f"\n[System: Executing {function_name}...]")
                            
                            # Call the function with parameters
                            action_function = available_actions[function_name]
                            result = action_function(**function_parms)
                            
                            # Format the result message
                            function_result_message = f"Action_Response: {result}"
                            print(f"[System: {function_result_message}]")
                            
                            # Add to conversation
                            messages.append({"role": "assistant", "content": ai_response})
                            messages.append({"role": "user", "content": function_result_message})
                            
                            # Continue the loop for more potential actions
                            break
                    else:
                        # Malformed function call, break the loop
                        break
            else:
                # No more function calls, we have a final answer
                messages.append({"role": "assistant", "content": ai_response})
                break
    
    print("\nThank you for using Travel Planner AI!")

if __name__ == "__main__":
    run_travel_agent()
import streamlit as st
import random
import math

def initialize_game_state():
    st.session_state.setdefault('mode', 'User Guessing')
    st.session_state.setdefault('min_value', 1)
    st.session_state.setdefault('max_value', 100)
    st.session_state.setdefault('number_to_guess', random.randint(st.session_state.min_value, st.session_state.max_value))
    st.session_state.setdefault('user_feedback', f"Guess a number between {st.session_state.min_value} and {st.session_state.max_value}!")
    st.session_state.setdefault('attempts', 0)
    st.session_state.setdefault('computer_low', st.session_state.min_value)
    st.session_state.setdefault('computer_high', st.session_state.max_value)
    st.session_state.setdefault('computer_feedback', "")

def reset_game_state():
    st.session_state.number_to_guess = random.randint(st.session_state.min_value, st.session_state.max_value)
    st.session_state.attempts = 0
    st.session_state.computer_low = st.session_state.min_value
    st.session_state.computer_high = st.session_state.max_value
    st.session_state.computer_feedback = "Game reset. Think of a new number within the updated range!"

def calculate_optimal_attempts():
    range_size = st.session_state.max_value - st.session_state.min_value + 1
    return math.ceil(math.log2(range_size))
initialize_game_state()
st.title("Number Guessing Game with Optimal Attempt Challenge")
mode = st.radio("Select Game Mode", ("User Guessing", "Machine Guessing"))
min_value = st.number_input("Enter minimum value:", min_value=1, value=st.session_state.min_value, step=1)
max_value = st.number_input("Enter maximum value:", value=st.session_state.max_value, step=1)
if max_value <= min_value:
    st.warning("Maximum value should be greater than minimum value. Setting it to minimum + 1.")
    max_value = min_value + 1
if min_value != st.session_state.min_value or max_value != st.session_state.max_value:
    st.session_state.min_value = min_value
    st.session_state.max_value = max_value
    reset_game_state()
    st.session_state.user_feedback = f"New range set! Guess a number between {st.session_state.min_value} and {st.session_state.max_value}."
optimal_attempts = calculate_optimal_attempts()
if mode == "User Guessing":
    st.write("User Guessing Mode: Try to guess the number I'm thinking of!")
    st.write(f"Optimal attempts: {optimal_attempts}")
    guess = st.number_input("Enter your guess:", min_value=st.session_state.min_value, max_value=st.session_state.max_value, step=1)
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.session_state.user_feedback = "Too low! Try again."
        elif guess > st.session_state.number_to_guess:
            st.session_state.user_feedback = "Too high! Try again."
        else:
            st.session_state.user_feedback = f"Congratulations! You guessed it in {st.session_state.attempts} attempts."
            if st.session_state.attempts <= optimal_attempts:
                st.session_state.user_feedback += " Great job! You guessed it within the optimal number of attempts!"
            else:
                st.session_state.user_feedback += " You exceeded the optimal attempts. Try to guess more efficiently next time!"
            reset_game_state()
    st.write(st.session_state.user_feedback)
else:
    st.write("Machine Guessing Mode: Think of a number within the range, and I'll try to guess it!")

    st.session_state.computer_guess = (st.session_state.computer_low + st.session_state.computer_high) // 2
    st.write(f"My guess is: {st.session_state.computer_guess}")
    feedback = st.radio("Is my guess correct?", ("Too low", "Too high", "Correct"))
    if st.button("Submit Feedback"):
        if feedback == "Too low":
            st.session_state.computer_low = st.session_state.computer_guess + 1
            st.session_state.computer_feedback = "I'll try higher."
        elif feedback == "Too high":
            st.session_state.computer_high = st.session_state.computer_guess - 1
            st.session_state.computer_feedback = "I'll try lower."
        else:
            st.session_state.computer_feedback = "I guessed it! Let's play again!"
            reset_game_state()
    st.session_state.computer_guess = (st.session_state.computer_low + st.session_state.computer_high) // 2
    st.write(st.session_state.computer_feedback)
if st.button("Reset Game"):
    reset_game_state()

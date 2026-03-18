# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I was able to play but when trying to continue guessing it gave me issues.
- List at least two concrete bugs you noticed at the start  
1. The reset feature does not reset properly
2. The range for the hard level was below 0

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude and Copilot.

- Give one example of an AI suggestion that was correct (including what the AI 
  suggested and how you verified the result).
Claude correctly identified that the New Game button was missing resets for 
`score` and `status` in session state. It suggested adding 
`st.session_state.score = 0` and `st.session_state.status = "playing"` to the 
new_game block. I verified this by deliberately losing a game, clicking New Game, 
and confirming the game started fresh instead of immediately showing "Game over."

- Give one example of an AI suggestion that was incorrect or misleading (including 
  what the AI suggested and how you verified the result).
Even after Claude helped fix check_guess in logic_utils.py, the game was still 
giving wrong hints — telling me to go higher when I guessed 100 and the answer 
was 4. The AI's fix was technically correct but incomplete because it did not 
remind me to delete the old broken version of check_guess still sitting in app.py 
and add the import. I caught this by checking app.py and noticing the original 
broken functions were still defined there, overriding the fixed ones in logic_utils.py.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested each fix by actually playing the game and trying to reproduce the broken 
behavior. For the reset bug I lost a game on purpose and clicked New Game. For the 
hint bug I guessed extreme values like 1 and 100 and checked whether the direction 
made sense given the secret shown in the debug panel.

- Describe at least one test you ran (manual or using pytest) and what it showed 
  you about your code.
I ran a manual test for the string comparison bug by opening the Developer Debug 
Info expander to see the secret, then guessing a single-digit number like 1 against 
a two-digit secret like 42. The game told me to go higher even though 1 is below 42, 
which confirmed the hint direction was completely broken on even-numbered attempts.

- Did AI help you design or understand any tests? How?
Yes, Claude explained that the bug was caused by Python's lexicographic string 
comparison, where "1" is considered greater than "42" alphabetically. That 
explanation helped me understand why single-digit guesses were the best way to 
expose the bug, since they're the most likely to produce wrong results under 
string comparison.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has 
  never used Streamlit?
Every time you interact with a Streamlit app — clicking a button, typing in a box — 
the entire Python script reruns from top to bottom. That means any regular variable 
you set gets wiped out on the next interaction. Session state is like a backpack the 
app carries between reruns: anything you store in `st.session_state` survives. That 
is why forgetting to reset `status` in session state kept the game locked even after 
clicking New Game — the old value was still sitting in the backpack.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future 
  labs or projects?
Adding FIXME comments to mark the exact line where a bug lives before touching 
anything. It forced me to actually understand where the problem was instead of 
just guessing, and it gave Copilot better context when I asked it for help.

- What is one thing you would do differently next time you work with AI on a 
  coding task?
I would verify that the AI's fix is complete end-to-end before moving on. In this 
project the fix for check_guess was correct in isolation but I still had to manually 
delete the old version from app.py and add the import — steps the AI did not 
explicitly walk me through the first time.

- In one or two sentences, describe how this project changed the way you think 
  about AI generated code.
AI generated code can look correct and still be broken in ways that only show up 
when the whole system runs together. I now know to treat AI suggestions as a 
starting point that still needs to be read carefully, tested manually, and verified 
in context — not just dropped in and assumed to work.
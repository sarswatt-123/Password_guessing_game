# 🎯 Number Guessing Game GUI (Python Tkinter)

A simple and interactive **Number Guessing Game** built using **Python** and **Tkinter GUI**. The computer randomly selects a number between **1 to 100**, and the player has to guess the correct number with the help of hints.

---

## 📸 Project Preview

```
+--------------------------------+
|      🎯 Number Guessing Game    |
|                                |
|     Guess Number (1 - 100)     |
|                                |
|          [       ]             |
|                                |
|          [ Check ]             |
|                                |
|     Your guess is too low      |
|                                |
+--------------------------------+
```

---

## 🚀 Features

✨ Interactive GUI using Tkinter
🎲 Random number generation from 1 to 100
📉 Displays "Too Low" hint
📈 Displays "Too High" hint
🎉 Congratulates user on correct guess
🔢 Counts number of attempts

---

## 🛠️ Technologies Used

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Python        | Core programming language    |
| Tkinter       | Creating graphical interface |
| Random Module | Generating secret number     |

---

## 🔄 Game Flow Diagram

```mermaid
flowchart TD
    A[Start Game] --> B[Generate Random Number 1-100]
    B --> C[User Enters Guess]
    C --> D{Is Guess Correct?}

    D -- No, Too Low --> E[Show "Too Low"]
    E --> C

    D -- No, Too High --> F[Show "Too High"]
    F --> C

    D -- Yes --> G[Display Success Message & Attempts]
```

---

## 📂 Project Structure

```
Number-Guessing-Game/
│
├── game.py       # Main Python source code
└── README.md     # Project documentation
```

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Move to the project folder

```bash
cd Number-Guessing-Game
```

### 3. Run the Python file

```bash
python game.py
```

---

## 🧠 Algorithm

1. Generate a random number between 1 and 100.
2. Take input from the user through the GUI.
3. Compare the entered number with the secret number.
4. Display whether the guess is low or high.
5. Repeat until the correct number is guessed.
6. Display the total attempts taken.

---

## 🔮 Future Enhancements

* 🔄 Add a Reset Game button
* 🎨 Improve GUI design and themes
* ⏱️ Add a timer
* 🏆 Add difficulty levels (Easy/Medium/Hard)
* 💾 Save high scores

---

## 👩‍💻 Author

Developed with ❤️ using Python and Tkinter.

⭐ If you like this project, don't forget to give it a star!

# 🚀 RDT Mars Rover Assessment

## 📌 Overview  
This project is a solution to the **Mars Rover technical assessment** provided by RDT. The goal is to develop a Python program that simulates the movement of robotic rovers on a plateau based on user input.

The rovers follow simple commands (`L`, `R`, `M`) to rotate left, right, or move forward within the boundaries of a given plateau.

---

## ✨ Features  
✔️ Accepts **multiple rovers** and movement instructions  
✔️ Ensures rovers **stay within plateau boundaries**  
✔️ Uses **modular OOP design** with a `Plateau` and `Rover` class  
✔️ Implements **efficient rotation logic** using modular indexing  
✔️ Allows easy **input handling** for dynamic testing  

---

## 📜 Example Input & Output  
### **🔹 Input**
5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM
### **🔹 Expected Output**
1 3 N 5 1 E


---

## 🏗️ Approach  
The project follows an **Object-Oriented Programming (OOP)** approach:
- **`Plateau` Class**: Stores plateau boundaries and checks rover limits.
- **`Rover` Class**: Handles movement, rotation, and command execution.

### 🔄 **Movement Logic**  
- **Turning Left (`L`)**: Moves to the previous direction in `["N", "E", "S", "W"]`, cycling back to the end if needed.
- **Turning Right (`R`)**: Moves to the next direction, cycling back to the start if needed.
- **Moving Forward (`M`)**: Updates X or Y position based on the rover's direction, ensuring it stays in bounds.

---

## ⏳ Time Taken  
⏱️ Approx. **4 hours**  
- Majority of time spent on **debugging movement logic and refining OOP structure**.

---

## 🛠️ Challenges & Learnings  
- Ensuring rovers **stay within boundaries** and do not exceed the plateau limits.  
- Handling **multiple rovers sequentially** as required.  
- Implementing **modulo indexing for direction changes** to simplify rotation logic.  
- Understanding **GitHub version control**, `.gitignore`, and repo structuring.

---

## 🚀 How to Run  
1️⃣ **Clone the repo**  
   ```sh
   git clone https://github.com/MattyCoding18/RDTMarsRover.git
```
2️⃣ **Navigate to the project folder**
```sh
cd RDTMarsRover
```
3️⃣ **Run the Python script**
```sh
python main.py
```





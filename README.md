# 🏫 IIT Goa Mess Live — Smart ID Scanner, Menu & Queue Simulator

> *A stochastic digital twin of the IIT Goa dining hall modeling mandatory ID card scanning, menu-driven crowd dynamics, tray refill bottlenecks, and staggered hostel batch timings.*

---

## 🚀 Overview
**IIT Goa Mess Live** is an interactive Python simulation and crowd-management dashboard designed to solve daily dining congestion during peak 30-minute rush windows across a 650-member campus community (students and faculty).

Unlike basic queue models, this project captures the realistic two-stage flow of the IIT Goa mess:
1. **Mandatory ID Card Scanner Gate:** Every arriving student and professor must queue at the entrance gate where unique student roll numbers (`2301..2603`) and faculty IDs (`PROF-101..199`) are logged via a Python `set()` to prevent double-scanning and track live headcount.
2. **Menu-Driven Crowd Spikes & Counter Queues:** After scanning, members choose from three serving counters loaded dynamically with the **official IIT Goa Mess Menu** across all 7 days and 4 meals (such as Wednesday Chicken Curry Lunch and Sunday Biriyani Dinner).

---

## ✨ Key Features

* **Official IIT Goa Mess Menu Integration:** Full dictionary mapping for Monday through Sunday (Breakfast, Lunch, Snacks, and Dinner) featuring campus favorites like Methi Thepla, Idly-Vada, Pani Puri, Egg Curry, and Chicken/Paneer Biriyani.
* **Realistic Campus Turnout Generation:** Dynamically models campus attendance based on meal type:
  * **Breakfast:** ~400 members (`370–445` range)
  * **Lunch & Dinner:** ~500 members (`470–545` range)
  * **Non-Veg / Special Meal Days:** Spikes to ~600 members (`565–635` range, capped under the 650 campus capacity limit).
* **Kitchen Tray Refill Bottlenecks:** Simulates food depletion (`random.uniform(1.7, 3.2)` per serving). When a tray hits 0%, a 3-minute orange `KITCHEN REFILLING` timer pauses that counter, demonstrating real-world queue build-ups.
* **Live Student Crowd Advisor:** An automated status banner that alerts students in real-time whether to **Go Now (Green)**, expect a **Moderate Crowd (Yellow)**, or watch out for a **Peak Rush Alert (Red)**.
* **Comparative Matplotlib Analytics:** A built-in analytics module that runs parallel 120-minute simulations to plot **Normal Mess Rush** against **Staggered Hostel Timing**.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x (Pure Python implementation — no external compiled binaries required)
* **GUI & Animation:** `tkinter` (Standard library)
* **Stochastic Engine:** `random` (Standard library)
* **Analytics Graphing:** `matplotlib` (Optional fallback included if `matplotlib` is not installed)

---

## 📂 Project Structure

```text
IIT-Goa-Mess-Live/
├── code/
│   └── iit_goa_mess_live.py   # Main simulation engine & Tkinter dashboard
└── README.md                  # Project documentation
```

---

## 🏃‍♂️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mallidimohan41297/IIT-Goa-Mess-Live.git
   cd IIT-Goa-Mess-Live
   ```

2. **(Optional) Install `matplotlib` for wait-time comparison graphs:**
   ```bash
   pip install matplotlib
   ```

3. **Run the simulator:**
   ```bash
   python3 code/iit_goa_mess_live.py
   ```

4. **Using the Dashboard:**
   * Select any **Day** (Monday–Sunday) and **Meal** (Breakfast, Lunch, Snacks, Dinner) from the dropdowns.
   * Click **Start / Resume** to watch the live ID Scanner gate and 3 food counters in action.
   * Toggle **Staggered Hostel Timing** and click **New Random Day Run** to see how splitting hostel arrival waves prevents red congestion bars.
   * Click **Plot Wait-Time Graph** to view a side-by-side `matplotlib` comparison of Normal vs. Staggered wait times.

---

## 👤 Author

**Mallidi Mohan Siva Venkata Rama Reddy**  
*Indian Institute of Technology Goa*  
GitHub: [@mallidimohan41297](https://github.com/mallidimohan41297)

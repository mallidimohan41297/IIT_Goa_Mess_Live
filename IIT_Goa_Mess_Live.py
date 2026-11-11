import tkinter as tk
from tkinter import ttk
import random
import os

# Safe check for matplotlib on lab computers
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

MAX_CAMPUS_CAPACITY = 650  # Total IIT Goa students + professors


# ==============================================================================
# PART 1: OFFICIAL IIT GOA MENU & REALISTIC TURNOVER GENERATOR (Member 1)
# ==============================================================================
# target_range: (min_members, max_members) who will scan ID and eat that meal
IIT_GOA_MENU = {
    "Monday": {
        "Breakfast": {
            "c1": "Methi Thepla + Tomato Curry",
            "c2": "Sprouted Moong + Bread, Butter & Jam",
            "c3": "Egg Bhurji + Milk/Tea/Coffee + Banana",
            "target_range": (380, 415)
        },
        "Lunch": {
            "c1": "Aloo Gravy + Mix Veg Dry + Dal Methi",
            "c2": "Lemon Rice + Plain Rice + Curd & Sugar",
            "c3": "Roti / Butter Roti + Fryums + Salad",
            "target_range": (480, 515)
        },
        "Snacks": {
            "c1": "Hot Samosa + Red & Green Chutney",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (430, 475)
        },
        "Dinner": {
            "c1": "Chilli Potato + Mushroom Curry + Masala Dal",
            "c2": "Jeera Rice + Roti / Butter Roti + Salad",
            "c3": "Sweet Dish: Ice Cream Counter",
            "target_range": (505, 540)
        }
    },
    "Tuesday": {
        "Breakfast": {
            "c1": "Idly + Vada (2 pcs) + Sambhar & Chutney",
            "c2": "Sweet Corn + Bread & Butter + Seasonal Fruit",
            "c3": "Boiled Eggs + Bournvita/Milk/Tea/Coffee",
            "target_range": (390, 425)
        },
        "Lunch": {
            "c1": "Chhole + Aloo Matar Gravy + Plain Toor Dal",
            "c2": "Plain Rice + Fried Papad + Mixed Salad",
            "c3": "Hot Poori + Sweet Lassi Counter",
            "target_range": (495, 530)
        },
        "Snacks": {
            "c1": "Vadapav / Pav Bhaji + Onion & Lemon",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (460, 500)
        },
        "Dinner": {
            "c1": "Palak Paneer + Bhindi Dry + Moong Dal",
            "c2": "Plain Rice + Roti / Butter Roti + Salad",
            "c3": "Sweet Dish: Besan Laddu",
            "target_range": (485, 520)
        }
    },
    "Wednesday": {
        "Breakfast": {
            "c1": "Poha + Sev, Lemon, Onion & Chutney",
            "c2": "Sprouted Moong + Bread/Jam + Seasonal Fruits",
            "c3": "Boiled Eggs + Milk/Tea/Coffee",
            "target_range": (370, 405)
        },
        "Lunch": {
            "c1": "Chicken Curry (Non-Veg Main) + Plain Rice",
            "c2": "Paneer Curry (Veg Main) + Dal Makhani + Soybean",
            "c3": "Roti / Butter Roti + Butter Milk + Fryums",
            "target_range": (580, 620)  # Non-Veg Day Spike (~600)
        },
        "Snacks": {
            "c1": "Dal Vada + Onion & Lemon",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (390, 430)
        },
        "Dinner": {
            "c1": "Rajma + French Beans + Dal Tadka",
            "c2": "Pulihora + Plain Rice + Butter Roti",
            "c3": "Sweet Dish: Sewai Kheer",
            "target_range": (480, 515)
        }
    },
    "Thursday": {
        "Breakfast": {
            "c1": "Poori / Upma + Bhaji & Coconut Chutney",
            "c2": "Sprouted Chana + Bread/Butter + Banana",
            "c3": "Boiled Eggs + Milk/Tea/Coffee",
            "target_range": (385, 420)
        },
        "Lunch": {
            "c1": "Besan Kadhi Pakoda + Sev Tomato Sabji + Dal Tadka",
            "c2": "Plain Rice + Curd & Sugar + Fried Papad",
            "c3": "Roti / Butter Roti + Beetroot Salad",
            "target_range": (470, 505)
        },
        "Snacks": {
            "c1": "Pani Puri (5 pcs) + Bhel + Aloo Bhurji & Sev",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (490, 535)
        },
        "Dinner": {
            "c1": "Mix Veg + Aloo Palak Gravy + Dal Palak/Sambhar",
            "c2": "Plain Rice + Roti / Butter Roti + Salad",
            "c3": "Sweet Dish: Motichur Laddoo",
            "target_range": (485, 520)
        }
    },
    "Friday": {
        "Breakfast": {
            "c1": "Aloo Paratha + Fresh Curd",
            "c2": "Boiled Chana + Bread/Jam + Seasonal Fruits",
            "c3": "Egg Bhurji + Milk/Tea/Coffee",
            "target_range": (405, 435)
        },
        "Lunch": {
            "c1": "Soya Bean Curry + Cabbage Matar + Dal Makhani",
            "c2": "Tomato Rice + Plain Rice + Boondi Raita",
            "c3": "Roti / Butter Roti + Fryums + Mixed Salad",
            "target_range": (480, 515)
        },
        "Snacks": {
            "c1": "Chana Chat + Red & Green Chutney",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (410, 445)
        },
        "Dinner": {
            "c1": "Egg Curry (Non-Veg Counter) + Jeera Rice",
            "c2": "Veg Kolhapuri + Matar Semi-Gravy + Dal Tadka",
            "c3": "Butter Roti + Sweet Dish: Fruit Custard",
            "target_range": (565, 605)  # Egg Curry + Fruit Custard Spike (~585)
        }
    },
    "Saturday": {
        "Breakfast": {
            "c1": "Hot Uttapam + Sambhar & Coconut Chutney",
            "c2": "Mixed Sprouts + Bread/Butter + Seasonal Fruits",
            "c3": "Boiled Eggs + Milk/Tea/Coffee",
            "target_range": (375, 410)
        },
        "Lunch": {
            "c1": "Rajma + Brinjal Dry + Rasam",
            "c2": "Plain Rice + Curd & Sugar + Fried Papad",
            "c3": "Roti / Butter Roti + Radish Salad",
            "target_range": (485, 520)
        },
        "Snacks": {
            "c1": "Hot Maggi Counter + Red & Green Chutney",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (475, 515)
        },
        "Dinner": {
            "c1": "Chole + Red Pumpkin + Moong Dal",
            "c2": "Hot Poori + Plain Rice + Salad",
            "c3": "Sweet Dish: Hot Gulab Jamun",
            "target_range": (510, 545)
        }
    },
    "Sunday": {
        "Breakfast": {
            "c1": "Crispy Masala Dosa + Sambhar & Chutney",
            "c2": "Mixed Groundnut + Bread/Butter + Banana",
            "c3": "Boiled Eggs + Milk/Tea/Coffee",
            "target_range": (415, 445)
        },
        "Lunch": {
            "c1": "Soybean Gravy + Shimla Mirch Aloo + Dal Methi",
            "c2": "Fried Rice + Plain Rice + Sabja Lemon Water",
            "c3": "Roti / Butter Roti + Fried Papad/Fryums",
            "target_range": (485, 520)
        },
        "Snacks": {
            "c1": "Veg Sandwich + Lemon & Onion",
            "c2": "Bread + Butter + Jam",
            "c3": "Hot Tea + Coffee Counter",
            "target_range": (420, 455)
        },
        "Dinner": {
            "c1": "Chicken Biriyani (Non-Veg Main) + Plain Rice",
            "c2": "Paneer Biriyani (Veg Main) + Dal Tadka + Veg Raita",
            "c3": "Sweet Dish: Kesari Bath",
            "target_range": (590, 635)  # Sunday Biriyani Peak (~610/650)
        }
    }
}


def generate_meal_arrival_schedule(day, meal, staggered_mode):
    """
    1. Picks a random total attendance for the chosen Day & Meal (e.g. ~400 Breakfast,
       ~500 Lunch/Dinner, ~600 Non-Veg/Biriyani, capped under 650 campus total).
    2. Uses random.choices() with minute weights to distribute those arrivals
       across the 120-minute meal window.
    """
    low, high = IIT_GOA_MENU[day][meal]["target_range"]
    total_expected = min(MAX_CAMPUS_CAPACITY, random.randint(low, high))

    minute_weights = []
    for m in range(120):
        if not staggered_mode:
            if 20 <= m <= 55:
                w = random.uniform(4.5, 6.5)
            elif 10 <= m < 20 or 55 < m <= 80:
                w = random.uniform(1.8, 2.8)
            else:
                w = random.uniform(0.3, 0.9)
        else:
            if (12 <= m <= 45) or (55 <= m <= 88):
                w = random.uniform(2.8, 3.8)
            else:
                w = random.uniform(0.8, 1.4)
        minute_weights.append(w)

    arrivals_per_minute = [0] * 120
    chosen_minutes = random.choices(range(120), weights=minute_weights, k=total_expected)
    for m in chosen_minutes:
        arrivals_per_minute[m] += 1

    return arrivals_per_minute, total_expected


def generate_unique_id(scanned_set):
    """Generates a unique IIT Goa ID (Students: 2301..2603, Faculty/Staff: PROF-xxx)."""
    while True:
        if random.random() < 0.07:
            new_id = f"PROF-{random.randint(101, 199)}"
        else:
            batch = random.choice(["2301", "2401", "2502", "2603"])
            new_id = f"{batch}{random.randint(101, 299)}"
        if new_id not in scanned_set:
            return new_id


# ==============================================================================
# PART 2: ID SCANNER GATE, QUEUE ENGINE & TRAY REFILL LOGIC (Member 2)
# ==============================================================================
def simulate_mess_minute(state, new_gate_arrivals):
    """
    Simulates 1 minute of IIT Goa Mess operation:
    - Step A: Students & Profs arrive at the ID Scanner Gate and scan their ID card.
    - Step B: Scanned members join one of the 3 food counters.
    - Step C: Counters serve food, deplete trays, and trigger 3-min refills when empty.
    """
    state["scanner_queue"] += new_gate_arrivals

    scan_capacity = random.randint(7, 12)
    scanned_now = min(state["scanner_queue"], scan_capacity)
    state["scanner_queue"] -= scanned_now

    latest_ids = []
    for _ in range(scanned_now):
        uid = generate_unique_id(state["scanned_id_set"])
        state["scanned_id_set"].add(uid)
        state["total_headcount"] += 1
        latest_ids.append(uid)

    if latest_ids:
        state["recent_scans"] = latest_ids[-4:]

    for _ in range(scanned_now):
        if random.random() < 0.72:
            chosen_idx = state["queues"].index(min(state["queues"]))
        else:
            chosen_idx = random.choices([0, 1, 2], weights=[0.42, 0.35, 0.23])[0]
        state["queues"][chosen_idx] += 1

    for i in range(3):
        if state["refills"][i] > 0:
            state["refills"][i] -= 1
            if state["refills"][i] == 0:
                state["trays"][i] = 100.0
            continue

        if state["queues"][i] > 0:
            serve_speed = random.randint(2, 4) if i == 2 else random.randint(3, 5)
            served = min(state["queues"][i], serve_speed)
            state["queues"][i] -= served

            state["trays"][i] -= served * random.uniform(1.7, 3.2)
            if state["trays"][i] <= 0:
                state["trays"][i] = 0.0
                state["refills"][i] = 3
                state["refill_count"] += 1

    gate_wait = state["scanner_queue"] * 0.10
    counter_wait = (sum(state["queues"]) / 3.0) * 0.25
    total_wait = round(gate_wait + counter_wait, 1)
    return total_wait


# ==============================================================================
# PART 3: STUDENT ADVISOR & MATPLOTLIB ANALYTICS ENGINE (Member 4)
# ==============================================================================
def make_fresh_state(day, meal, staggered_mode):
    schedule, expected_total = generate_meal_arrival_schedule(day, meal, staggered_mode)
    return {
        "schedule": schedule,
        "expected_total": expected_total,
        "scanner_queue": 0,
        "scanned_id_set": set(),
        "total_headcount": 0,
        "recent_scans": [],
        "queues": [0, 0, 0],
        "trays": [100.0, 100.0, 100.0],
        "refills": [0, 0, 0],
        "refill_count": 0
    }


def open_matplotlib_comparison(day, meal):
    minutes = list(range(120))
    normal_waits = []
    staggered_waits = []

    state_norm = make_fresh_state(day, meal, staggered_mode=False)
    state_stag = make_fresh_state(day, meal, staggered_mode=True)

    for m in minutes:
        w_n = simulate_mess_minute(state_norm, state_norm["schedule"][m])
        normal_waits.append(w_n)

        w_s = simulate_mess_minute(state_stag, state_stag["schedule"][m])
        staggered_waits.append(w_s)

    if HAS_MATPLOTLIB:
        plt.figure(figsize=(8.6, 4.8))
        plt.plot(
            minutes, normal_waits,
            label=f"Normal Rush (Turnout: {state_norm['total_headcount']}/{MAX_CAMPUS_CAPACITY})",
            color="#dc2626", linewidth=2.2
        )
        plt.plot(
            minutes, staggered_waits,
            label=f"Staggered Hostel Timing (Turnout: {state_stag['total_headcount']}/{MAX_CAMPUS_CAPACITY})",
            color="#16a34a", linewidth=2.2
        )
        plt.axhline(y=5.0, color="#475569", linestyle="--", label="5-Min Student Comfort Threshold")
        plt.title(f"IIT Goa Mess Live Wait-Time Analysis: {day} {meal}")
        plt.xlabel("Minutes from Meal Start (0 to 120 mins)")
        plt.ylabel("Estimated Total Wait Time (ID Scan + Counter) [Mins]")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()


# ==============================================================================
# PART 4: TKINTER INTERACTIVE CAMPUS DASHBOARD (Member 3)
# ==============================================================================
class IITGoaMessLiveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IIT Goa Mess Live - ID Scanner, Menu & Queue Simulator (Max 650 Campus)")
        self.root.geometry("970x690")
        self.root.configure(bg="#f1f5f9")

        self.day_var = tk.StringVar(value="Wednesday")
        self.meal_var = tk.StringVar(value="Lunch")
        self.staggered_var = tk.BooleanVar(value=False)

        self.is_running = False
        self.current_minute = 0
        self.peak_wait = 0.0
        self.wait_history = []
        self.state = make_fresh_state("Wednesday", "Lunch", False)

        self.logo_img = None
        self.load_optional_logo()
        self.build_interface()
        self.reset_sim()

    def load_optional_logo(self):
        for fname in ["image_14fe15.jpg", "image_14fe35.png", "image_14fdf3.png", "campus.png", "logo.png"]:
            if os.path.exists(fname):
                try:
                    raw = tk.PhotoImage(file=fname)
                    self.logo_img = raw.subsample(max(1, raw.width() // 85), max(1, raw.height() // 55))
                    break
                except Exception:
                    self.logo_img = None

    def build_interface(self):
        banner = tk.Frame(self.root, bg="#0f172a", pady=10, padx=15)
        banner.pack(fill=tk.X)

        if self.logo_img:
            tk.Label(banner, image=self.logo_img, bg="#0f172a").pack(side=tk.LEFT, padx=(0, 12))

        title_box = tk.Frame(banner, bg="#0f172a")
        title_box.pack(side=tk.LEFT)
        tk.Label(
            title_box, text="IIT GOA MESS LIVE - SMART ID SCANNER & QUEUE SIMULATOR",
            font=("Arial", 15, "bold"), bg="#0f172a", fg="#f8fafc"
        ).pack(anchor="w")
        tk.Label(
            title_box,
            text="Campus Strength: 650 (Students + Profs)  |  Avg: ~400 B'fast | ~500 Lunch/Dinner | ~600 Non-Veg",
            font=("Arial", 10), bg="#0f172a", fg="#94a3b8"
        ).pack(anchor="w")

        self.headcount_badge = tk.Label(
            banner, text="ID SCANNED: 0 / 600 (Max 650)",
            font=("Arial", 12, "bold"), bg="#1d4ed8", fg="white", padx=12, pady=6
        )
        self.headcount_badge.pack(side=tk.RIGHT, padx=5)

        ctrl = tk.Frame(self.root, bg="#e2e8f0", pady=8, padx=12)
        ctrl.pack(fill=tk.X)

        tk.Label(ctrl, text="Day:", font=("Arial", 10, "bold"), bg="#e2e8f0").pack(side=tk.LEFT, padx=(4, 2))
        day_cb = ttk.Combobox(ctrl, textvariable=self.day_var, values=list(IIT_GOA_MENU.keys()), width=10, state="readonly")
        day_cb.pack(side=tk.LEFT, padx=4)
        day_cb.bind("<<ComboboxSelected>>", lambda e: self.reset_sim())

        tk.Label(ctrl, text="Meal:", font=("Arial", 10, "bold"), bg="#e2e8f0").pack(side=tk.LEFT, padx=(8, 2))
        meal_cb = ttk.Combobox(ctrl, textvariable=self.meal_var, values=["Breakfast", "Lunch", "Snacks", "Dinner"], width=10, state="readonly")
        meal_cb.pack(side=tk.LEFT, padx=4)
        meal_cb.bind("<<ComboboxSelected>>", lambda e: self.reset_sim())

        tk.Checkbutton(
            ctrl, text="Staggered Hostel Timing",
            variable=self.staggered_var, command=self.reset_sim,
            font=("Arial", 10, "bold"), bg="#e2e8f0"
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(ctrl, text="Start / Resume", command=self.start_sim, bg="#16a34a", fg="white", font=("Arial", 10, "bold"), padx=8).pack(side=tk.LEFT, padx=4)
        tk.Button(ctrl, text="Pause", command=self.pause_sim, bg="#ca8a04", fg="white", font=("Arial", 10, "bold"), padx=8).pack(side=tk.LEFT, padx=4)
        tk.Button(ctrl, text="New Random Day Run", command=self.reset_sim, bg="#dc2626", fg="white", font=("Arial", 10, "bold"), padx=8).pack(side=tk.LEFT, padx=4)

        if HAS_MATPLOTLIB:
            tk.Button(
                ctrl, text="Plot Wait-Time Graph",
                command=lambda: open_matplotlib_comparison(self.day_var.get(), self.meal_var.get()),
                bg="#2563eb", fg="white", font=("Arial", 10, "bold"), padx=8
            ).pack(side=tk.RIGHT, padx=4)

        self.advisor_banner = tk.Label(
            self.root,
            text="STUDENT LIVE ADVISOR: Press 'Start' to simulate live ID scanning and queue wait times.",
            font=("Arial", 11, "bold"), bg="#dcfce7", fg="#166534", pady=7
        )
        self.advisor_banner.pack(fill=tk.X, padx=14, pady=(8, 4))

        self.canvas = tk.Canvas(self.root, width=940, height=460, bg="white", highlightthickness=1, highlightbackground="#cbd5e1")
        self.canvas.pack(padx=14, pady=4)

    def format_meal_clock(self, minute):
        meal = self.meal_var.get()
        start_hour, start_min, suffix = {
            "Breakfast": (7, 30, "AM"),
            "Lunch": (12, 30, "PM"),
            "Snacks": (4, 30, "PM"),
            "Dinner": (7, 30, "PM")
        }[meal]
        total_m = start_min + minute
        hr = start_hour + (total_m // 60)
        mn = total_m % 60
        if hr > 12:
            hr -= 12
        return f"{hr}:{mn:02d} {suffix}"

    def draw_canvas(self, gate_arrivals=0, total_wait=0.0):
        self.canvas.delete("all")
        day = self.day_var.get()
        meal = self.meal_var.get()
        menu_info = IIT_GOA_MENU[day][meal]
        low_t, high_t = menu_info["target_range"]

        self.canvas.create_rectangle(15, 12, 925, 104, fill="#f8fafc", outline="#94a3b8", width=1)
        self.canvas.create_text(
            28, 30,
            text=f"STEP 1: MANDATORY ID CARD SCANNER GATE  (Arriving This Min: +{gate_arrivals})",
            anchor="w", font=("Arial", 11, "bold"), fill="#0f172a"
        )

        g_q = self.state["scanner_queue"]
        g_width = min(g_q * 9, 310)
        g_col = "#22c55e" if g_q < 8 else ("#eab308" if g_q < 18 else "#ef4444")
        self.canvas.create_text(28, 58, text="ID Gate Queue:", anchor="w", font=("Arial", 10, "bold"), fill="#334155")
        self.canvas.create_rectangle(140, 46, 140 + g_width, 70, fill=g_col, outline="")
        self.canvas.create_text(148 + g_width, 58, text=f"{g_q} waiting to scan ID", anchor="w", font=("Arial", 10, "bold"))

        recent_str = ",  ".join(self.state["recent_scans"]) if self.state["recent_scans"] else "Waiting for first ID scan..."
        self.canvas.create_text(
            28, 86,
            text=f"Latest Scanned IDs (Students & Profs):  [ {recent_str} ]",
            anchor="w", font=("Consolas", 10, "bold"), fill="#1d4ed8"
        )

        clock_str = self.format_meal_clock(self.current_minute)
        self.canvas.create_text(
            910, 30,
            text=f"Mess Clock: {clock_str} (Min {self.current_minute}/120)",
            anchor="e", font=("Arial", 11, "bold"), fill="#0f172a"
        )
        self.canvas.create_text(
            910, 56,
            text=f"Est. Wait: {total_wait} mins  |  Peak Wait: {self.peak_wait} mins",
            anchor="e", font=("Arial", 10, "bold"), fill="#dc2626" if total_wait >= 6 else "#15803d"
        )
        self.canvas.create_text(
            910, 84,
            text=f"Today's Random Turnout Target: {self.state['expected_total']} (Usual Range: {low_t}-{high_t} / 650 Max)",
            anchor="e", font=("Arial", 9, "bold"), fill="#475569"
        )

        counter_titles = [
            f"Counter 1:  {menu_info['c1']}",
            f"Counter 2:  {menu_info['c2']}",
            f"Counter 3:  {menu_info['c3']}"
        ]

        for i in range(3):
            y_top = 122 + i * 108
            self.canvas.create_rectangle(15, y_top, 925, y_top + 96, fill="#ffffff", outline="#cbd5e1")

            q_len = self.state["queues"][i]
            tray_pct = self.state["trays"][i]
            refill_mins = self.state["refills"][i]

            self.canvas.create_text(28, y_top + 18, text=counter_titles[i], anchor="w", font=("Arial", 11, "bold"), fill="#1e293b")

            bar_w = min(q_len * 9, 510)
            q_color = "#22c55e" if q_len < 12 else ("#eab308" if q_len < 25 else "#ef4444")
            self.canvas.create_text(28, y_top + 46, text="Counter Queue:", anchor="w", font=("Arial", 9, "bold"), fill="#475569")
            self.canvas.create_rectangle(135, y_top + 34, 135 + bar_w, y_top + 58, fill=q_color, outline="")
            self.canvas.create_text(
                142 + bar_w, y_top + 46,
                text=f"{q_len} in line (~{round(q_len * 0.25, 1)} min wait)",
                anchor="w", font=("Arial", 10, "bold")
            )

            self.canvas.create_text(28, y_top + 76, text="Food Tray Level:", anchor="w", font=("Arial", 9, "bold"), fill="#475569")
            self.canvas.create_rectangle(135, y_top + 66, 385, y_top + 84, fill="#e2e8f0", outline="#94a3b8")

            if refill_mins > 0:
                self.canvas.create_rectangle(135, y_top + 66, 385, y_top + 84, fill="#f97316", outline="")
                self.canvas.create_text(
                    260, y_top + 75,
                    text=f"TRAY EMPTY - KITCHEN REFILLING ({refill_mins} min left)",
                    font=("Arial", 9, "bold"), fill="white"
                )
            else:
                fill_w = int(2.5 * tray_pct)
                t_col = "#3b82f6" if tray_pct > 25 else "#eab308"
                self.canvas.create_rectangle(135, y_top + 66, 135 + fill_w, y_top + 84, fill=t_col, outline="")
                self.canvas.create_text(
                    395, y_top + 75,
                    text=f"{int(tray_pct)}% left  (Total Refills Today: {self.state['refill_count']})",
                    anchor="w", font=("Arial", 9, "bold")
                )

    def update_student_advisor(self, total_wait):
        if total_wait < 3.5:
            self.advisor_banner.config(
                text=f"GO NOW! Low Crowd (Wait ~{total_wait} mins). ID Scanner & Food Counters are moving smoothly.",
                bg="#dcfce7", fg="#166534"
            )
        elif total_wait < 7.0:
            self.advisor_banner.config(
                text=f"MODERATE CROWD (Wait ~{total_wait} mins). Moving steadily across counters.",
                bg="#fef9c3", fg="#854d0e"
            )
        else:
            self.advisor_banner.config(
                text=f"PEAK RUSH ALERT (Wait ~{total_wait} mins)! Stay in hostel/office for 15-20 mins before visiting.",
                bg="#fee2e2", fg="#991b1b"
            )

    def step_simulation(self):
        if not self.is_running:
            return

        if self.current_minute >= 120 and self.state["scanner_queue"] == 0:
            self.is_running = False
            best_min = self.wait_history.index(min(self.wait_history[15:100])) if len(self.wait_history) > 100 else 10
            best_clock = self.format_meal_clock(best_min)
            self.advisor_banner.config(
                text=f"MEAL FINISHED! Total IDs Scanned: {self.state['total_headcount']} / {MAX_CAMPUS_CAPACITY}  |  Peak Wait: {self.peak_wait}m  |  Best Slot: {best_clock}",
                bg="#dbeafe", fg="#1e40af"
            )
            return

        new_arrivals = self.state["schedule"][self.current_minute] if self.current_minute < 120 else 0
        total_wait = simulate_mess_minute(self.state, new_arrivals)

        self.wait_history.append(total_wait)
        if total_wait > self.peak_wait:
            self.peak_wait = total_wait

        self.headcount_badge.config(
            text=f"ID SCANNED: {self.state['total_headcount']} / {self.state['expected_total']} (Max {MAX_CAMPUS_CAPACITY})"
        )
        self.update_student_advisor(total_wait)
        self.draw_canvas(new_arrivals, total_wait)

        self.current_minute += 1
        self.root.after(150, self.step_simulation)

    def start_sim(self):
        if not self.is_running:
            self.is_running = True
            self.step_simulation()

    def pause_sim(self):
        self.is_running = False

    def reset_sim(self):
        self.is_running = False
        self.current_minute = 0
        self.peak_wait = 0.0
        self.wait_history = []
        day = self.day_var.get()
        meal = self.meal_var.get()
        self.state = make_fresh_state(day, meal, self.staggered_var.get())
        self.headcount_badge.config(
            text=f"ID SCANNED: 0 / {self.state['expected_total']} (Max {MAX_CAMPUS_CAPACITY})"
        )
        self.advisor_banner.config(
            text=f"NEW RANDOM RUN READY: {day} {meal} - Random Turnout Target Generated: {self.state['expected_total']} members (out of 650). Press Start!",
            bg="#e0f2fe", fg="#075985"
        )
        self.draw_canvas(0, 0.0)


if __name__ == "__main__":
    root = tk.Tk()
    app = IITGoaMessLiveApp(root)
    root.mainloop()
